# Installation

## Install with pip

```bash
pip install {{cookiecutter.project_name}}
```

## Install from source

```bash
pip install "git+https://github.com/karthikrangasai/{{cookiecutter.project_name}}.git@master#egg={{cookiecutter.project_name}}"
```

## Installation directions for contributors

**NOTE:** Please install ``{{cookiecutter.project_name}}`` with packages for testing and building docs.

- Fork the [repository](https://github.com/karthikrangasai/{{cookiecutter.project_name}}.git).
- Clone it locally

    ```bash
    git clone https://github.com/[your-username]/{{cookiecutter.project_name}}.git
    ```

- Change the working directory

    ```bash
    cd {{cookiecutter.project_name}}
    ```

- Install ``{{cookiecutter.project_name}}`` in editable mode with all extra packages for development

    ```bash
    poetry install --all-extras
    ```
