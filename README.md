# Python DevOps Course
Python DevOps course material that I created for the coding club of TSP ([Club Code](https://discord.gg/zTcwSUUZsS)). 

## Installation
Install a virtual environment:
```shell
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

Create a gitignore, you can use a plugin of your IDE, download one, or create one by yourself.
```shell
curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -o .gitignore
```

## Create the requirements.txt file
It can simply be achieved with pip:
```shell
pip freeze > requirements.txt
```

> :warning: pyproject.toml has to be updated!

You can use a script to update pyproject.toml:
```shell
python update_pyproject.py 
```

## Structure
The structure can be obtained with `tree --gitignore -a --matchdirs -I .git`.
```console
├── .gitignore
├── main.py
└── README.md
```
