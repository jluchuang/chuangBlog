USE blog;
SET NAMES 'utf8';
SET time_zone = "+08:00";

alter table blog_article change type_id tag_id INT(11);
alter table blog_article add column key_words varchar(256) not NULL default "";

create table blog_tag(
    id INT(11) not null AUTO_INCREMENT, 
    type_name varchar(256) not null default "", 
    primary key (id)
);