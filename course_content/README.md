# 深度学习基础课程 Notebook

本仓库包含一门深度学习实践课程的 Jupyter Notebook 及环境配置文件。课程内容涵盖图像分类、卷积神经网络、数据增强、模型部署、迁移学习与自然语言处理。

## 仓库结构

```text
.
├── Dockerfile
├── environment/
│   ├── entrypoint.sh
│   └── requirements.txt
└── tutorials/
    ├── 00_jupyterlab.ipynb
    ├── 01_mnist.ipynb
    ├── 02_asl.ipynb
    ├── 03_asl_cnn.ipynb
    ├── 04a_asl_augmentation.ipynb
    ├── 04b_asl_predictions.ipynb
    ├── 05a_doggy_door.ipynb
    ├── 05b_corgi_door.ipynb
    ├── 06_nlp.ipynb
    └── utils.py
```

### `Dockerfile`

基于 `pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime` 构建 JupyterLab 环境。它会安装 Notebook 所需的 Python 包，将 `tutorials/` 内容复制至 `/dli/tutorials`，暴露端口 `8888`，并启动 JupyterLab。

该 Docker 镜像适用于安装了 NVIDIA GPU 与 `nvidia-container-toolkit` 的主机。

### `environment/`

包含环境配置文件：

- `requirements.txt`：使用 `pip` 运行 Notebook 所需的 Python 依赖。
- `entrypoint.sh`：适用于以 shell 入口点启动的环境的 JupyterLab 启动脚本。

### `tutorials/`

包含课程 Notebook：

- `00_jupyterlab.ipynb`：JupyterLab 介绍与基本操作流程。
- `01_mnist.ipynb`：使用 MNIST 手写数字数据集进行图像分类。
- `02_asl.ipynb`：使用美国手语数据集进行图像分类。
- `03_asl_cnn.ipynb`：用于图像分类的卷积神经网络。
- `04a_asl_augmentation.ipynb`：通过数据增强提升模型泛化能力。
- `04b_asl_predictions.ipynb`：使用已训练模型进行预测。
- `05a_doggy_door.ipynb`：使用预训练模型。
- `05b_corgi_door.ipynb`：基于预训练模型的迁移学习。
- `06_nlp.ipynb`：序列数据的自然语言处理。
- `utils.py`：Notebook 共用的辅助代码。

## 使用 Docker 运行

在此目录下构建镜像：

```bash
docker build -t fdl-course .
```

运行 JupyterLab：

```bash
docker run --rm -it --gpus all -p 8888:8888 fdl-course
```

然后打开：

```text
http://localhost:8888/lab
```

若希望将 Notebook 的修改保存到本地，运行容器时挂载 `tutorials/` 目录：

```bash
docker run --rm -it --gpus all -p 8888:8888 \
  -v "$PWD/tutorials:/dli/tutorials" \
  fdl-course
```

如果端口 `8888` 已被占用，可映射至其他本地端口：

```bash
docker run --rm -it --gpus all -p 8890:8888 fdl-course
```

然后打开 `http://localhost:8890/lab`。

## 使用 `pip` 在本地运行

如不使用 Docker，可创建 Python 虚拟环境并从 `environment/requirements.txt` 安装依赖。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r environment/requirements.txt
```

从仓库目录启动 JupyterLab：

```bash
jupyter lab tutorials
```

或直接运行 `environment/entrypoint.sh` 脚本：

```bash
sh environment/entrypoint.sh
```

JupyterLab 启动后将在终端打印本地 URL，在浏览器中打开该 URL，然后在文件浏览器中选择 Notebook 即可。

## 注意事项

- 部分 Notebook 在首次运行时可能需要下载数据集或预训练模型文件。
- Docker 配置使用了支持 CUDA 的 PyTorch 镜像。对于没有 NVIDIA GPU 的机器，本地 `pip` 安装通常是更简便的选择。
- 在运行 JupyterLab 的终端中按 `Ctrl+C` 可停止服务。
