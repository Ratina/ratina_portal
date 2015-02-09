# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-10

Environment variables.
"""

__author__ = "Savor d'Isavano"

__all__ = ['env']

import os

_ENV_PREFIX = 'RATINA_PORTAL'

env = {
    k[len(_ENV_PREFIX)+1:]: v
    for k, v in os.environ.items() if k.startswith(_ENV_PREFIX)
}
