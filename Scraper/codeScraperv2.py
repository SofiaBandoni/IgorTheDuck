import requests
from bs4 import BeautifulSoup
from sql_metadata import Parser
import sqlparse

# Indicar la url del repositorio a escrapear
github_url = 'https://raw.githubusercontent.com/SofiaBandoni/IgorTheDuck/master/Folder1/query1.hql'


def get_raw_code(github_url):
    url = github_url
    response = requests.get(url)
    response_code = response.status_code
    if response_code != 200:
        print("Error ocurred: " + str(response.status_code))
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    return(dom)
    
def get_sql_tables(raw_code):
    # tables = Parser(str(raw_code)).tables
    # return(tables)
    raw_sql = str(raw_code)
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

if __name__ == '__main__':
    raw_code = get_raw_code(github_url)
    # print(raw_code)
    sql_tables = get_sql_tables(raw_code)
    # print(sql_tables)
    