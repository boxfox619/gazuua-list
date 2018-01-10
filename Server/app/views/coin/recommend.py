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

        # recommends = json.dumps([mongo_to_dict(recommend, ['recommend_coins']) for coin in RecommendModel.objects()], ensure_ascii=False)
        #
        # return Response(
        # ,
        #  200,
        #  content_type='application/json; charset=utf8')
