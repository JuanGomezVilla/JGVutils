# JGVutils

[![FlangerJS](https://img.shields.io/badge/version-v1.0.2.0-blue.svg)](https://flangerjs.org)

Useful utils to use in Python with standard libraries

## 1. Setup

1. Instalar la librería de _pandas_:
    ```bash
    pip install pandas
    ```
2. Instalar o actualizar _setuptools_:
    ```bash
    python -m pip install --user --upgrade setuptools
    ```
3. Acceder a la carpeta con el código:
    ```bash
    cd src
    ```
4. Crear un setup para cargarlo:
    ```bash
    python setup.py sdist
    ```
5. Instalar _twine_:
    ```bash
    pip install twine
    ```
6. Para cargar el resultado:
    ```bash
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    ```

## 2. Instalación

- Para pruebas:
    ```bash
    pip install -i https://test.pypi.org/simple/ JGVutils
    ```
- Código oficial:
    ```bash
    pip install JGVutils
    ```