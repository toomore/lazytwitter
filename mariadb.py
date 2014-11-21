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
        print 'ENTERRR'
        return self

    def sql(self, sql, params=None):
        self.cur.execute(sql, params)
        return self.cur.fetchall()

    def get_columns(self):
        return [i[0] for i in self.cur.description]

    def get_cur(self):
        return self.cur

    def get_rowcount(self):
        return self.cur.rowcount

    def __exit__(self, type, value, traceback):
        print type, value, traceback
        self.cur.close()
        self.conn.close()


class Userdata(MariaDB):
    pass

##cur.execute("""select * from %s""" % setting.TESTTABLE)

with Userdata() as userdata:
    result = userdata.sql("""select * from %s""" % setting.TESTTABLE)

for i in result:
    print i

print userdata.get_columns()
print 'get cur:', userdata.get_rowcount()

#print '>>> print cur', cur, dir(cur)
#columns = [i[0] for i in cur.description]
#print columns
#print cur.description_flags
#cur.close()
