# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

pyboon 是一个 Python 工具库，为 Python 开发提供便利函数。这是一个可发布的 PyPI 包，专注于简化日常开发任务。

## 核心架构

### 模块化设计
项目采用模块化架构，每个模块专注特定功能域：

- **x.py**: 核心工具函数，包含字符串转换、时间处理、JSON 操作、表格展示等
- **chain.py**: 函数式编程链式操作，实现 Chain 类支持 map、filter 等操作
- **file.py**: 文件操作和模板引擎，支持 Mustache 模板渲染
- **sql.py**: 数据库操作工具，基于 dataset 库提供 MySQL 连接和查询功能
- **rest.py**: HTTP 请求封装，简化 GET/POST/JSON/FORM 请求
- **underscore.py**: 函数式编程工具，提供 map、filter、reduce 等操作的增强版本
- **trans.py**: 数据转换工具
- **convert.py**: 数据类型转换工具
- **json2.py**: JSON 处理增强工具
- **datetime2.py**: 日期时间处理工具
- **qs.py**: 查询字符串处理工具
- **print2.py**: 打印输出增强工具

### 导入别名系统
项目在 `__init__.py` 中定义了简洁的导入别名：
```python
from . import trans as t
from . import file as f
from . import underscore as _
from .chain import Chain as __
```

## 开发命令

### 环境设置
```bash
# 安装开发工具
pipx install twine fabric3 pipenv

# 安装项目依赖
pipenv install

# 本地安装开发版本
fab li  # 等价于 pip install -e .

# 重新安装已发布版本
fab rei  # 从 PyPI 安装
fab rei:src  # 从官方源安装
```

### 测试
```bash
# 运行所有测试
python -m pytest test/

# 运行单个测试文件
python -m pytest test/test_chain.py
python -m pytest test/test_x.py

# 测试特定功能
python -m pytest test/test_sql.py -v
```

### 构建和发布
```bash
# 版本升级（通过 fabric）
fab upv      # 升级补丁版本 (0.0.24 -> 0.0.25)
fab upv:++   # 升级次版本 (0.0.24 -> 0.1.0) 
fab upv:+++  # 升级主版本 (0.0.24 -> 1.0.0)

# 构建和发布
fab up       # 自动升级版本、构建、上传到 PyPI

# 手动构建
python setup.py sdist bdist_wheel
twine upload dist/*

# Git 操作
fab push:"commit message"  # git add . && git commit && git push
```

## 代码结构规范

### 测试组织
- 每个模块都有对应的测试文件：`test/test_模块名.py`
- 测试直接从模块导入：`from pyboon.x import *`
- 测试函数使用 `test_` 前缀

### 依赖管理
项目使用双重依赖管理：
- `Pipfile`: 开发环境依赖管理（pipenv）
- `setup.py`: 包发布依赖声明

核心依赖包括：
- requests, bs4: HTTP 和网页处理
- rich: 终端输出美化
- pymysql, dataset: 数据库操作
- openpyxl: Excel 文件处理
- chevron: Mustache 模板引擎
- pyyaml, markdown: 文档处理

### 版本管理
版本号格式：`主版本.次版本.补丁版本`（如 0.0.24）
版本信息存储在 `setup.py` 中，通过 fabric 脚本自动管理。

## 重要约定

### 数据库配置
SQL 模块默认连接本地 MySQL：
- 默认 DB_URL: `mysql://root:password@localhost:3306/hello?charset=UTF8MB4`
- 使用 dataset 库进行 ORM 操作
- 支持数据库信息查询和表结构分析

### 模板系统
文件模块支持 Mustache 模板：
- 模板存储在 `templates/` 目录
- 使用 `{{}}` 作为分隔符
- 支持模板路径和内容的动态渲染

### 链式操作
Chain 类提供 JavaScript 风格的函数式编程：
```python
from pyboon import __
result = __(items).map(func).to_list()
```

此项目专注于实用性和简洁性，为 Python 开发者提供常用工具的便捷封装。