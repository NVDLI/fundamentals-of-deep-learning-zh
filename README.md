# 深度学习基础

[![许可证: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/) [![许可证](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)

《深度学习基础》是 NVIDIA 深度学习培训中心（DLI）推出的一门开源实践课程，通过交互式 Jupyter Notebook 介绍神经网络、卷积架构与迁移学习。

访问[NVIDIA 培训和认证中文官网](https://www.nvidia.cn/training/)，探索全系列课程、培训机会及 NVIDIA 认证项目，加速 AI 技能进阶与职业发展。

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

```bash
git clone https://github.com/NVDLI/fundamentals-of-deep-learning-zh.git
cd fundamentals-of-deep-learning-zh/course_content
```

使用提供的 `Dockerfile` 部署内容：

```bash
docker build -t fdl-app . && docker run -d -p 8888:8888 --name fdl-container --gpus all fdl-app
```

然后在浏览器中打开 <http://localhost:8888>，导航至 `tutorials/` 目录。

#### 3. 在自建的云端 GPU 实例上运行（例如 NVIDIA Brev）

NVIDIA 仅以源码和 `Dockerfile` 的形式发布本课程，不提供预构建的容器镜像，也不提供托管的运行环境。
如需使用云端 GPU，可自行在 [NVIDIA Brev](https://brev.nvidia.com/) 等平台创建 GPU 实例（NVIDIA T4 或 L4 即可运行全部实验），
然后在实例中按照上文“1. 克隆并在本地运行”或“2. 使用 Docker 运行”的步骤，从本仓库自行搭建环境。

#### 4. 在 NVIDIA DGX Spark 上运行

DGX Spark（ARM64 + Blackwell GB10 架构）需要专门的构建流程，与上述平台不同。详细步骤、已知问题及排查方法请参见
[DGX_SPARK.md](DGX_SPARK.md)。

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

本仓库采用双重许可：文档、技能与素材（documentation/skills/assets）遵循 CC-BY-4.0，源代码遵循 Apache-2.0。
两份许可证的完整文本见根目录 [LICENSE](LICENSE)；单独的副本另见 [LICENSES/CC-BY-4.0.txt](LICENSES/CC-BY-4.0.txt)
与 [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt)。

- 源代码文件及 Jupyter Notebook 中的代码单元格：Apache-2.0
- 文档、Notebook 中的 Markdown 及原始单元格、NVIDIA 制作的教育媒体：CC-BY-4.0
- 每个完整的 Jupyter Notebook 同时包含两种许可的内容：代码单元格遵循 Apache-2.0，非代码单元格遵循 CC-BY-4.0。

以下内容不适用上述许可：

- 公有领域素材：ASL 手语字母表图片
  [`course_content/tutorials/images/asl.png`](course_content/tutorials/images/asl.png)
  （原文件名 Asl_alphabet_gallaudet.png，作者 Ds13 (Darren Stone)）属于公有领域，详见
  [LICENSES/LicenseRef-Public-Domain.txt](LICENSES/LicenseRef-Public-Domain.txt)。
- 其他第三方材料（图片、数据集、依赖软件包等）：遵循其原始许可证，详见
  [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 与 [REUSE.toml](REUSE.toml)。
- Microsoft 365 高级创意内容：`course_content/slides/` 中幻灯片所含的 Microsoft 365 图库图片和图标不在本项目的开源许可范围内，
  具体位置见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

NVIDIA 的名称、徽标和商标不授权一般性重复使用。
