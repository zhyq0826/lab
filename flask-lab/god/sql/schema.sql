drop database IF EXISTS `blog`;

create database if not EXISTS `blog`;

ALTER database `blog` CHARACTER SET utf8mb4;

SET character_set_client = utf8mb4;
SET character_set_connection = utf8mb4;
SET character_set_database = utf8mb4;
SET character_set_results = utf8mb4;
SET character_set_server = utf8mb4;

SET collation_connection = utf8_general_ci;
SET collation_database = utf8_general_ci;
SET collation_server = utf8_general_ci;

use blog;

create table if not EXISTS entries (
    id bigint not null auto_increment primary key,
    title blob not null,
    uid bigint not null,
    dig_count bigint  not null default 0,
    comment_count bigint  not null default 0,
    `text` blob not null
);

create table if not EXISTS tag (
    id bigint  not null auto_increment primary key,
    name varchar(255) not null
);


create table if not EXISTS user (
    id bigint not null primary key,
    username varchar(255) not null,
    avatar varchar(255) not null
);


create index user_name on user (username);

create index entries_title on entries (title(20));

