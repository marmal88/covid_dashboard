
## Description


### 1.1 Setting up python version and creating virtual environment
**Create Python Environment**
To create the correct python version use the command, If done correctly the `.python-version` file containing the python version should be created:

```bash
# Check if you have the python version installed on your computer
pyenv versions | grep 3.11.4

# If version does not exists, then search for version using command:
pyenv install -l
# and install using command:
pyenv install 3.11.4

# Once installed check which version is currently being activated using command:
pyenv versions
# To activate the version locally use command:
pyenv local 3.11.4

# Check again if right python version has been installed
python -V
```

### 1.2 Setting up Poetry

Initialize poetry environment and define settings to create venv in repo

```bash
# initialize poetry environment
poetry init
# configure poetry to create venv in project
poetry config virtualenvs.in-project true
```
Activating poetry environment

```bash
# actvate poetry environment
poetry shell
```

Misc: Updating, adding and removing dependencies. 

```bash
# adding new packages
poetry add pandas
poetry add -G dev pre-commit
# update poetry dependecies
poetry update
```