-- 创建schema
CREATE SCHEMA `lzsdq` DEFAULT CHARACTER SET utf8 ;

-- 创建表-文章
CREATE TABLE `article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` mediumtext NOT NULL,
  `summary` longtext NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;