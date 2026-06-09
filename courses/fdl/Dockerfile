# PyTorch + CUDA 11.8 + cuDNN 8 — requires NVIDIA GPU + nvidia-container-toolkit on the host
# Run with: docker run --gpus all ...
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Avoid interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# System deps (Pillow needs libjpeg/libpng)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libjpeg-turbo8 \
        libpng16-16 \
        git \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# Python packages
RUN pip install --no-cache-dir \
        jupyterlab==4.* \
        ipywidgets \
        torchvision==0.16.* \
        transformers==4.35.* \
        pillow \
        matplotlib \
        numpy \
        pandas \
	datasets
 

# Shell niceties
ENV SHELL=/bin/bash
ENV PYTHONPATH=/dli/task

WORKDIR /dli/task
COPY tutorials/ .

EXPOSE 8888

CMD ["jupyter", "lab", \
     "--ip=0.0.0.0", \
     "--allow-root", \
     "--no-browser", \
     "--NotebookApp.token=", \
     "--NotebookApp.password=", \
     "--NotebookApp.base_url=/lab"]
