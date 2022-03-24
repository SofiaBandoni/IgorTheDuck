import requests
from bs4 import BeautifulSoup

# Indicar la url del repositorio a escrapear
github_url = 'https://github.com/SofiaBandoni/IgorTheDuck'

# Armo una funcion que recorre el repositorio y va a devolver los links de cada carpeta dentro del mismo
def get_repositories(github_url):
    url = github_url
    response = requests.get(url)
    response_code = response.status_code
    if response_code != 200:
        print("Error ocurred: " + str(response.status_code))
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    all_folders = dom.find_all(class_ = 'js-navigation-open Link--primary')
    links = []
    for folder in range(len(all_folders)):
        links.append("https://github.com" + all_folders[folder].get("href"))       
    return(links)

          
def get_dagfiles(repos):
    for repo in repos:
        url = repo
        response = requests.get(url)
        response_code = response.status_code
        if response_code != 200:
            print("Error ocurred: " + str(response.status_code))
            return
        html_content = response.content
        dom = BeautifulSoup(html_content, 'html.parser')
        dagfiles = dom.find_all(class_ = 'js-navigation-open Link--primary')
        #print(dagfiles)
        dagfiles_links = []
        for dagfile in range(len(dagfiles)):
            dagfiles_links.append("https://github.com" + dagfiles[dagfile].get("href"))
        print(dagfiles_links)
        #return(dagfiles_links)
        
    

if __name__ == '__main__':
    print('Started Scraping Main Repository')
    repos = get_repositories(github_url)
    print("These are the folders links in main repository:" )
    print(repos)
    print("Started Scraping Folders In Main Repository")
    print("These are the links in folders of main repository: ")
    dagfiles = get_dagfiles(repos)
    #print("These are de dagfiles links:")
    #print(dagfiles)
    