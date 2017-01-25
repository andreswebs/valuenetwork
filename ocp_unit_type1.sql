PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE "work_ocp_unit_type";
CREATE TABLE "work_ocp_unit_type" ("unit_type_id" integer NOT NULL PRIMARY KEY REFERENCES "general_unit_type" ("artwork_type_id"), "ocp_unit_id" integer NULL UNIQUE REFERENCES "valueaccounting_unit" ("id"), "unit_id" integer NULL UNIQUE REFERENCES "general_unit" ("id"));
INSERT INTO "work_ocp_unit_type" VALUES(34,NULL,NULL);
INSERT INTO "work_ocp_unit_type" VALUES(35,NULL,NULL);
INSERT INTO "work_ocp_unit_type" VALUES(36,NULL,NULL);
INSERT INTO "work_ocp_unit_type" VALUES(37,NULL,NULL);
INSERT INTO "work_ocp_unit_type" VALUES(38,NULL,NULL);
INSERT INTO "work_ocp_unit_type" VALUES(48,NULL,NULL);
INSERT INTO "work_ocp_unit_type" VALUES(67,NULL,NULL);
INSERT INTO "work_ocp_unit_type" VALUES(68,NULL,NULL);
COMMIT;