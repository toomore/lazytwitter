# -*- coding: utf-8 -*-
'''
ref: https://www.python.org/dev/peps/pep-0249/
'''
import MySQLdb
import setting


class MariaDB(object):

    def __init__(self):
        self.conn = MySQLdb.connect('localhost', setting.DBUSER, setting.DBPASS, setting.DBS)
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self

    def sql(self, sql, params=None, need_commit=False):
        self.cur.execute(sql, params)
        print self.cur._executed

        if need_commit:
            self.conn.commit()

        return self.cur.fetchall()

    def select(self, sql, params=None):
        result = self.sql(sql, params)
        columns = self.get_columns()
        return (dict(zip(columns, i)) for i in result)

    def insert(self, sql, params=None):
        self.sql(sql, params, True)

    def update(self, sql, params=None):
        self.sql(sql, params, True)

    def get_columns(self):
        return [i[0] for i in self.cur.description]

    def get_cur(self):
        return self.cur

    def get_rowcount(self):
        return self.cur.rowcount

    def __exit__(self, type, value, traceback):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    ##cur.execute("""select * from %s""" % setting.TESTTABLE)

    #with Usertoken() as usertoken:
    #    result = usertoken.select("""select user_id, screen_name from `usertoken`""")
    #    #result = usertoken.insert("""insert into `usertoken`(user_id, screen_name, oauth_token, oauth_token_secret) value('112222', 'toomore', 'A', 'B') ON DUPLICATE KEY UPDATE screen_name='toomore2', oauth_token='C', oauth_token_secret='D'""")

    #for i in result:
    #    print i

    #print usertoken.get_columns()
    print 'get cur:', usertoken.get_rowcount()

    #print '>>> print cur', cur, dir(cur)
    #columns = [i[0] for i in cur.description]
    #print columns
    #print cur.description_flags
    #cur.close()
