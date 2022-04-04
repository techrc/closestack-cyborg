"""
pecan configuration.
"""


app = {
    'root': 'cyborg.api.controllers.root.RootController',
    'modules': ['cyborg.api'],
    'debug': False
}
