#!/bin/bash

DB=sqlite3.db
TABLES=("produccion_coccion" "produccion_maltas_x_coccion" "produccion_lupulos_x_coccion" "produccion_levaduras_x_coccion" "produccion_agregados_x_coccion")

for TABLE in ${TABLES[@]};do
  INDEXES="$(echo "SELECT name FROM sqlite_master WHERE type == 'index' AND tbl_name = '$TABLE';"| sqlite3 $DB)"
  for i in $INDEXES; do
    echo "DROP INDEX '$i';" | sqlite3 $DB
  done
done
