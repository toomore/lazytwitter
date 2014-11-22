# -*- coding: utf-8 -*-
from mariadb import MariaDB


class Usertoken(MariaDB):
    def add_token(self, **kwargs):
        result = usertoken.insert("""insert into `usertoken`(user_id, screen_name, oauth_token, oauth_token_secret) value(%(user_id)s, %(screen_name)s, %(oauth_token)s, %(oauth_token_secret)s) ON DUPLICATE KEY UPDATE screen_name=%(screen_name)s, oauth_token=%(oauth_token)s, oauth_token_secret=%(oauth_token_secret)s""", kwargs)


if __name__ == '__main__':
    data = {'user_id': 32323,
            'screen_name': 'Toomore',
            'oauth_token': 'OOOO',
            'oauth_token_secret': 'SSSS',
           }
    with Usertoken() as usertoken:
        result = usertoken.select("""select user_id, screen_name from `usertoken`""")
        usertoken.add_token(**data)

    for i in result:
        print i
