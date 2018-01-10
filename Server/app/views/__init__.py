from flask_restful import Api
from flask import render_template

from app.views.coin.coin import *
from app.views.coin.recommend import *

class ViewInjector(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        api = Api(app)

        @app.route('/')
        def index():
            return render_template('index.html')

        api.add_resource(Coin, '/coins')
        api.add_resource(Recommend, '/recommends')
