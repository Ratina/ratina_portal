# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-09

Ratina localized tags and filters.
"""

__author__ = "Savor d'Isavano"

from django import template

register = template.Library()


class RangeNode(template.Node):
    def __init__(self, num, context_name):
        self.num, self.context_name = num, context_name
    def render(self, context):
        context[self.context_name] = range(int(self.num))
        return ""
        
@register.tag
def num_range(parser, token):
    """
    Takes a number and iterates and returns a range (list) that can be 
    iterated through in templates
    
    Syntax:
    {% num_range 5 as some_range %}
    
    {% for i in some_range %}
      {{ i }}: Something I want to repeat\n
    {% endfor %}
    
    Produces:
    0: Something I want to repeat 
    1: Something I want to repeat 
    2: Something I want to repeat 
    3: Something I want to repeat 
    4: Something I want to repeat
    """
    try:
        fnctn, num, trash, context_name = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError("%s takes the syntax %s number_to_iterate\
            as context_variable" % (fnctn, fnctn))
    if not trash == 'as':
        raise TemplateSyntaxError("%s takes the syntax %s number_to_iterate\
            as context_variable" % (fnctn, fnctn))
    return RangeNode(num, context_name)


def rt_date(value):
    return value.strftime('%-Y-%-m-%-d')

def rt_date_cn(value):
    return value.strftime('%-Y年%-m月%-d日')


register.filter('rt_date', rt_date)
register.filter('rt_date_cn', rt_date_cn)
