# GermanNLP

This repository contains a Python project for Natural Language Processing.

## How To Setup Python

The project was developed with Python Version 3.7.9 which can be found here:
<https://www.python.org/downloads/release/python-379/>

The required modules for this project can be installed with pip, by using the following command:

```code
pip install -r requirements.txt
```

For using Tensorflow 2.4.0 CUDA 11.0 is required, which can be found here:
<https://developer.nvidia.com/cuda-toolkit-archive>

The cuDNN 8.0.5 Installation Guide can be found here:
<https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html>

---

### NOTE

* After installing everything you can check your Setup by executing "tests/test_tensorflow.py"
* Multiple Installations of different CUDA-Versions can cause the error "ImportError: DLL load failed" while importing tensorflow.

---

## Dataset

The dataset for this project is the "german-speechdata-package-v2", which can be found here:
<http://www.repository.voxforge1.org/downloads/de/>
