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
        recommends = RecommendModel.objects().order_by('-score').to_json()
        recommendCoins = []
        for item in recommends:
            coin_info = CoinModel.objects({'symbol', item['symbol']}).first()
            item['name'] = coin_info.name;
            item['rate'] = coin_info.rate;
            recommendCoins.append()
            
        return Response(
         recommendCoins,
         200,
         content_type='application/json; charset=utf8')
