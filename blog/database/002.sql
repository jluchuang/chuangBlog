USE blog;
SET NAMES 'utf8';
SET time_zone = "+08:00";

ALTER TABLE blog_article ADD COLUMN summary LONGTEXT NOT NULL;

