import pandas as pd
from functools import reduce

repos =  [{'master_folder': 'Folder1', 
           'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder1'}, 
          {'master_folder': 'Folder2', 
           'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder2'}, 
          {'master_folder': 'Folder3', 
           'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder3'}, 
          {'master_folder': 'Scraper', 
           'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}]

py_dicts = [{'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder1/dagfile.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder1'}, 
            {'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder2/dagfile.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder2'}, 
            {'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/dagfileParser.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}, 
            {'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/ghRepoScraper.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}, 
            {'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/ghRepoScraperv2.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}, 
            {'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/hqlParser.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}, 
            {'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/Deprecated/codeScraper.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper/Deprecated'}, 
            {'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/Deprecated/repoScraper.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper/Deprecated'}, 
            {'python_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/Deprecated/sqlParser.py', 
             'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper/Deprecated'}]
hql_dicts = [{'hql_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder1/query1.hql', 
              'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder1'}, 
             {'hql_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder2/query2.hql', 
              'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder2'}, 
             {'hql_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder3/query3.hql', 
              'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder3'}, 
             {'hql_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder3/SubFolder/query4.hql', 
              'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder3/SubFolder'}, 
             {'hql_raw_links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder3/SubFolder/Subsubfolder/query5.hql', 
              'master_folder_link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder3/SubFolder/Subsubfolder'}]


repos_df = pd.DataFrame(repos)
py_dict_df = pd.DataFrame(py_dicts)
hql_dicts_df = pd.DataFrame(hql_dicts)
merged_df = reduce(lambda x,y: pd.merge(x,y, on='master_folder_link', how='left'), [repos_df, py_dict_df, hql_dicts_df])
merged_df.to_excel("df.xlsx")

merged_df_py = pd.merge(py_dict_df, repos_df, on='master_folder_link', how='left')
miss_df_bool = (merged_df_py['master_folder'].isna())
merged_df_py[miss_df_bool].to_excel("missmatched_py.xlsx")

merged_df_hql = pd.merge(hql_dicts_df, repos_df, on='master_folder_link', how='left')
miss_df_bool = (merged_df_hql['master_folder'].isna())
merged_df_hql[miss_df_bool].to_excel("missmatched_hql.xlsx")

