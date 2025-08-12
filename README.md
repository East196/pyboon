# pyboon

一个为 Python 开发者提供便利的工具库。

## 特性

- **链式操作**: JavaScript 风格的函数式编程支持
- **数据库工具**: 基于 dataset 的 MySQL 操作封装
- **HTTP 请求**: 简化的 REST API 调用
- **文件操作**: 支持 Mustache 模板的文件处理
- **数据转换**: 字符串格式转换（驼峰、下划线等）
- **表格展示**: 基于 rich 的美化输出
- **函数式工具**: map、filter、reduce 等操作的增强版本

## 安装

```bash
pip install pyboon
```

## 快速开始

```python
from pyboon import x, f, _, __

# 字符串转换
x.to_camel("hello_world")        # "helloWorld"
x.to_underscore("HelloWorld")    # "hello_world"

# 链式操作
numbers = [1, 2, 3, 4, 5]
result = __(numbers).map(lambda x: x * 2).to_list()  # [2, 4, 6, 8, 10]

# 函数式操作
_.map2([1, 2, 3], lambda x: x * 2)     # [2, 4, 6]
_.filter2([1, 2, 3, 4], lambda x: x > 2)  # [3, 4]

# 文件操作
content = f.read("example.txt")
f.write("output.txt", "Hello World")

# 表格展示
data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
x.print_table(data)
```

## 模块概览

| 模块 | 功能 | 导入别名 |
|------|------|----------|
| x | 核心工具函数 | `from pyboon import x` |
| chain | 链式操作 | `from pyboon import __` |
| file | 文件和模板操作 | `from pyboon import f` |
| underscore | 函数式编程工具 | `from pyboon import _` |
| sql | 数据库操作 | `from pyboon.sql import *` |
| rest | HTTP 请求封装 | `from pyboon.rest import *` |

## 开发指南

### 环境设置
```bash
pipx install twine fabric3 pipenv
pipenv install
```

### 本地安装
```bash
fab li  # pip install -e .
```

### 测试
```bash
python -m pytest test/
```

### 构建发布
```bash
fab up  # 自动升级版本并发布到 PyPI
```

## 许可证

Apache License 2.0
