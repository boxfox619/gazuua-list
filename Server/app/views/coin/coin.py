import json

from flask import Response
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.coin.coin import *
from app.models.coin import RecommendModel, CoinModel

class Coin(Resource):
    @swag_from(COIN_GET)
    def get(self):
        """
        코인 정보 조회
        """

        # return Response(
        # json.dumps([mongo_to_dict(coin, ['coins']) for coin in CoinModel.objects()], ensure_ascii=False),
        # 200,
        # content_type='application/json; charset=utf8')
