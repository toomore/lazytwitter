CREATE TABLE IF NOT EXISTS usertoken (
    user_id varchar(128) primary key NOT NULL,
    screen_namename varchar(128) NOT NULL,
    oauth_token varchar(128) NOT NULL,
    oauth_token_secret varchar(128) NOT NULL,
    created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    modifed timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
    ) engine=InnoDB default charset utf8;
