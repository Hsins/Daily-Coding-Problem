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
[![README in Traditional Chinese](https://img.shields.io/badge/README-English-8CA1AF.svg?logo=read-the-docs&style=flat-square)](./README.md)  
[![](https://img.shields.io/badge/Easy-29-34ED43.svg?logo=&style=flat-square)]()
[![](https://img.shields.io/badge/Medium-33-51ADEF.svg?logo=&style=flat-square)]()
[![](https://img.shields.io/badge/Hard-25-EF5151.svg?logo=&style=flat-square)]()

</div>

## Features

- Follow this [article](https://wkrzywiec.medium.com/how-to-write-good-quality-python-code-with-github-actions-2f635a2ab09a) to set up the integration with CodeFactor, Linter and Unit Testing running with GitHub Actions.

## 分支狀況

專案共有三個分支，分別負責不同用途：

- [`main`](https://github.com/Hsins/Daily-Coding-Problem/tree/main) 存放解答程式以及測試程式的程式碼原始碼
- [`docs`](https://github.com/Hsins/Daily-Coding-Problem/tree/docs) 存放 [解答手冊](https://dcp.hsins.me/) 的程式原始碼
- [`gh-pages`](https://github.com/Hsins/Daily-Coding-Problem/tree/gh-pages) 託管由 GitHub Actions 根據 `docs` 分支存放的內容自動構建的靜態頁面文件（構建工作流的檔案設定可以在 [這裡](https://github.com/Hsins/Daily-Coding-Problem/blob/docs/.github/workflows/site-deployment.yml) 找到）

## 目錄結構

下述的目錄結構遵循文章 [Good Integration Practices](https://docs.pytest.org/en/stable/goodpractices.html) 所描述的概念，屬於 Pytest 所支持的常見測試用結構：

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

## 使用說明

### 題目練習

如果您想要透過此專案來練習與加強自己的解題能力，但卻不知道該如何進行測試以及檢查格式，可以遵循以下步驟：

```bash
# 下載當前專案並安裝依賴
$ git clone https://github.com/Hsins/Daily-Coding-Problem.git
$ pip install -r requirements.txt

# 練習題目（添加 solution*.py 並編輯對應的測試文件 test_day_*.py）
# ...

# 執行測試
$ pytest                        # 執行所有測試檔案
$ pytest tests/test_day_001.py  # 執行指定測試檔案

# 檢查格式（使用 wemake-python-styleguide 風格）
$ flake8 --format=wemake solutions
```

你可以在這份 [文件](https://wemake-python-stylegui.de/en/stable/pages/usage/violations/) 中查看所有不合法格式的說明。

### 建置站點

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

站點建置之後，所有的靜態文件會存放在預設的 `./site` 資料夾下。

## 授權許可

Licensed under the MIT License, Copyright © 2020-present Hsins.
