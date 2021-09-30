#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
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
    local('rd /s/q build')
    local('rd /s/q dist')
    local('rd /s/q pyboon.egg-info')


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


def rei():
    local('pip uninstall pyboon -y')
    local('pip install pyboon')
