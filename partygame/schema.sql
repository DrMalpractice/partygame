create table if not exists user (
    userid          integer         primary key autoincrement not null,
    username        varchar(20)     not null,
    password_hash   varchar(64)     not null,
    email           varchar(256)    unique not null,
    admin           boolean         not null default(0),
    registered      datetime        not null default(datetime('now')),
    lastlogin       datetime        not null default(datetime('now'))
);
