# coding: utf-8
__version__ = '0.1'
__all__ = ['one']

__author__ = 'ljun'

from process import traverse


def one(obj):
    """
             @type obj: object
    """
    return repr(traverse(obj)).replace(u"'", u'"')
