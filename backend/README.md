## Contributing
See [Contributing Guidelines](https://cbg-ethz.github.io/PYggdrasil/contributing/).
### Setting up the repository

To build the package and maintain dependencies we use [Poetry](https://python-poetry.org/).
In particular, it's good to install it and become familiar with its basic functionalities by reading the documentation. 

To set up the environment (together with development tools) run:
```bash
$ poetry install --with dev
$ poetry run pre-commit install
```

Then, you will be able to run tests:
```bash
$ poetry run pytest
```
... or check the types:
```bash
$ poetry run pyright
```

Alternatively, you may prefer to work with the right Python environment using:
```bash
$ poetry shell
$ pytest
```

### Existing code quality checks
The code quality checks run during on GitHub can be seen in ``.github/workflows/test.yml``.

We are using:

  * [Ruff](https://github.com/charliermarsh/ruff) to lint the code.
  * [Black](https://github.com/psf/black) to format the code.
  * [Pyright](https://github.com/microsoft/pyright) to check the types.
  * [Pytest](https://docs.pytest.org/) to run the unit tests.
  * [Interrogate](https://interrogate.readthedocs.io/) to check the documentation.


### Workflow

We use [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow),
in which modifications of the code should happen via small pull requests.