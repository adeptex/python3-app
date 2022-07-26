# {{ cookiecutter.project_slug }}

![](coverage.svg)

Python3 app **{{ cookiecutter.project_slug }}**


## Installation

```bash
make install
```

## Usage

### CLI
```bash
{{ cookiecutter.project_slug }} -h
```

### Module
```py
import {{ cookiecutter.project_slug }}
for item in {{ cookiecutter.project_slug }}.run("-c config.yml"):
    print(item)
```

## Development

```bash
make install-dev
make test
```
