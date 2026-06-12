# Fundamentals of Deep Learning

[![Launch on Brev](https://img.shields.io/badge/Launch%20on-Brev-76B900)](https://brev.nvidia.com/) [![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)

The Fundamentals of Deep Learning is an open-source, hands-on course repository
from the NVIDIA Deep Learning Institute (DLI) that introduces neural networks,
convolutional architectures, and transfer learning through interactive Jupyter
notebooks and real-world datasets.

Inspired by literate programming, maintained by NVIDIA DLI, and launchable in
one click via NVIDIA Brev, this repository contains:

- **README, CODE_OF_CONDUCT, CONTRIBUTING templates** — README files inform
  anyone about the first steps to use, learn, and contribute to the project.
- **CITATION.cff** — Citing this work aligns with best practices for
  reproducible research. Adhering to established standards for documenting
  project dependencies demonstrates our commitment to quality, transparency,
  and integrity.
- **LICENSE** — This repository is licensed under the Apache 2.0 License. Please
  review the license before using, distributing, or contributing. The full DLI
  course (dedicated GPU access, auto-graded assessments, certificate of
  completion) is available at nvidia.com/dli under separate terms.
- **notebooks/** — Placeholder for final notebooks: Five hands-on Jupyter
  notebooks covering neural networks, CNNs, data augmentation, and transfer
  learning. Notebooks can be added to `docs/_toc.yml` to compose the project
  documentation.

  | # | Notebook | Topics |
  |---|----------|--------|
  | 01 | `01_mnist.ipynb` | Intro to neural networks, MNIST handwritten digits |
  | 02 | `02_asl.ipynb` | CNNs for image classification, American Sign Language dataset |
  | 03 | `03_asl_cnn.ipynb` | Data augmentation, model improvement |
  | 04 | `04_transfer_learning.ipynb` | Pre-trained models, transfer learning with ImageNet |
  | 05 | `05_assessment.ipynb` | Final project: train a fresh food classifier |

- **data/** — Placeholder folder for datasets. Data is immutable. By default,
  the data folder is present but ignored from version control to prevent large
  files from being mistakenly versioned. Datasets are downloaded automatically
  on first run.
- **environment.yml and requirements.txt** — Dependency specifications for
  Conda and pip. It is recommended the project be used in a dedicated virtual
  environment.
- **setup.sh** — Optional bash setup script used by the Brev Launchable for
  VM-mode environment configuration — installs dependencies, configures
  Jupyter, and prepares the workspace automatically.
- **.pre-commit-config.yml** — Using pre-commit enforces code standards and
  catches errors before commits reach the review stage. Checks include notebook
  output clearing, syntax validation, and formatting compliance.
- **GitHub Actions and Dependabot** — Automated workflows validate notebooks,
  build documentation, and publish to GitHub Pages on every push to main.
  Dependabot keeps dependencies up to date and flags security vulnerabilities.
- **GitHub Issues and Pull Request Templates** — Custom templates guide
  contributors when filing bugs, requesting features, or submitting changes —
  encouraging consistency and maintainability.

Full course available at: nvidia.com/dli — includes dedicated GPU resources,
auto-graded assessments, and a certificate upon completion.

## Learning Outcomes

By completing these labs, you will be able to:

- Build and train neural networks using PyTorch on real image datasets
- Apply convolutional neural networks (CNNs) to image classification tasks
- Use data augmentation and transfer learning to improve accuracy on limited data
- Manage the bias-variance tradeoff and apply techniques to address overfitting
- Deploy a trained model to make predictions on new, unseen data

## Usage

### Getting Started

#### 1. Launch with Brev (Recommended)

The fastest path to a running environment — no local setup required.

🌟 [Launch this course on NVIDIA Brev](https://brev.nvidia.com/)

1. Click the **Launch on Brev** button above (or the badge at the top of this README).
2. Sign in or create a free NVIDIA Brev account.
3. Select a GPU instance — an NVIDIA T4 or L4 is sufficient for all five labs.
4. Click **Deploy**. Your environment will be ready in ~2 minutes with CUDA,
   Python, and all dependencies pre-installed.
5. Open JupyterLab from the Brev console and navigate to the `notebooks/` directory.

To create or share your own Launchable from this repository, see the Brev
Launchables documentation.

#### 2. Clone and run locally

```bash
git clone https://gitlab-master.nvidia.com/dli/expand-the-funnel/fundamentals-of-deep-learning.git
cd fundamentals-of-deep-learning
```

**Prerequisites:** Python 3.9+, an NVIDIA GPU with CUDA 11.8+ (CPU-only works
but is slow for later notebooks), and conda or pip.

**With Conda (recommended):**

```bash
conda env create -f environment.yml
conda activate dli-fdl
jupyter lab
```

**With pip:**

```bash
pip install -r requirements.txt
jupyter lab
```

Then open <http://localhost:8888> in your browser and navigate to the
`notebooks/` directory.

#### 3. Run with Docker

A pre-built container with all dependencies is available on NGC:

```bash
docker run --gpus all -p 8888:8888 \
  nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.6.1 \
  jupyter lab --ip=0.0.0.0 --allow-root --no-browser
```

#### 4. Review and update notebook content

The repository comes with five lab notebooks that should be run in order.
Please ensure notebooks are cleared of all output before committing
(Kernel > Restart & Clear Output). Notebooks can be added to `docs/_toc.yml` to
publish them as a Jupyter Book documentation site.

#### 5. Enable GitHub Actions and GitHub Pages

After forking or cloning, enable GitHub Actions to automatically build and
publish the Jupyter Book documentation:

1. Go to **Settings > Actions > General** and select read and write permissions.
2. Go to **Settings > Pages** and select Deploy from GitHub Actions.

On the next push to main, the documentation will be built and published
automatically. Check progress under the Actions tab.

> ⚠️ If publishing from a private fork, review your content carefully and follow
> your organization's data privacy policy before enabling public Pages.

Congratulations! Once set up, your project documentation will be live at:

🌟 <https://fdl-test-d701be.gitlab-master-pages.nvidia.com/>

## Add Content

### Updating the Jupyter Book `_config.yml` metadata

Update `docs/_config.yml` to reflect your fork's details:

```yaml
title: Fundamentals of Deep Learning
author: <your-team>
repository:
  url: https://gitlab-master.nvidia.com/dli/expand-the-funnel/fundamentals-of-deep-learning
  branch: main
execute:
  execute_notebooks: "auto"
```

### Update the table of contents

Edit `docs/_toc.yml` to control which notebooks appear in the published documentation:

```yaml
format: jb-book
root: README
parts:
  - caption: Labs
    numbered: True
    chapters:
      - file: notebooks/01_mnist.ipynb
      - file: notebooks/02_asl.ipynb
      - file: notebooks/03_asl_cnn.ipynb
      - file: notebooks/04_transfer_learning.ipynb
      - file: notebooks/05_assessment.ipynb
```

See Jupyter Book: Structure and organize content for further options.

### Building documentation locally

Install documentation dependencies and build locally:

```bash
pip install -e .[docs]
jupyter-book build . --config docs/_config.yml --toc docs/_toc.yml
```

The generated site will be in `_build/html/`. Open `index.html` in a browser to preview.

## Python Package Management

If extending this project as a Python package, include a `pyproject.toml` for
standardized dependency management:

```toml
[build-system]
requires = ["hatchling>=1.21.0", "hatch-vcs>=0.3.0"]
build-backend = "hatchling.build"

[project]
name = "dli-fundamentals-of-deep-learning"
description = "NVIDIA DLI Fundamentals of Deep Learning — open-source lab notebooks"
readme = { file = "README.md", content-type = "text/markdown" }
license = { file = "LICENSE" }
authors = [ { name = "NVIDIA DLI", email = "dli@nvidia.com" } ]
dynamic = ["version"]

[project.optional-dependencies]
docs = [ "jupyter-book>=1,<2" ]
```

Install from the repository directly:

```bash
pip install git+https://gitlab-master.nvidia.com/dli/expand-the-funnel/fundamentals-of-deep-learning.git
```

See Packaging Python Projects for more.

## Contributing

We welcome contributions from the community. To contribute:

1. Fork this repository and create a feature branch:
   ```bash
   git checkout -b feature/your-improvement
   ```
2. Make your changes. Ensure notebooks are cleared of all output before committing.
3. Test your changes in a clean environment using `environment.yml`.
4. Open a Pull Request with a clear description of what changed and why.

For significant changes or new notebooks, please open an issue first to discuss.
Do not commit datasets or large binary files — use download scripts instead.

See [CONTRIBUTING](CONTRIBUTING.md) for full guidelines.

## Code of Conduct

This repository maintains a Code of Conduct to ensure an inclusive and
respectful environment for everyone. Please adhere to it in all interactions
within our community.

## License

This project is licensed under the Apache License 2.0.
