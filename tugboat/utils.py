# encoding: utf-8
"""
Utility methodss
"""


def get_post_data(request):
    """
    Attempt to coerce POST json data from the request, falling
    back to the raw data if json could not be coerced.
    :param request: flask.request

    :return: dict
    """
    try:
        post_data = request.get_json(force=True)
    except:
        post_data = request.values

    return post_data
