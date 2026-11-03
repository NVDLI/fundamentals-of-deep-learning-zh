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

---

## 7. Copyright and license notices for third-party software

This section follows the NVIDIA OSS notices-file format: one entry per
third-party software component listed in Sections 1 and 2.1, giving the
copyright holder, the license, a link to the license text, and the copyright
statement as published in the component's own license or notice file. The
copyright statements below are reproduced from each project's upstream
`LICENSE`/`NOTICE` file (at the pinned release tag where one exists). The full
license texts are linked; Apache-2.0 and CC-BY-4.0 are also in `LICENSES/`.

### Python packages declared by this repository (Section 1)

**Copyright Amazon.com, Inc. - Apache-2.0 License** (boto3 1.34.104)
License Text (https://spdx.org/licenses/Apache-2.0.html)

    boto3
    Copyright 2013-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

**Copyright The HuggingFace Datasets Authors - Apache-2.0 License** (datasets 5.0.0)
License Text (https://spdx.org/licenses/Apache-2.0.html)

    Copyright 2020 The HuggingFace Datasets Authors and the TensorFlow Datasets Authors.

**Copyright The HuggingFace Inc. team - Apache-2.0 License** (huggingface_hub 1.21.0)
License Text (https://spdx.org/licenses/Apache-2.0.html)

    Copyright 2019-present, the HuggingFace Inc. team.

**Copyright Project Jupyter Contributors - BSD 3-clause License** (ipywidgets 8.1.2)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) 2015 Project Jupyter Contributors
    All rights reserved.

**Copyright Project Jupyter Contributors - BSD 3-clause License** (jupyterlab 4.2.0)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) 2015-2022 Project Jupyter Contributors
    All rights reserved.

**Copyright Kaggle Inc - Apache-2.0 License** (kagglehub 1.0.2)
License Text (https://spdx.org/licenses/Apache-2.0.html)

    Copyright 2018 Kaggle Inc

**Copyright Matplotlib Development Team - Matplotlib License (PSF-based)** (matplotlib 3.8.4)
License Text (https://matplotlib.org/stable/project/license.html)

    Copyright (c) 2012- Matplotlib Development Team; All Rights Reserved
    Copyright (c) 2002-2011 John D. Hunter; All Rights Reserved

**Copyright AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team - BSD 3-clause License** (pandas 2.3.3)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
    All rights reserved.
    Copyright (c) 2011-2023, Open source contributors.

**Copyright Matthew Barnett; Secret Labs AB - Apache-2.0 and CNRI-Python Licenses** (regex 2026.6.28)
License Text (https://spdx.org/licenses/Apache-2.0.html, https://spdx.org/licenses/CNRI-Python.html)

    This work was derived from the 're' module of CPython 2.6 and CPython 3.1,
    copyright (c) 1998-2001 by Secret Labs AB and licensed under CNRI's Python 1.6
    license.
    All additions and alterations are licensed under the Apache 2.0 License.
    Copyright 2020 Matthew Barnett

**Copyright Kenneth Reitz - Apache-2.0 License** (requests 2.32.2)
License Text (https://spdx.org/licenses/Apache-2.0.html)

    Requests
    Copyright 2019 Kenneth Reitz

**Copyright alvations - MIT License** (sacremoses 0.1.1)
License Text (https://spdx.org/licenses/MIT.html)

    Copyright (c) 2020 alvations

**Copyright Google Inc. - Apache-2.0 License** (sentencepiece 0.2.1)
License Text (https://spdx.org/licenses/Apache-2.0.html)

    Copyright 2016 Google Inc.

**Copyright PyTables maintainers - BSD 3-clause License** (tables 3.9.2)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) 2002-2004 by Francesc Alted
    Copyright (c) 2005-2007 by Carabos Coop. V.
    Copyright (c) 2008-2010 by Francesc Alted
    Copyright (c) 2011-2021 by PyTables maintainers
    All rights reserved.

**Copyright nteract - BSD 3-clause License** (testbook 0.4.2)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) 2020, nteract
    All rights reserved.

**Copyright Casper da Costa-Luis, Google Inc., Noam Yorav-Raphael - MPL-2.0 and MIT Licenses** (tqdm 4.66.3)
License Text (https://spdx.org/licenses/MPL-2.0.html, https://spdx.org/licenses/MIT.html)

    MPL-2.0 2015-2024 (c) Casper da Costa-Luis
    MIT 2016 (c) [PR #96] on behalf of Google Inc.
    MIT 2013 (c) Noam Yorav-Raphael, original author.
    Copyright (c) 2013 noamraph

**Copyright The Hugging Face team - Apache-2.0 License** (transformers 5.12.1)
License Text (https://spdx.org/licenses/Apache-2.0.html)

    Copyright 2018- The Hugging Face team. All rights reserved.

**Copyright IPython Development Team - BSD 3-clause License** (IPython, installed as a dependency of jupyterlab and ipywidgets)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) 2008-Present, IPython Development Team
    Copyright (c) 2001-2007, Fernando Perez <fernando.perez@colorado.edu>
    Copyright (c) 2001, Janko Hauser <jhauser@zscout.de>
    Copyright (c) 2001, Nathaniel Gray <n8gray@caltech.edu>
    All rights reserved.

### Packages supplied by the default base image (Section 2.1)

These are not installed or pinned by this repository; they are listed because
the course code imports them directly.

**Copyright Facebook, Inc. and contributors - BSD 3-clause License** (torch / PyTorch 2.4.1)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) 2016-     Facebook, Inc            (Adam Paszke)
    Copyright (c) 2014-     Facebook, Inc            (Soumith Chintala)
    Copyright (c) 2011-2014 Idiap Research Institute (Ronan Collobert)
    Copyright (c) 2012-2014 Deepmind Technologies    (Koray Kavukcuoglu)
    Copyright (c) 2011-2012 NEC Laboratories America (Koray Kavukcuoglu)
    Copyright (c) 2011-2013 NYU                      (Clement Farabet)
    Copyright (c) 2006-2010 NEC Laboratories America (Ronan Collobert, Leon Bottou, Iain Melvin, Jason Weston)
    Copyright (c) 2006      Idiap Research Institute (Samy Bengio)
    (see the PyTorch LICENSE file for the complete list of contributors)

**Copyright Soumith Chintala - BSD 3-clause License** (torchvision 0.19.1)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) Soumith Chintala 2016,
    All rights reserved.

**Copyright NumPy Developers - BSD 3-clause License** (numpy)
License Text (https://spdx.org/licenses/BSD-3-Clause.html)

    Copyright (c) 2005-2026, NumPy Developers.
    All rights reserved.

**Copyright Secret Labs AB, Fredrik Lundh, Jeffrey A. Clark and contributors - HPND / MIT-CMU License** (Pillow)
License Text (https://spdx.org/licenses/HPND.html, https://spdx.org/licenses/MIT-CMU.html)

    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh and contributors
    Copyright © 2010 by Jeffrey 'Alex' Clark and contributors

**Copyright Python Software Foundation - PSF-2.0 License** (Python / CPython)
License Text (https://spdx.org/licenses/PSF-2.0.html)

    Copyright (c) 2001 Python Software Foundation; All Rights Reserved
    (and subsequent years; see the CPython LICENSE file)

The NVIDIA CUDA and cuDNN runtime libraries in the default base image are
NVIDIA components and are subject to NVIDIA's license terms. The DGX Spark
base image (`nvcr.io/nvidia/pytorch:25.10-py3`, Section 2.2) ships its own
license and third-party notices inside the container.
