from unittest import TestCase as TC

from app import app


class TCBase(TC):
    def __init__(self):
        TC.__init__(self)

        self.client = app.test_client()
