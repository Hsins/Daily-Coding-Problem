<!-- Badge for License -->
<div align="right">

  [![wemake-python-styleguide](https://img.shields.io/badge/style-WeMake-000000.svg?style=flat-square)](https://github.com/wemake-services/wemake-python-styleguide)
  [![](https://img.shields.io/github/license/Hsins/Daily-Coding-Problem.svg?style=flat-square)](./LICENSE)

</div>

<!-- Logo -->
<p align="center">
  <img src="https://i.imgur.com/BMV51Qj.png" alt="Daily Coding Problem" height="150px">
</p>


<!-- Title and Description -->
<div align="center">

# Daily Coding Problem

🗓️ _Solutions to the problems from [Daily Coding Problem](https://www.dailycodingproblem.com/). You can subscribe to that service and then it will send a coding task to you every day for practicing and enhancing your problem-solving ability._

<!-- Badges -->
[![](https://img.shields.io/badge/Python-3.8-blue?logo=python&style=flat-square)](https://www.python.org/)
[![](https://img.shields.io/codecov/c/github/Hsins/Daily-Coding-Problem?logo=codecov&style=flat-square&token=ZGFXPJ4N6U)](https://codecov.io/gh/Hsins/Daily-Coding-Problem)
[![CodeFactor](https://www.codefactor.io/repository/github/hsins/daily-coding-problem/badge?style=flat-square)](https://www.codefactor.io/repository/github/hsins/Daily-Coding-Problem)
[![README in Traditional Chinese](https://img.shields.io/badge/README-繁體中文-8CA1AF.svg?logo=read-the-docs&style=flat-square)](./README_zh-TW.md)  
[![](https://img.shields.io/badge/Easy-29-34ED43.svg?logo=&style=flat-square)]()
[![](https://img.shields.io/badge/Medium-33-51ADEF.svg?logo=&style=flat-square)]()
[![](https://img.shields.io/badge/Hard-25-EF5151.svg?logo=&style=flat-square)]()

</div>

## Features

- Follow this [article](https://wkrzywiec.medium.com/how-to-write-good-quality-python-code-with-github-actions-2f635a2ab09a) to set up the integration with CodeFactor, Linter and Unit Testing running with GitHub Actions.

## Branches

There are a three branches for difference usage here:

- [`main`](https://github.com/Hsins/Daily-Coding-Problem/tree/main) hold all the solutions and testings.
- [`docs`](https://github.com/Hsins/Daily-Coding-Problem/tree/docs) store the resource code of solution manual [site](https://dcp.hsins.me/).
- [`gh-pages`](https://github.com/Hsins/Daily-Coding-Problem/tree/gh-pages) host the website pages published by GitHub Actions (check the [workflow file](https://github.com/Hsins/Daily-Coding-Problem/blob/docs/.github/workflows/site-deployment.yml)).

## Structures

The folder structure shown below keeps the concepts of the supporting common layouts from [Good Integration Practices](https://docs.pytest.org/en/stable/goodpractices.html).

```
.
├── solutions
│   ├── day_001
│   │   ├── solution01.py
│   │   ├── ...
│   │   └── README.md
│   └── ...
├── test
│   ├── __init__.py
│   ├── test_day_001.py
│   └── ...
├── ...
├── README.md
├── README_zh-TW.md
└── LICENSE
```

## Instructions

### Practice Problems

If you want to practice and enhance your problem-solving ability with the project but don't know how to run testings and check format. Follow the steps:

```bash
# clone the project and install dependencies
$ git clone https://github.com/Hsins/Daily-Coding-Problem.git
$ pip install -r requirements.txt

# Solve Problems (add solution*.py and edit the corresponding test_day_*.py)
# ...

# run testings
$ pytest                        # run all testings
$ pytest tests/test_day_001.py  # run certain testing

# check format with wemake-python-styleguide
$ flake8 --format=wemake solutions
```

You can check the full list of violations and explanations in this [documentation](https://wemake-python-stylegui.de/en/stable/pages/usage/violations/).

### Build up Site

```bash
# clone the project and install dependencies
$ git clone https://github.com/Hsins/Daily-Coding-Problem.git
$ git checkout docs
$ pip install -r requirements

# start the server
$ mkdocs serve

# build site
$ mkdocs build
```

Note that the default directory for publishing would be `./site`.


## License

Licensed under the MIT License, Copyright © 2020-present Hsins.
