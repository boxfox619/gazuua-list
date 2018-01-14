import json

from flask import Response
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.coin.recommend import *
from app.models.coin import RecommendModel, CoinModel

class Recommend(Resource):
    @swag_from(RECOMMEND_GET)
    def get(self):
        """
        추천 코인 정보 조회
        """
        recommends = RecommendModel.objects().order_by('-score')
        recommendCoins = []
        for item in recommends:
            symbol = json.loads(item.to_json())['_id']
            coin_info = CoinModel.objects(symbol=symbol).first()
            recommendCoins.append(json.loads(coin_info.to_json()))

        return Response(
         json.dumps(recommendCoins),
         200,
         content_type='application/json; charset=utf8')
