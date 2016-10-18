drop database IF EXISTS `blog`;

create database if not EXISTS `blog`;

ALTER database `blog` CHARACTER SET utf8;

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_database = utf8;
SET character_set_results = utf8;
SET character_set_server = utf8;

SET collation_connection = utf8_general_ci;
SET collation_database = utf8_general_ci;
SET collation_server = utf8_general_ci;

use blog;

create table if not EXISTS entries (
    id int unsigned not null auto_increment primary key,
    title text not null,
    `text` text not null
);