import logging

logger = logging.getLogger(__name__)

def rewrite_tween_factory(handler, registry):
    def rewrite_tween(request):
        for pattern, target in registry.rewrite_rules:
            print pattern, target
            path = request.path
            mo = pattern.match(path)
            if mo is not None:
                host_url = request.host_url
                qs = '?' + request.query_string
                path = target % mo.groupdict()
                logger.info('Rewriting url: %s --> %s' % (request.path, path))
                path_qs = path + qs
                url = host_url + path_qs
                request.url = url
                request.path = path
                request.path_qs = path_qs
        response = handler(request)
        return response
    return rewrite_tween

def add_rewrite_rule(config, pattern, target):
    pattern = re.compile(pattern)
    if not hasattr(config.registry, 'rewrite_rules'):
        config.registry.rewrite_rules = []
    config.registry.rewrite_rules.append((pattern, target))
    def register_tween():
        config.add_tween(rewrite_tween_factory)
    config.action('rewrite_tween', register_tween)

def includeme(config):
    config.add_directive('add_rewrite_rule',
                         add_rewrite_rule)

