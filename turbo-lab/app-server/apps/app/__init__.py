
from turbo import register

import app, api


register.register_group_urls('', [
    ('/', app.HomeHandler),
])

register.register_group_urls('/v1', [
    ('', api.HomeHandler),
    ('/celery', api.TestCeleryHandler),
])
