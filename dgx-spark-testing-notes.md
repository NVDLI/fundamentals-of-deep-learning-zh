# DGX Spark 测试记录

本文档记录了在 NVIDIA DGX Spark（ARM64 + Grace Blackwell GB10 架构）上端到端运行本课程期间发现的
全部问题、根因及修复方式，供内部评审参考。除非另有说明，所有修复均已提交到本仓库（GitLab）；
是否同步到 GitHub 公开仓库需视 DGX Spark 说明的发布审批情况而定（见文末"仓库同步说明"）。

## 一、环境与基础设施问题

| # | 问题 | 根因 | 修复方式 | 状态 |
|---|---|---|---|---|
| 1 | `docker build` 在 DGX Spark 上直接失败 | 仓库自带 `Dockerfile` 基于 `pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime`——仅提供 x86_64 版本，且 CUDA 11.8 早于 Blackwell 架构 | 改用 `nvcr.io/nvidia/pytorch:25.10-py3`（首个支持 GB10 的 NGC 镜像），独立为 `Dockerfile.spark` | ✅ 已修复 |
| 2 | 从中国大陆网络 `git clone`/`git pull` 报 `GnuTLS recv error` | 对 github.com 的 HTTP/2 连接间歇性受干扰 | `git config --global http.version HTTP/1.1` | ✅ 已修复 |
| 3 | 容器内 `pip install` 报 `Name or service not known` | 容器继承了宿主机的 `127.0.0.53`（systemd-resolved stub），容器内不可用 | 在 `/etc/docker/daemon.json` 中添加 `"dns": ["8.8.8.8", "114.114.114.114"]` 并重启 Docker（注意 `--network host` 无法解决此问题） | ✅ 已修复 |
| 4 | `import torch` 报 `Failed to initialize NumPy: _ARRAY_API not found` | 安装 `requirements.txt` 会将 NumPy 升级到 2.x，覆盖 NGC 镜像中与 NumPy 1.x 链接的 PyTorch 构建 | 在同一 pip 安装层显式钉住 `numpy<2` | ✅ 已修复 |
| 5 | `torch.compile()` 报 `'sm_121' is not a recognized processor` | Triton 编译后端对 GB10（sm_121）的支持缺口，即使在 `25.10-py3` 上仍可能出现 | `-e TORCHDYNAMO_DISABLE=1` 容器环境变量——使所有 `torch.compile()` 静默降级为不编译，无需修改任何 Notebook；未设置该变量的其他 GPU 平台不受影响 | ✅ 已修复 |
| 6 | JupyterLab 打开后显示 `/workspace` 而非课程目录 | 直接运行裸 NGC 镜像时未指定 `--notebook-dir` | `--notebook-dir=/dli/tutorials` 已写入 `Dockerfile.spark` 的 `CMD` | ✅ 已修复 |
| 7 | 容器内 Notebook 内容陈旧，`git pull` 后仍不更新 | 容器重建时遗漏了 `-v` 绑定挂载参数，实际运行的是镜像构建时刻的快照（`Mounts: []`） | 使用 `-v <宿主机路径>:/dli` 重新创建容器 | ✅ 已修复 |
| 8 | `huggingface_hub` 报 `Network is unreachable` | 两个叠加原因：(a) Docker 默认网桥无 IPv6 路由（与地域无关，Docker 通用限制）；(b) 从中国大陆网络访问 `huggingface.co` 的 IPv4 连接被静默丢弃 | `-e HF_ENDPOINT=https://hf-mirror.com` | ✅ 已修复 |
| 9 | ASL 数据集下载缓慢，偶发 `IncompleteRead` | `huggingface_hub` 的 Xet 存储后端从美国节点提供该文件，自带断点续传重试机制，但耗时较长（15–20 分钟） | 已在 `DGX_SPARK.md` 中记录为预期行为，无需人工干预 | ✅ 已记录 |
| 10 | Kaggle（05b）数据集下载极慢（约 56 kB/s，耗时约 1 小时），中断后无断点续传 | Kaggle 文件托管于 Google Cloud Storage，从中国大陆网络访问受到严重限速；`download_kagglehub_dataset()` 本身不含重试/续传逻辑，中断后需清空 `data/datasets/` 重新下载 | 已确认最终可下载成功（非凭据问题，与 `DGX_SPARK.md` 当前文字描述不符） | ⏳ **待办**——`DGX_SPARK.md` 已知问题列表中仍写着"可能需要 Kaggle 账号凭据"，需改为准确描述（无需凭据，但需预留约 1 小时且不支持断点续传） |

## 二、Notebook 内容缺陷（中文版）

