RECOMMEND_GET = {
    'tags': ['추천코인'],
    'description': '추천 코인 목록 조회',
    'parameters': [],
    'responses': {
        '200': {
            'description': '추천 코인 목록 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'rank': 1,
                        'token': 'BTC',
                        'name': 'BitCoin',
                        'rate': '12%'
                    },
                    {
                        'rank': 2,
                        'token': 'ETH',
                        'name': 'Ethereum',
                        'rate': '-12%'
                    }
                ]
            }
        }
    }
}
