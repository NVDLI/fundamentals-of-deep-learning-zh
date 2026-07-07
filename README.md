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
| 01 | 深度学习简介 | [slides_01.pptx](./course_content/slides/slides_01.pptx) | [01_mnist.ipynb](./course_content/tutorials/01_mnist.ipynb) |
| 02 | 神经网络的训练方式 | [slides_02.pptx](./course_content/slides/slides_02.pptx) | [02_asl.ipynb](./course_content/tutorials/02_asl.ipynb) |
| 03 | 卷积神经网络 | [slides_03.pptx](./course_content/slides/slides_03.pptx) | [03_asl_cnn.ipynb](./course_content/tutorials/03_asl_cnn.ipynb) |
| 04 | 数据增强与模型部署 | [slides_04.pptx](./course_content/slides/slides_04.pptx) | [04a_asl_augmentation.ipynb](./course_content/tutorials/04a_asl_augmentation.ipynb) <br> [04b_asl_predictions.ipynb](./course_content/tutorials/04b_asl_predictions.ipynb) |
| 05 | 预训练模型 | [slides_05.pptx](./course_content/slides/slides_05.pptx) | [05a_doggy_door.ipynb](./course_content/tutorials/05a_doggy_door.ipynb) <br> [05b_corgi_door.ipynb](./course_content/tutorials/05b_corgi_door.ipynb) |
| 06 | 高级架构 | [slides_06.pptx](./course_content/slides/slides_06.pptx) | [06_nlp.ipynb](./course_content/tutorials/06_nlp.ipynb)  |

> 注意：由于仓库大小限制，幻灯片未包含在此 GitLab 分支中。
> 如需查阅，幻灯片已上传至 Google Drive：[幻灯片](https://drive.google.com/drive/folders/1ShCS0EOAG26cuLRkedbt5t_qPzmPoyHW?usp=sharing)。
> 正式发布前将添加至公开 GitHub 仓库。

## 使用方法

### 快速开始

#### 1. 使用 Brev 启动（推荐）

🌟 [在 NVIDIA Brev 上启动本课程](https://brev.nvidia.com/)

1. 点击上方的 **Launch on Brev** 按钮（或本 README 顶部的徽章）。
2. 登录或免费注册 NVIDIA Brev 账号。
3. 选择 GPU 实例——NVIDIA T4 或 L4 已足够运行所有五个实验。
4. 点击 **Deploy**。环境将在约 2 分钟内准备就绪，CUDA、Python 及所有依赖均已预装。
5. 在 Brev 控制台打开 JupyterLab，导航至 `course_content/tutorials/` 目录。

#### 2. 克隆并在本地运行

```bash
git clone https://github.com/NVDLI/fundamentals-of-deep-learning.git
cd course_content
```

**前置条件：** Python 3.9+、配备 CUDA 11.8+ 的 NVIDIA GPU（仅 CPU 也可运行，但后续 Notebook 速度较慢），以及 conda 或 pip。

```bash
pip install -r environment/requirements.txt
jupyter lab
```

然后在浏览器中打开 <http://localhost:8888>，导航至 `tutorials/` 目录。

#### 3. 使用 Docker 运行

使用提供的 `Dockerfile` 部署内容：

```bash
docker build -t fdl-app . && docker run -d -p 8888:8888 --name fdl-container --gpus all fdl-app
```

然后在浏览器中打开 <http://localhost:8888>，导航至 `tutorials/` 目录。

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

每个完整的 Jupyter Notebook 同时包含 Apache-2.0 代码单元格和 CC-BY-4.0 非代码单元格。

NVIDIA 的名称、徽标和商标不授权一般性重复使用。
