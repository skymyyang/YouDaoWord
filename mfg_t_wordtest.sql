/*
Navicat MySQL Data Transfer

Source Server         : 192.168.180.187
Source Server Version : 50624
Source Host           : 192.168.180.187:3306
Source Database       : metest

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2017-03-13 18:09:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for mfg_t_wordtest
-- ----------------------------
DROP TABLE IF EXISTS `mfg_t_wordtest`;
CREATE TABLE `mfg_t_wordtest` (
  `f_word` varchar(255) DEFAULT NULL,
  `f_asymbol` varchar(255) DEFAULT NULL,
  `f_esymbol` varchar(255) DEFAULT NULL,
  `f_explain` text,
  `f_cizu` text,
  `f_liju` text,
  `f_xiangguancihui` text,
  `f_aspoken` varchar(255) DEFAULT NULL,
  `f_espoken` varchar(255) DEFAULT NULL,
  `f_biaoji` text,
  `f_type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mfg_t_wordtest
-- ----------------------------
