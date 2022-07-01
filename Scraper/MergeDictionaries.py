import pandas as pd
from functools import reduce

repos =  [{'Master Folder': 'Folder1', 
           'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder1'}, 
          {'Master Folder': 'Folder2', 
           'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder2'}, 
          {'Master Folder': 'Folder3', 
           'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder3'}, 
          {'Master Folder': 'Scraper', 
           'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}]

py_dicts = [{'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder1/dagfile.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder1'}, 
            {'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder2/dagfile.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder2'}, 
            {'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/dagfileParser.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}, 
            {'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/ghRepoScraper.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}, 
            {'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/ghRepoScraperv2.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}, 
            {'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/hqlParser.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper'}, 
            {'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/Deprecated/codeScraper.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper/Deprecated'}, 
            {'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/Deprecated/repoScraper.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper/Deprecated'}, 
            {'Python Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Scraper/Deprecated/sqlParser.py', 
             'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Scraper/Deprecated'}]

hql_dicts = [{'HQL Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder1/query1.hql', 
              'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder1'}, 
             {'HQL Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder2/query2.hql', 
              'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder2'}, 
             {'HQL Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder3/query3.hql', 
              'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder3'}, 
             {'HQL Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder3/SubFolder/query4.hql', 
              'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder3/SubFolder'}, 
             {'HQL Raw Links': 'https://raw.githubusercontent.com//SofiaBandoni/IgorTheDuck/master/Folder3/SubFolder/Subsubfolder/query5.hql', 
              'Master Folder Link': 'https://github.com/SofiaBandoni/IgorTheDuck/tree/master/Folder3/SubFolder/Subsubfolder'}]

repos_df = pd.DataFrame(repos)
py_dict_df = pd.DataFrame(py_dicts)
hql_dicts_df = pd.DataFrame(hql_dicts)
merged_df = reduce(lambda x,y: pd.merge(x,y, on='Master Folder Link', how='left'), [repos_df, py_dict_df, hql_dicts_df])
merged_df.to_excel("df.xlsx")

merged_df = pd.merge(py_dict_df, repos_df, on='master_folder_link', how='left')
miss_df_bool = (merged_df['master_folder'].isna())
merged_df[miss_df_bool].to_excel("missmatched.xlsx")
