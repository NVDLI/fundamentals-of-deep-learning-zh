# Fundamentals of Deep Learning

[![Launch on Brev](https://img.shields.io/badge/Launch%20on-Brev-76B900)](https://brev.nvidia.com/) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)

Fundamentals of Deep Learning is an open-source, hands-on course from the NVIDIA Deep Learning Institute (DLI) that introduces neural networks, convolutional architectures, and transfer learning through interactive Jupyter notebooks.

## Learning Outcomes

In these labs, learners will:

- Build and train neural networks using PyTorch on real image datasets
- Apply convolutional neural networks (CNNs) to image classification tasks
- Use data augmentation and transfer learning to improve accuracy on limited data
- Manage the bias-variance tradeoff and apply techniques to address overfitting
- Deploy a trained model to make predictions on new, unseen data

## Usage

### Getting Started

#### 1. Launch with Brev (Recommended)

🌟 [Launch this course on NVIDIA Brev](https://brev.nvidia.com/)

1. Click the **Launch on Brev** button above (or the badge at the top of this README).
2. Sign in or create a free NVIDIA Brev account.
3. Select a GPU instance — an NVIDIA T4 or L4 is sufficient for all five labs.
4. Click **Deploy**. The environment will be ready in ~2 minutes with CUDA,
   Python, and all dependencies pre-installed.
5. Open JupyterLab from the Brev console and navigate to the `notebooks/` directory.

#### 2. Clone and run locally

```bash
git clone https://github.com/NVDLI/fundamentals_of_deep_learning.git
cd course_content
```

**Prerequisites:** Python 3.9+, an NVIDIA GPU with CUDA 11.8+ (CPU-only works
but is slow for later notebooks), and conda or pip.

```bash
pip install -r environment/requirements.txt
jupyter lab
```

Then open <http://localhost:8888> in your browser and navigate to the
`tutorials/` directory.

#### 3. Run with Docker

To deploy the content with the provided `Dockerfile`, run:

```bash
docker build -t fdl-app . && docker run -d -p 8888:8888 --name fdl-container fdl-app
```

Then open <http://localhost:8888> in your browser and navigate to the
`tutorials/` directory.

## Contributing

We welcome contributions from the community. To contribute:

1. Fork this repository and create a feature branch:
   ```bash
   git checkout -b feature/your-improvement
   ```
2. Make your changes. Ensure notebooks are cleared of all output before committing.
3. Open a Pull Request with a clear description of what changed and why.

For significant changes or new notebooks, please open an issue first to discuss.
Please do not commit datasets or large binary files — use download scripts instead.

See [CONTRIBUTING](CONTRIBUTING.md) for full guidelines.

## License

This project is licensed under [Creative Commons 4.0](LICENSE).
