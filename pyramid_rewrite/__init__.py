# -*- coding: utf-8 -*-

"""
This is a small pyramid extension that allows to add rules for rewriting
the PATH_INFO portion of a requested URL.

Usage example:
    def main(global_config, **settings):
        config = Configurator(settings=settings)
        config.include('pyramid_rewrite')
        # add url rewriting rules...
        #   first parameter is a regular expression
        #   second parameter is the target url
        config.add_rewrite_rule(r'/favicon.ico', r'/static/favicon.ico')
        config.add_rewrite_rule(r'/gallery/(?P<subpath>.*)',
                                r'/root/%(subpath)s')
        #
        # ... rest of configuration
        #
        # return WSGI application instance
        return config.make_wsgi_app()
"""

# This software is distributed under the FreeBSD License.
# See the accompanying file LICENSE for details.
#
# Copyright 2012 Benjamin Hepp


import logging
import re

logger = logging.getLogger(__name__)


__version__ = 0.2


# Add configuration directive
def includeme(config):
    config.add_directive('add_rewrite_rule', add_rewrite_rule)
    config.add_tween('pyramid_rewrite.rewrite_tween_factory')


# Configuration directive for adding a rewrite rule
def add_rewrite_rule(config, pattern, target):
    tpattern = pattern
    if not pattern.startswith(r'^'):
        tpattern = '^' + tpattern
    if not pattern.endswith(r'$'):
        tpattern = tpattern + r'$'
    cpattern = re.compile(tpattern)
    if not hasattr(config.registry, 'rewrite_rules'):
        config.registry.rewrite_rules = []
    config.registry.rewrite_rules.append((pattern, cpattern, target))

# Tween to perform URL rewriting before a request is handled by Pyramid
def rewrite_tween_factory(handler, registry):

    if not hasattr(registry, 'rewrite_rules'):
        return handler

    def rewrite_tween(request):
        for pattern, cpattern, target in request.registry.rewrite_rules:
            path_info = request.path_info
            logger.debug('Matching pattern "%s" against "%s" ' \
                        % (pattern, path_info))
            mo = cpattern.match(path_info)
            if mo is not None:
                path_info = target % mo.groupdict()
                logger.debug('Rewriting url: %s --> %s' \
                            % (request.path_info, path_info))
                request.path_info = path_info
        return handler(request)

    return rewrite_tween
