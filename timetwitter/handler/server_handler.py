__author__ = 'shoyeb'

class ServerHandler(object):
    parse_form_data = True

    def __init__(self, app):
        self.app = app
        self.config = app.config_obj
