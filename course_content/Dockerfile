# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# Base image: pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime (PyTorch 2.4.1 + CUDA 11.8 + cuDNN 9),
# pulled by the user from Docker Hub. Requires an NVIDIA GPU + nvidia-container-toolkit on the host.
# Run with: docker run --gpus all ...
FROM pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime

# Avoid interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# System deps (Pillow needs libjpeg/libpng)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libjpeg-turbo8 \
        libpng16-16 \
        git \
        gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ./environment/requirements.txt .
RUN pip install -r requirements.txt


# Pinned JupyterLab and ipywidgets (direct runtime dependencies; see THIRD_PARTY_NOTICES.md)
RUN pip install --upgrade jupyterlab==4.2.0
RUN pip install ipywidgets==8.1.2

ENV SHELL=/bin/bash
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
