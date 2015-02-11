# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-11

Custom extensions.
"""

__author__ = "Savor d'Isavano"

import re
from functools import lru_cache

def _extract_args(argstr):
    arguments = argstr.split(',')
    try:
        x = arguments[0]
        args = {
            k.strip(): v.strip() for k, v in
            (
                arg.split('=') for arg in arguments
            )
        }
        return (x, args)
    except:
        return (argstr, {})    


_file_tag = re.compile('#file\((?P<file>.*?)\)')

def _convert_file_to_url(postobj, file):
    bf = next((f for f in list(postobj.files.all()) if f.name == file), None)
    if bf:
        return bf.file.url
    return '#file_error'
    

def _replace_file(postobj, content):
    def replace_method(matchobj):
        file = matchobj.group('file')
        return _convert_file_to_url(postobj, file)
    content = re.sub(_file_tag, replace_method, content)
    return content


_img_tag = re.compile('#image\((?P<arguments>.*?)\)')

def _replace_image(postobj, content):
    def replace_method(matchobj):
        argstr = matchobj.group('arguments')
        try:
            file, args = _extract_args(argstr)
            tmpl = '''<a class="preview" href="{file}" rel="prettyPhoto">
    <img src="{file}" style="max-width: 100%;{otherstyles}"{otherattrs}>
</a>
            '''
            otherattrs = {}
            otherstyles = {}
            for k, v in args:
                if k in ['width', 'height']:
                    otherstyles[k] = v
                else:
                    otherattrs[k] = v
            return tmpl.format(
                file=_convert_file_to_url(postobj, file),
                otherstyles=";".join(
                    "{}:{}".format(k, v) for k, v in otherstyles
                ) + (";" if otherstyles else ""),
                otherattrs = (" " if otherattrs else "") + " ".join(
                    '{}="{}"'.format(k, v) for k, v in otherattrs
                )
            )
        except:
            return '#image_error'

    content = re.sub(_img_tag, replace_method, content)
    return content


_audio_tag = re.compile('#audio\s*\((?P<arguments>.*?)\)')
    
def _replace_audio(postobj, content):
    def replace_method(matchobj):
        argstr = matchobj.group('arguments')
        try:
            file, args = _extract_args(argstr)
            tmpl = '''<audio controls>
    <source src="{file}"{otherattrs}>
    对不起，你该升级浏览器了。
</audio>
            '''
            otherattrs = {}
            for k,v in args:
                otherattrs[k] = v
            return tmpl.format(
                file=_convert_file_to_url(postobj, file),
                otherattrs = (" " if otherattrs else "") + " ".join(
                    '{}="{}"'.format(k, v) for k, v in otherattrs
                )
            )
        except:
            return '#audio_error'

    content = re.sub(_audio_tag, replace_method, content)
    return content


_ext_tag = re.compile('#(?P<tag>\w+?)\((?P<arguments>.*?)\)')

@lru_cache(128)
def ext_markdown(postobj, content, *args, **kwargs):
    def replace_method(matchobj):
        tag = matchobj.group('tag')
        matched =  matchobj.string[matchobj.start():matchobj.end()]
        if tag == 'image':
            next_ = _replace_image(postobj, matched)
        elif tag == 'audio':
            next_ = _replace_audio(postobj, matched)
        elif tag == 'file':
            next_ = _replace_file(postobj, matched)
        else:
            next_ = "#tag_error"
            return next_

        if next_ == content:
            return content

        return ext_markdown(postobj, next_)

    content = re.sub(_ext_tag, replace_method, content)
    return content
