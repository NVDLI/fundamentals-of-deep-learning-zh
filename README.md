# 深度学习基础

[![在 Brev 上启动](https://img.shields.io/badge/Launch%20on-Brev-76B900)](https://brev.nvidia.com/) [![许可证: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/) [![许可证](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)

《深度学习基础》是 NVIDIA 深度学习培训中心（DLI）推出的一门开源实践课程，通过交互式 Jupyter Notebook 介绍神经网络、卷积架构与迁移学习。

## 学习成果

完成本课程的实验后，学员将能够：

- 使用 PyTorch 在真实图像数据集上构建并训练神经网络
- 将卷积神经网络（CNN）应用于图像分类任务
- 利用数据增强与迁移学习提升有限数据集上的模型精度
- 理解偏差-方差权衡，并掌握应对过拟合的技术手段
- 部署已训练的模型，对新的未见数据进行预测

## 课程模块

| # | 模块 | 幻灯片 | Notebook |
|---|---|----------|--------|
| 01 | 深度学习简介 | [slides_01.pptx](./course_content/slides/part1.pptx) | [01_mnist.ipynb](./course_content/tutorials/01_mnist.ipynb) |
| 02 | 神经网络的训练方式 | [slides_02.pptx](./course_content/slides/part2.pptx) | [02_asl.ipynb](./course_content/tutorials/02_asl.ipynb) |
| 03 | 卷积神经网络 | [slides_03.pptx](./course_content/slides/part3.pptx) | [03_asl_cnn.ipynb](./course_content/tutorials/03_asl_cnn.ipynb) |
| 04 | 数据增强与模型部署 | [slides_04.pptx](./course_content/slides/part4.pptx) | [04a_asl_augmentation.ipynb](./course_content/tutorials/04a_asl_augmentation.ipynb) <br> [04b_asl_predictions.ipynb](./course_content/tutorials/04b_asl_predictions.ipynb) |
| 05 | 预训练模型 | [slides_05.pptx](./course_content/slides/part5.pptx) | [05a_doggy_door.ipynb](./course_content/tutorials/05a_doggy_door.ipynb) <br> [05b_corgi_door.ipynb](./course_content/tutorials/05b_corgi_door.ipynb) |
| 06 | 高级架构 | [slides_06.pptx](./course_content/slides/part6.pptx) | [06_nlp.ipynb](./course_content/tutorials/06_nlp.ipynb)  |


## 使用方法

### 快速开始

#### 1. 克隆并在本地运行

```bash
git clone https://github.com/NVDLI/fundamentals-of-deep-learning-zh.git
cd fundamentals-of-deep-learning-zh/course_content
```

**前置条件：** Python 3.9+、配备 CUDA 11.8+ 的 NVIDIA GPU（仅 CPU 也可运行，但后续 Notebook 速度较慢），以及 conda 或 pip。

```bash
pip install -r environment/requirements.txt
jupyter lab
```

然后在浏览器中打开 <http://localhost:8888>，导航至 `tutorials/` 目录。

#### 2. 使用 Docker 运行

使用提供的 `Dockerfile` 部署内容：

```bash
docker build -t fdl-app . && docker run -d -p 8888:8888 --name fdl-container --gpus all fdl-app
```

然后在浏览器中打开 <http://localhost:8888>，导航至 `tutorials/` 目录。

#### 3. 使用 Brev 启动

🌟 [在 NVIDIA Brev 上启动本课程](https://brev.nvidia.com/)

1. 点击上方的 **Launch on Brev** 按钮（或本 README 顶部的徽章）。
2. 登录或免费注册 NVIDIA Brev 账号。
3. 选择 GPU 实例——NVIDIA T4 或 L4 已足够运行所有五个实验。
4. 点击 **Deploy**。环境将在约 2 分钟内准备就绪，CUDA、Python 及所有依赖均已预装。
5. 在 Brev 控制台打开 JupyterLab，导航至 `course_content/tutorials/` 目录。

#### 4. 在 NVIDIA DGX Spark 上运行

DGX Spark 搭载 GB10（Grace Blackwell）超级芯片，CPU 为 **ARM64（aarch64）** 架构，GPU 计算能力为
**sm_121**。仓库自带的 `course_content/Dockerfile` 基于 `pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime`
镜像，该镜像仅提供 x86_64 版本，且基于 CUDA 11.8（早于 Blackwell 架构），因此**无法在 DGX Spark 上直接构建**。
需要改用 NVIDIA NGC 提供的多架构镜像。

**前置条件：** 已在 DGX Spark 上安装 Docker 与 NVIDIA Container Toolkit（DGX OS 默认已包含）。

**第一步：登录 NGC 镜像仓库**（`nvcr.io/nvidia/pytorch` 为公开镜像，无需 API Key 即可拉取；如遇权限问题，可在
[ngc.nvidia.com](https://ngc.nvidia.com/) 免费注册账号，在**账号设置（Account Settings）→ API Key** 中生成密钥后执行
`docker login nvcr.io`，用户名填 `$oauthtoken`，密码填 API Key）。

**第二步：克隆仓库并新建针对 Spark 的 Dockerfile**（不要直接修改 `course_content/Dockerfile`，避免影响其他平台的构建）：

```bash
git clone https://github.com/NVDLI/fundamentals-of-deep-learning-zh.git
cd fundamentals-of-deep-learning-zh/course_content
```

```bash
cat > Dockerfile.spark << 'EOF'
FROM nvcr.io/nvidia/pytorch:25.10-py3

ARG PIP_INDEX_URL=https://pypi.org/simple
ENV PIP_INDEX_URL=${PIP_INDEX_URL}

COPY ./environment/requirements.txt .
RUN pip install -r requirements.txt "numpy<2"

ENV PYTHONPATH=/dli
WORKDIR /dli/
COPY . .
WORKDIR /dli/tutorials

EXPOSE 8888
CMD ["jupyter", "lab", \
     "--ip=0.0.0.0", \
     "--allow-root", \
     "--no-browser", \
     "--NotebookApp.token=", \
     "--NotebookApp.password="]
EOF
```

> **为什么是 `25.10-py3`？** NGC PyTorch 镜像从 25.10 版本起才开始为 GB10（sm_121）提供支持。
> 低于该版本的镜像（例如 24.08、25.01、25.09）在 `import torch` 与常规张量运算（eager 模式）时
> 看起来正常，但一旦调用 `torch.compile()`（本课程 01、02、03、04a 四个 Notebook 中均有使用）
> 会报错 `'sm_121' is not a recognized processor for this target` 并导致训练失败。
>
> **`torch.compile()` 在 GB10 上目前仍可能报错。** 即使使用 `25.10-py3`，其内置的 Triton
> 编译后端对 sm_121 的支持也可能不完整，因此上述报错仍可能出现——这是 GB10（Blackwell 架构）
> 生态适配尚不成熟导致的已知限制，而非本仓库的配置问题。上方 `docker run` 命令中的
> `-e TORCHDYNAMO_DISABLE=1` 会让所有 `torch.compile(...)` 调用静默降级为直接返回原模型
> （即不进行任何编译优化），四个 Notebook 无需任何修改即可正常运行。这只会让训练速度略慢
> （本课程模型很小，几乎无感知），不影响正确性。若在其他支持 `torch.compile` 的 GPU（如
> RTX 3500 等消费级/工作站显卡）上运行，请不要设置该环境变量，以便获得完整的编译加速效果。
>
> **为什么额外加装 `numpy<2`？** NGC 镜像自带的 PyTorch 编译时链接的是 NumPy 1.x。安装
> `requirements.txt` 中的 pandas / matplotlib / opencv-python 等依赖会把 NumPy 升级到 2.x，
> 导致 PyTorch 的 NumPy 桥接失效（报错 `A module that was compiled using NumPy 1.x cannot be
> run in NumPy 2.2.6` 及 `Failed to initialize NumPy: _ARRAY_API not found`），因此需要在同一层
> 显式钉住 NumPy 主版本。

**第三步：构建镜像**（体积较大，视网络情况需 5–15 分钟）：

```bash
docker build -t fdl-app -f Dockerfile.spark .
```

**第四步：运行容器**（用绑定挂载替代镜像内置副本，这样下载的数据集、训练产生的文件以及对
Notebook 的修改都会保留在宿主机上，不会随容器删除而丢失）：

```bash
docker rm -f fdl-container 2>/dev/null
docker run -d \
  --name fdl-container \
  --gpus all \
  --shm-size=2g \
  -p 8888:8888 \
  -e TORCHDYNAMO_DISABLE=1 \
  -v "$(pwd)":/dli \
  fdl-app
```

**第五步：验证 GPU 是否可用**（建议在打开 Notebook 前先做一次快速检查）：

```bash
docker exec fdl-container python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

应输出 `True NVIDIA GB10`。

**第六步：打开 JupyterLab。** 若从其他电脑通过局域网访问，请使用 DGX Spark 的 IP 地址而非
`localhost`（可在 Spark 上执行 `ip addr show` 查看）：

```
http://<DGX-Spark-IP地址>:8888
```

容器已将工作目录设为 `tutorials/`，因此打开后会直接看到全部 Notebook，无需再手动进入子目录。

**停止与重新启动容器：**

```bash
docker stop fdl-container      # 停止
docker start fdl-container     # 重新启动（数据与已装依赖均保留）
docker rm -f fdl-container     # 彻底删除
```

**已知问题：**

- `torch.compile()`（01、02、03、04a 四个 Notebook 均有使用）在 GB10 上可能报错
  `'sm_121' is not a recognized processor for this target`。上方 `docker run` 命令已包含的
  `-e TORCHDYNAMO_DISABLE=1` 会让其静默降级为不编译，无需修改 Notebook；详见第二步下方说明。
- 06_nlp.ipynb 会从 HuggingFace 下载 BERT 模型（约 1.3 GB）；05a/05b 会从
  `download.pytorch.org` 下载 VGG16 预训练权重（约 528 MB）；05b_corgi_door.ipynb 通过
  `kagglehub` 下载数据集，可能需要 Kaggle 账号凭据。请确保 DGX Spark 可以访问公网，
  或提前准备好相应的凭据/镜像文件。
- 若所在网络访问 GitHub、HuggingFace 或 PyPI 不稳定（例如中国大陆网络环境），可在
  `docker build` 时追加 `--build-arg PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple`，
  并在 `docker run` 时追加 `-e HF_ENDPOINT=https://hf-mirror.com`；如遇 Docker 容器内 DNS
  解析失败（`Name or service not known`），需在宿主机 `/etc/docker/daemon.json` 中显式配置
  `"dns": ["8.8.8.8", "114.114.114.114"]` 后执行 `sudo systemctl restart docker`
  （注意 `--network host` 无法解决此问题，因为它会直接复用宿主机可能存在问题的 DNS 解析器）。
- 即使已设置 `HF_ENDPOINT` 镜像，在网络不稳定的环境下下载数据集（如 02_asl.ipynb 中约 300MB 的
  ASL 数据集）仍可能显示多次 `Error while downloading ... Trying to resume download...`。这是
  `huggingface_hub` 自带的断点续传重试机制，属正常现象，请耐心等待其自动完成，无需手动干预；
  整个下载过程可能耗时 15–20 分钟。

## 贡献

我们欢迎社区贡献。贡献步骤如下：

1. Fork 此仓库并创建功能分支：
   ```bash
   git checkout -b feature/your-improvement
   ```
2. 进行修改。提交前请确保清除 Notebook 中的所有输出。
3. 提交 Pull Request，并清晰描述变更内容及原因。

对于重大变更或新增 Notebook，请先提交 Issue 进行讨论。
请勿提交数据集或大型二进制文件——请使用下载脚本代替。

详见 [CONTRIBUTING](CONTRIBUTING.md)。

## 许可证

本仓库采用混合许可模式：

- 源代码文件及 Jupyter Notebook 中的代码单元格：
  [Apache 许可证 2.0](LICENSES/Apache-2.0.txt)
- 文档、Markdown 及 Notebook 原始单元格、NVIDIA 制作的教育媒体：
  [知识共享署名 4.0 国际许可协议](LICENSES/CC-BY-4.0.txt)
- 第三方材料：其原始许可证，详见
  [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

每个完整的 Jupyter Notebook 采用双重许可：代码单元格遵循 Apache-2.0，非代码单元格遵循 CC-BY-4.0。合并双重许可条款详见
[LICENSES/CC-BY-4.0-Apache2_Dual_License.txt](LICENSES/CC-BY-4.0-Apache2_Dual_License.txt)。

NVIDIA 的名称、徽标和商标不授权一般性重复使用。
