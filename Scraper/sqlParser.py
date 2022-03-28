from sql_metadata import Parser

raw_sql = """insert into overwrite partition database.tabla_insert as select *

from
database.table
inner join database.table2 on table.id = table2.id"""

sql = raw_sql.replace("overwrite","") .replace("partition", "")
tablas = Parser(str(sql)).tables
print(tablas)

for tabla in tablas:
    sink = sql.find(tabla)
    determine_sink = sql[0:sink]
    if "insert into" in determine_sink and "from" not in determine_sink:
        print(tabla + ": sink")
    else:
        print(tabla + ": source")
