#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import codecs
import chevron

CURRENT_DIR = os.path.split(os.path.realpath(__file__))[0]


def current_src_dir():
    return CURRENT_DIR


def read(rpath):
    with codecs.open(rpath, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def write(rpath, content):
    dir, _ = os.path.split(rpath)
    if not os.path.exists(dir):
        os.makedirs(dir)
    with codecs.open(rpath, 'w', encoding='utf-8') as f:
        f.write(content)


def ms(args):
    return chevron.render(**args, def_ldel='{{', def_rdel='}}')


def tpl(path_template, data):
    t = os.path.join(current_src_dir(), "templates", path_template)
    with codecs.open(t, "r", encoding='utf-8') as f:
        content_template = f.read()
    path_args = {'template': path_template, 'data': data}
    content_args = {'template': content_template, 'data': data}
    path, content = ms(path_args), ms(content_args)
    rpath = os.path.join(current_src_dir(), path.replace(".mst", ""))
    write(rpath, content)
    return rpath, content


def rm(path_template, data):
    path_args = {'template': path_template, 'data': data}
    path = ms(path_args)
    rpath = os.path.join(current_src_dir(), path.replace(".mst", ""))
    rmpath(rpath)


def rmdir(path_template, data):
    path_args = {'template': path_template, 'data': data}
    path = ms(path_args)
    rpath = os.path.join(current_src_dir(), path)
    shutil.rmtree(rpath)


def rmpath(rpath):
    if os.path.exists(rpath):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(rpath)
        # os.unlink(rpath) #正在使用会报错
    else:
        print('no such file:%s' % rpath)  # 则返回文件不存在


def _rmline(rpath, rline):
    content = read(rpath)
    content = content.replace(rline, '')
    write(rpath, content)
    print("_rmline", rpath, rline)


def rmline(path, line_template, data):
    line_args = {'template': line_template, 'data': data}
    rline = ms(line_args)
    rpath = os.path.join(current_src_dir(), path.replace(".mst", ""))
    _rmline(rpath, rline)


def _insert_before(rpath, xline, rline):
    content = read(rpath)
    content = content.replace(xline, rline+"\n"+xline)
    write(rpath, content)
    print("_insert_before", rpath, rline)


def insert_before(path, xline, line_template, data):
    line_args = {'template': line_template, 'data': data}
    rline = ms(line_args)
    rpath = os.path.join(current_src_dir(), path.replace(".mst", ""))
    _insert_before(rpath, xline, rline)
