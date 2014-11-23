# -*- coding: utf-8 -*-
import couchdb

COUCHDB = couchdb.Server()

class CouchDBBase(dict):

    def __init__(self, db_name, _id, prepare_date=True):
        self.db_name = db_name
        self._id = _id
        self.db = COUCHDB[db_name]

        if prepare_date:
            self.get_data()

    def get_data(self):
        self.update(self.db.get(self._id, {}))

    def save(self):
        data = self.db.get(self._id, {'_id': self._id})
        data.update(self)
        self.db.save(data)


class Test(CouchDBBase):
    db_name = 'toomoretest'

    def __init__(self, _id):
        super(Test, self).__init__(self.db_name, _id)


if __name__ == '__main__':
    test = Test('oppp')
    print 'test: ', test
    #test['name'] = 'toomore2'
    #test.save()
