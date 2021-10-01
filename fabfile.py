#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import re
from fabric.api import local, lcd
from pyboon import x, f


def push(msg):
    local('git add .')
    local(f'git commit -m "{msg}"')
    local('git push')


def up():
    upv()
    local('python setup.py sdist bdist_wheel')
    local('twine upload dist/*')
    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('pyboon.egg-info')


def upv(abc="+"):
    '''
    升版
    '''
    content = str(f.read("setup.py"))
    ret = re.search(r"version='([0-9]+.\d..*)',", content)
    vs, v = ret.group(0), ret.group(1)
    a, b, c = ret.group(1).split(".")
    a = str(int(a)+1) if abc == "+++" else a
    b = str(int(b)+1) if abc == "++" else b
    c = str(int(c)+1) if abc == "+" else c
    nv = ".".join([a, b, c])
    nvs = vs.replace(v, nv)
    ncontent = content.replace(vs, nvs)
    f.write(os.path.join(os.getcwd(), "setup.py"), ncontent)


def t():
    f.CURRENT_DIR = os.path.split(os.path.realpath(__file__))[0]
    print(f.current_src_dir())


def rei(src=None):
    local('pip uninstall pyboon -y')
    if src:
        local('pip install -i https://pypi.org/simple pyboon')
    else:   
        local('pip install pyboon')