| # | 问题 | 根因 | 修复方式 | 状态 |
|---|---|---|---|---|
| 11 | `02_asl`/`03_asl_cnn`/`04a`：`pd.read_csv()` 报错，`data/asl_data/` 从未被创建 | 中文翻译遗漏了英文原版中触发下载的 `download_asl_dataset()` 调用单元格 | 在三个 Notebook 中补回对应的 import 与调用 | ✅ 已修复并推送 |
| 12 | `02_asl`："2.2.1 Kaggle" 小节描述的数据来源与实际不符 | 数据源已从 Kaggle 的 `sign-language-mnist` 迁移至 HuggingFace 镜像，但说明文字未同步更新 | 改写为"2.2.1 HuggingFace"，准确描述实际来源 | ✅ 已修复并推送 |
| 13 | `02_asl`/`04b`：正文写训练/验证集为 27,455 / 7,172 张，实际为 19,200 / 4,800 张 | 沿用了旧版 Kaggle 数据集的数字，未随 HuggingFace 迁移更新（英文原版存在相同问题） | 根据实测与算式核实（36 个原始类别中保留 24 个）后更正数字 | ✅ 已修复并推送 |
| 14 | 提交的 Notebook 中混入本地执行痕迹（`kagglehub` 报错回溯、`execution_count`、`language_info.version` 被覆盖） | 在独立的本机 Windows Jupyter 环境中测试时产生的执行残留，恰好也是同一份被 OneDrive 同步的文件 | 提交前按仓库 `CONTRIBUTING.md` 的要求清除所有输出与执行元数据 | ✅ 已修复并推送 |
| 15 | `04b`：`torch.load()` 报 `UnpicklingError` | PyTorch ≥2.6 将 `weights_only` 默认值改为 `True`；`04a` 保存的是完整模型对象而非 `state_dict()`（英文原版存在相同问题） | 为 `torch.load()` 增加 `weights_only=False`（该文件由用户本人上一节课生成，可信） | ✅ 已修复并推送 |
| 16 | `06_nlp`：正文写 token 数为 23，实际输出为 24；相邻文字有重复的"是" | 中文翻译笔误（英文原版正确写的是 24） | 更正为 24，并清理重复字符 | ✅ 已修复并推送 |
| 17 | `04b`：正文引用了不存在的 `data/asl_images` 文件夹 | 说明文字残留旧文件夹名，实际代码与文件从来都在 `images/` 下（英文原版存在相同问题）；代码本身无误，仅正文文字有误 | 将三处 `data/asl_images` 更正为 `images` | ✅ 已修复并推送 |
| 18 | `05b_corgi_door`：文件末尾存在一个多余的重复页眉图片单元格 | 该重复早于本次测试即已存在于仓库中；GitHub 上后续的页眉清理提交只删除了开头的页眉，遗漏了文末这一处 | 删除该多余单元格，确保全部 9 个 Notebook 均无页眉图片 | ✅ 已修复并推送 |
| 19 | `02_asl`："构建模型"练习的解答代码单元格默认展开显示，未按预期折叠 | 该单元格缺少 `"jupyter": {"source_hidden": true}` 元数据，是本课程唯一一处此类缺陷（已用三种独立方法交叉核实全部 9 个 Notebook） | 补回缺失的元数据 | ✅ 已修复并推送 |

## 三、README / 文档问题

| # | 问题 | 处理方式 | 状态 |
|---|---|---|---|
| 20 | README "2. 使用 Docker 运行" 一节直接给出 `docker build` 命令，未包含克隆步骤，脱离上下文单独阅读会因找不到 `Dockerfile` 而失败 | 补充与选项 1 相同的 `git clone && cd` 代码块，使每个快速开始选项自成一体 | ✅ 已修复并推送（GitLab + GitHub） |
| 21 | DGX Spark 说明占据 README 全文 230 行中的 129 行，远超其余三个平台选项之和 | 拆分为独立文件 `DGX_SPARK.md`，README 中仅保留一行指引 | ✅ 已修复（仅 GitLab，见下文"仓库同步说明"） |

## 四、确认为非缺陷的情况（避免future重复排查）

| # | 表面现象 | 实际情况 |
|---|---|---|
| 22 | `01_mnist` 下载 MNIST 时 `yann.lecun.com` 返回 404 | 属预期行为——`torchvision` 自动切换至第二镜像源（`ossci-datasets.s3.amazonaws.com`）并下载成功，与地域或网络限制无关 |
| 23 | `06_nlp` 加载 BERT 时提示 `UNEXPECTED` 权重（`cls.seq_relationship.*`、`bert.pooler.*`） | 属预期行为——`bert-base-cased` 原始预训练包含 NSP 头与 pooler 层，而 `BertForMaskedLM` 不使用这两部分；库自身的提示信息已说明这种情况可以忽略 |
| 24 | 在 GitHub 网页上直接预览 Notebook 时，所有"点击 `...` 查看解答"对应的代码单元格均显示为展开状态 | 非 Notebook 文件本身的问题——GitHub 的网页预览通过独立的静态渲染服务（`notebooks.githubusercontent.com`），并非真正的 JupyterLab，不支持 `jupyter.source_hidden` 折叠交互；元数据本身完全正确，在真实 JupyterLab（Docker / Brev / DGX Spark 等所有实际运行方式）中均按预期折叠 |

## 五、仓库同步说明

测试期间发现，公开的 GitHub 仓库（`NVDLI/fundamentals-of-deep-learning-zh`）在独立于本次测试的情况下
向前推进了 11 个提交，包含全部 9 个 Notebook 的页眉图片清理，以及**完整移除了 README 中的 DGX Spark
说明**。经确认，这是有意为之的流程：

- **GitLab**（本仓库）：作为内部评审阶段的"暂存"仓库，保留完整的 DGX Spark 说明（`DGX_SPARK.md` +
  README 指引），供内部评审通过后再发布。
- **GitHub**：作为面向学员的公开仓库，在 DGX Spark 说明通过内部评审前不包含相关内容；README 与
  GitLab 版本刻意保持差异，仅此一点。
- **Notebook 内容**：两个仓库需保持完全一致——GitHub 一侧独立产生的页眉清理已合并回 GitLab，
  本文档记录的全部 Notebook 修复也已同步推送至两侧。

后续每次修改 Notebook 内容时，需分别推送到两个远程仓库；如涉及 README，除非同时更新 GitHub 发布状态，
否则应仅推送至 GitLab。
