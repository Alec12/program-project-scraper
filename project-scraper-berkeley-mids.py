%%time

#import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import time
import warnings
warnings.filterwarnings("ignore")


#Create df framework
df = pd.DataFrame(columns= {'Year','Semester', 'Project', 'Description', 'Link'})

for j in np.arange(2015, 2024):
    for ssn in ('a-spring','b-summer','c-fall'):
        try:
            # Parse Domains
            domain = "https://www.ischool.berkeley.edu/programs/mids/capstone/"+str(j)+str(ssn)
            r = requests.get(domain)
            soup = BeautifulSoup(r.text, "html.parser")
            
            # Extract title and link from span_tags
            span_tags = soup.find_all('span', class_='field-content')
            titles = [span.find('a').text for span in span_tags if span.find('a') and 'projects' in span.find('a').get('href')]
            hrefs = ["https://www.ischool.berkeley.edu"+span.find('a').get('href') for span in span_tags if span.find('a') and 'projects' in span.find('a').get('href')]

            # Extract teaser_texts from div_tags
            div_tags = soup.find_all('div', class_='views-field views-field-field-teaser-text')
            teaser_texts = [div.get_text(strip=True) for div in div_tags if not div.find('p')]

            # Store information in a new DataFrame
            new_df = pd.DataFrame({'Year': j, 'Semester': ssn,'Project': titles,'Description': teaser_texts,'Link': hrefs})

            # Append to original DataFrame
            df = df.append(new_df, ignore_index=True)
            df = df[original_columns]
            print(domain)
        except:
            print("error or no program that semester")
            
            

