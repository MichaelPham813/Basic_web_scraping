from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd

###List of SCP###
scps_lists = []

#Get url from wikis list of scps
url = "https://scpcb.fandom.com/wiki/List_of_SCPs"
page = urlopen(url)


#Get the response and content 
with page as response:
    #Parse the HTML element
    soup = bs(response,"html.parser")
    
    #Get header element
    table = soup.find_all("table")[0]
    header = table.find_all("th")
    
    #Save header into lists
    scps_lists = [anchor.get_text().strip() for anchor in header]
    
    #Create dataframe
    df = pd.DataFrame(columns = scps_lists)
    
    #Get content element
    table_content_title = soup.find_all("tbody")[0]
    table_content_row = table_content_title.find_all("tr")
    for rows in table_content_row[1:]:
        rows_data = rows.find_all("td")
        rows_data_content = [data.get_text().strip() for data in rows_data]
        length = len(df)
        df.loc[length] = rows_data_content

df.to_csv("D:/AnalystProjects/SCP_List.csv")