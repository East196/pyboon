#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
from fabric.api import local, lcd

def cwd():
    local(os.getcwd())

def push(msg):
    local('git add .')
    local(f'git commit -m "{msg}"')
    local('git push')

def clean():
    local('python setup.py sdist bdist_wheel')
    local('twine upload dist/*')
    local('rd /s/q build')
    local('rd /s/q dist')
    local('rd /s/q pyboon.egg-info')

    