"""
setting json as content-type of response
"""


import wsmeext.pecan as wsme_pecan


def expose(*args, **kwargs):
    """descriptor
    """
    if 'rest_content_types' not in kwargs:
        kwargs['rest_content_types'] = ('json',)

    return wsme_pecan.wsexpose(*args, **kwargs)

