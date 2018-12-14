class CommonActions(object):

    """
    All miscellaneous common actions
    """

    @staticmethod
    def format_url(url, *routes):
        return url.rstrip(r'\/') + "/" + '/'.join([route.replace('/', '') for route in routes]).lstrip('')
