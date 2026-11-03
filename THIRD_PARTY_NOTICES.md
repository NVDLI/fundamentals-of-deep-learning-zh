# Third-Party Notices

This file lists the third-party software, base images, data, and media that
this project depends on or includes, together with their licenses. NVIDIA's own
material is licensed as described in [LICENSE](LICENSE). The third-party
material listed here is not relicensed by NVIDIA and remains under its own
license.

## Release scope

NVIDIA distributes this project as source only, through this repository:
Jupyter notebooks, helper scripts, slide decks, images, and the Dockerfile
(`course_content/Dockerfile`, plus the Dockerfile instructions in
`DGX_SPARK.md`). NVIDIA does not build or publish container images for this
project and does not provide a hosted environment for it (for example, an
NVIDIA-hosted Brev Launchable).

The packages, base images, data, and models in Sections 1–4 are not included
in this repository. Users obtain them directly from their upstream sources
(PyPI, Docker Hub, NVIDIA NGC, the Ubuntu archive, Hugging Face, Kaggle, and
download.pytorch.org) when they build or run the course environment, under the
licenses shown below. Each package ships with its own full license text; binary
wheels of some packages also bundle native libraries under additional licenses
(see each package's license files).

---

## 1. Python packages declared by this repository

Installed by `course_content/Dockerfile`, either from
`course_content/environment/requirements.txt` or by the Dockerfile's explicit
`pip install` steps.

| Package | Version | License | Declared in | Source |
|---------|---------|---------|-------------|--------|
| boto3 | 1.34.104 | Apache-2.0 | requirements.txt | https://github.com/boto/boto3 |
| datasets | 5.0.0 | Apache-2.0 | requirements.txt | https://github.com/huggingface/datasets |
| huggingface_hub | 1.21.0 | Apache-2.0 | requirements.txt | https://github.com/huggingface/huggingface_hub |
| ipywidgets | 8.1.2 | BSD-3-Clause | Dockerfile | https://github.com/jupyter-widgets/ipywidgets |
| jupyterlab | 4.2.0 | BSD-3-Clause | Dockerfile | https://github.com/jupyterlab/jupyterlab |
| kagglehub | 1.0.2 | Apache-2.0 | requirements.txt | https://github.com/Kaggle/kagglehub |
| matplotlib | 3.8.4 | Matplotlib License (PSF-based) | requirements.txt | https://github.com/matplotlib/matplotlib |
| pandas | 2.3.3 | BSD-3-Clause | requirements.txt | https://github.com/pandas-dev/pandas |
| regex | 2026.6.28 | Apache-2.0 AND CNRI-Python | requirements.txt | https://github.com/mrabarnett/mrab-regex |
| requests | 2.32.2 | Apache-2.0 | requirements.txt | https://github.com/psf/requests |
| sacremoses | 0.1.1 | MIT | requirements.txt | https://github.com/alvations/sacremoses |
| sentencepiece | 0.2.1 | Apache-2.0 | requirements.txt | https://github.com/google/sentencepiece |
| tables | 3.9.2 | BSD-3-Clause | requirements.txt | https://github.com/PyTables/PyTables |
| testbook | 0.4.2 | BSD-3-Clause | requirements.txt | https://github.com/nteract/testbook |
| tqdm | 4.66.3 | MPL-2.0 AND MIT | requirements.txt | https://github.com/tqdm/tqdm |
| transformers | 5.12.1 | Apache-2.0 | requirements.txt | https://github.com/huggingface/transformers |

`IPython` (BSD-3-Clause, https://github.com/ipython/ipython), which every
notebook imports, is installed as a dependency of `jupyterlab` (through
`ipykernel`) and of `ipywidgets`; it may also be present in the base image.

---

## 2. Packages supplied by the base images (not installed or pinned by this repository)

### 2.1 Default build: `course_content/Dockerfile`

Base image: `pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime`, published on
Docker Hub by the PyTorch project (it is not an NVIDIA NGC container). Users
pull it directly from Docker Hub; NVIDIA does not redistribute it.

| Package | Version | License | Used by |
|---------|---------|---------|---------|
| torch (PyTorch) | 2.4.1 (from the image tag) | BSD-3-Clause | notebooks 01–06, `utils.py`, `data/data.py` |
| torchvision | 0.19.1 (companion release of torch 2.4.1) | BSD-3-Clause | notebooks 01, 04a, 04b, 05a, 05b |
| numpy | provided by the base image (not pinned by this repository) | BSD-3-Clause | notebook 05a, `utils.py`, `data/data.py` |
| Pillow (PIL) | provided by the base image (not pinned by this repository) | HPND (Pillow 10.x and earlier) / MIT-CMU (Pillow 11.0 and later) | notebook 05b |
| Python (CPython) | provided by the base image | PSF-2.0 | runtime |

The base image also contains NVIDIA CUDA 11.8 and cuDNN 9 runtime libraries,
which are subject to NVIDIA's license terms for those components, and Ubuntu
and conda packages under their own licenses.

### 2.2 DGX Spark build described in `DGX_SPARK.md`

Base image: `nvcr.io/nvidia/pytorch:25.10-py3` from NVIDIA NGC, provided under
the NVIDIA Deep Learning Container License; the container includes its own
license and third-party notices. Users pull it directly from NGC. According to
the NGC release notes it supplies Ubuntu 24.04, Python 3.12, CUDA 13.0.2,
PyTorch 2.9.0a0+145a3a7bda, and JupyterLab 4.3.6, together with torchvision,
numpy, Pillow, and IPython. The documented build installs
`course_content/environment/requirements.txt` on top and constrains numpy to
`numpy<2`.

---

## 3. System packages installed by `course_content/Dockerfile` (apt)

Installed from the Ubuntu archive when the image is built. The full license
statement for each package is in `/usr/share/doc/<package>/copyright` inside
the built image.

| Package | License | Purpose |
|---------|---------|---------|
| libjpeg-turbo8 | IJG AND BSD-3-Clause AND Zlib | JPEG codec library |
| libpng16-16 | libpng-2.0 | PNG codec library |
| git | GPL-2.0-only | Version-control command-line tool |
| gcc | GPL-3.0-or-later (runtime libraries under the GCC Runtime Library Exception) | C compiler tool |

These are standalone programs or system libraries loaded by third-party
packages; NVIDIA code does not link against them.

---

## 4. Data and pretrained models downloaded at runtime

The notebooks download the following when they run. None of them is included
in this repository.

| Item | Used in | Source | License / terms |
|------|---------|--------|-----------------|
| MNIST handwritten digits | 01_mnist (`torchvision.datasets.MNIST`) | http://yann.lecun.com/exdb/mnist/ | See the dataset page (commonly cited as CC BY-SA 3.0) |
| ASL-HG dataset | 02_asl, 03_asl_cnn, 04a_asl_augmentation (`data/data.py`) | https://huggingface.co/datasets/juanjodurillo/asl-hg (record: https://doi.org/10.17632/j4y5w2c8w9.1) | CC-BY-4.0 |
| Penny the Corgi dataset | 05b_corgi_door (`kagglehub`) | https://www.kaggle.com/datasets/danielledetering/penny-the-corgi | CC-BY-4.0 |
| VGG16 ImageNet weights (`VGG16_Weights.DEFAULT`) | 05a_doggy_door, 05b_corgi_door (torchvision) | https://download.pytorch.org/models/ | See the torchvision model documentation |
| bert-base-cased | 06_nlp (transformers) | https://huggingface.co/google-bert/bert-base-cased | Apache-2.0 |
| bert-large-uncased-whole-word-masking-finetuned-squad | 06_nlp (transformers) | https://huggingface.co/google-bert/bert-large-uncased-whole-word-masking-finetuned-squad | Apache-2.0 |

---

## 5. Microsoft 365 premium creative content in the slide decks

The slide decks in `course_content/slides/` contain stock images and icons
from the Microsoft 365 premium creative content library. These Microsoft
assets are not licensed under this project's open source licenses. They are
included only inside the PowerPoint files, under Microsoft's terms for premium
creative content:

https://support.microsoft.com/en-us/office/foundations-experiences/what-am-i-allowed-to-use-premium-creative-content-for

Recipients may not extract, reuse, sublicense, or redistribute these assets
separately, including under this project's open source licenses. Any use of
them outside the slide decks, or outside a PDF exported from them, must be
separately permitted by Microsoft. Slide 2 of each deck repeats this notice.

| File | Slides (as numbered in PowerPoint) | Microsoft assets |
|------|------------------------------------|------------------|
| `course_content/slides/part1.pptx` | 11, 14, 15, 16, 17, 18, 20, 21, 31, 32, 33, 34, 36, 38 | Stock photos (circuit board, kitten in a meadow, yellow vintage car, breaking wave, child with astronaut drawing, graph, photographer, stacked hands) and icons |
| `course_content/slides/part2.pptx` | 25, 29, 31 | Icons (linear graph, periodic graph) and an illustration (connecting lines and dots) |
| `course_content/slides/part3.pptx` | 7, 8 | Icons (water drop, dim sun, sunglasses) |
| `course_content/slides/part4.pptx` | 6, 13 | Icons (wolf, puppies, camera) |
| `course_content/slides/part5.pptx` | 6, 10, 12, 13, 14, 16 | Stock photos (desk with technical drawings, tiger on a rock, brain scan, snowflake) and icons (checkmark, close, scissors) |
| `course_content/slides/part6.pptx` | 6, 7, 8, 13, 16, 29, 33, 38 | Stock photos (kitten, alpacas, giraffes, puffins, falcon, rocket launch) and icons |

No Microsoft 365 premium creative content is used in the notebooks or in the
image files under `course_content/tutorials/`.

---

## 6. Third-party media included in this repository

### ASL-HG images

Files:

- `course_content/tutorials/images/A.jpg`
- `course_content/tutorials/images/B.jpg`

Source: ASL-HG: American Sign Language Hand Gesture Image Dataset

Creators: Md. Famidul Islam Pranto, Md. Rifatul Islam, Md. Ali Akbor,
Nabonita Ghosh, Md. Rahatun Alam, Sudipto Chaki, and Md Masudul Islam.

- Dataset copy: https://huggingface.co/datasets/juanjodurillo/asl-hg
- Canonical record: https://doi.org/10.17632/j4y5w2c8w9.1
- License: Creative Commons Attribution 4.0 International (`LICENSES/CC-BY-4.0.txt`)
- Modifications: Images were selected and prepared for course presentation.

### ASL alphabet (public domain)

File: `course_content/tutorials/images/asl.png`

- Creator: Ds13 (Darren Stone)
- Source: https://commons.wikimedia.org/wiki/File:Asl_alphabet_gallaudet.png
- Status: Released into the public domain by the creator; see
  `LICENSES/LicenseRef-Public-Domain.txt`
- Modifications: Original file renamed to `asl.png`; image content was not modified

### Jack Russell Terrier photograph

File: `course_content/tutorials/data/doggy_door_images/happy_dog.jpg`

- Photographer: Plank
- Photographer profile: https://commons.wikimedia.org/wiki/User:Plank
- Source: https://commons.wikimedia.org/wiki/File:Jack_Russell_Terrier_1.jpg
- License: Creative Commons Attribution 3.0 Unported (`LICENSES/CC-BY-3.0.txt`)
- License URL: https://creativecommons.org/licenses/by/3.0/
- Modification: Resized for course use

### MNIST figure

File: `course_content/tutorials/images/mnist1.png`

`mnist1.png` is an NVIDIA-created selection and arrangement of samples
from the MNIST Database of Handwritten Digits.

- MNIST authors: Yann LeCun, Corinna Cortes, and Christopher J. C. Burges
- Dataset source: http://yann.lecun.com/exdb/mnist/
- Retrieval method: `torchvision.datasets.MNIST`
- Modification: NVIDIA selected and arranged samples into one educational figure.

CC BY 4.0 covers NVIDIA's selection, arrangement, and presentation.

### Penny and brown_bear within the Corgi dataset

Files:

- `course_content/tutorials/images/Penny.jpg`
- `course_content/tutorials/data/doggy_door_images/brown_bear.jpg`

- Creator/licensor: Danielle Detering
- Source: https://www.kaggle.com/datasets/danielledetering/penny-the-corgi
- License: Creative Commons Attribution 4.0 International (`LICENSES/CC-BY-4.0.txt`)
- License URL: https://creativecommons.org/licenses/by/4.0/
- Modifications: Selected and incorporated into the course materials.

### Sleepy cat photograph

File:

- `course_content/tutorials/data/doggy_door_images/sleepy_cat.jpg`

- Creator/licensor: Vadim Kudlay (NVIDIA employee)
- Copyright: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
- Source: Original photograph taken by Vadim Kudlay and supplied with authorization for distribution under CC BY 4.0.
- License: Creative Commons Attribution 4.0 International (`LICENSES/CC-BY-4.0.txt`)
- License URL: https://creativecommons.org/licenses/by/4.0/
- Modifications: Incorporated into the course materials.
