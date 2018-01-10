
from app.models import *

class CoinModel(Document):
    """
    코인 현재 가격
    """
    symbol = StringField(primary_key=True)
    name = StringField(required=True)
    rate = StringField(required=True)

class RecommendModel(Document):
    """
    추천 코인 정보
    """
    symbol = StringField(primary_key=True)
    score = FloatField(required=True)
