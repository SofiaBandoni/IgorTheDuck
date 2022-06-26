import re
import requests
from bs4 import BeautifulSoup

dagfile_link = 'https://raw.githubusercontent.com/SofiaBandoni/IgorTheDuck/master/Folder2/dagfile.py'

def get_raw_code(dagfile_link):
    url = dagfile_link
    response = requests.get(url)
    response_code = response.status_code
    if response_code != 200:
        print("Error ocurred: " + str(response.status_code))
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    return(dom)

dagfile_regex_dict = {'dag' : re.compile(r'(?<=dag_id[\s=|=])\S*', re.IGNORECASE),
                      'owner' : re.compile(r'(?<="owner":).\S*', re.IGNORECASE),
                      'email' : re.compile(r'(?<="email":).\S*', re.IGNORECASE)}

def dagfile_parser(raw_code):
    for key, value in dagfile_regex_dict.items():
        matches = value.findall(raw_code)
        for match in matches:
            data = match.replace(' ','').replace('"','').replace('[', '').replace(']', '').replace(',','')
            print(data)
    
if __name__ == '__main__':
    raw_code = str(get_raw_code(dagfile_link))
    dagfile_content = dagfile_parser(raw_code)