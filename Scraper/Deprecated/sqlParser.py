from sql_metadata import Parser
import sqlparse

raw_sql = """drop table if exists data_lake_analytics.tmp_abnbankinfo{{ envCode }} purge;

 

create external table data_lake_analytics.tmp_abnbankinfo{{ envCode }} as

select distinct bank_code,

    FIRST_value(bank_name) over(partition by bank_code order by day desc) as bank_name

from pre_facturacion.cbs_ar_dic_bank_info;"""

splitted = sqlparse.split(raw_sql)


for query in splitted:
    if "select" in query:
        to_query_parser = query
    else:
        print("Se descarta")


sql = to_query_parser.replace("overwrite","").replace("create external table", "insert into")
tablas = Parser(str(sql)).tables

for tabla in tablas:
    sink = sql.find(tabla)
    determine_sink = sql[0:sink]
    if "insert" in determine_sink and "partition" not in determine_sink and "from" not in determine_sink:
        print(tabla + ": sink")
    elif "partition" in determine_sink and "from" not in determine_sink:
        print(tabla + ": partition")
    else:
        print(tabla + ": source")
