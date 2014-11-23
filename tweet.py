# -*- coding: utf-8 -*-
from couchdbbase import CouchDBBase


class Tweet(CouchDBBase):
    db_name = 'lazytwitter_tweet'

    def __init__(self, _id):
        super(Tweet, self).__init__(self.db_name, _id)
