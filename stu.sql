/*
 Navicat Premium Data Transfer

 Source Server         : localhost_1521_ORCL
 Source Server Type    : Oracle
 Source Server Version : 120200
 Source Host           : localhost:1521
 Source Schema         : C##DHQ

 Target Server Type    : Oracle
 Target Server Version : 120200
 File Encoding         : 65001

 Date: 02/07/2020 19:41:15
*/


-- ----------------------------
-- Table structure for stu
-- ----------------------------
DROP TABLE "C##DHQ"."stu";
CREATE TABLE "C##DHQ"."stu" (
  "NAME" VARCHAR2(255 BYTE) VISIBLE,
  "CLASS" VARCHAR2(255 BYTE) VISIBLE,
  "NUMBER" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "SCORE" VARCHAR2(255 BYTE) VISIBLE
)
TABLESPACE "SYSTEM"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  FREELISTS 1
  FREELIST GROUPS 1
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of stu
-- ----------------------------
INSERT INTO "C##DHQ"."stu" VALUES ('马一', '一班', '3', '73');
INSERT INTO "C##DHQ"."stu" VALUES ('马小云', '一班', '1', '41');
INSERT INTO "C##DHQ"."stu" VALUES ('马小腾', '一班', '2', '99');
INSERT INTO "C##DHQ"."stu" VALUES ('王小林', '一班', '4', '97');
INSERT INTO "C##DHQ"."stu" VALUES ('丁一', '一班', '6', '60');
INSERT INTO "C##DHQ"."stu" VALUES ('小明', '一班', '7', '88');

-- ----------------------------
-- Primary Key structure for table stu
-- ----------------------------
ALTER TABLE "C##DHQ"."stu" ADD CONSTRAINT "SYS_C008072" PRIMARY KEY ("NUMBER");

-- ----------------------------
-- Checks structure for table stu
-- ----------------------------
ALTER TABLE "C##DHQ"."stu" ADD CONSTRAINT "SYS_C008071" CHECK ("NUMBER" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "C##DHQ"."stu" ADD CONSTRAINT "SYS_C008340" CHECK ("NUMBER" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
