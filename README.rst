Introduction
============

pyramid_rewrite is a small extension for pyramid to rewrite urls before further processing takes place.

Documentation
=============

Usage example::

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

Better documentation will follow.

