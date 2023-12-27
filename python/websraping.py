# web scrapping : scrapping the data from the web....

# urllib or requests -- this for thitting the endpoint

# bs4 -- this the parsing the data

import urllib.request
from bs4 import BeautifulSoup

url='https://www.shine.com/job-search/python-jobs?q=python'

url_info=urllib.request.urlopen(url)

# print(url_info)

# print(url_info.read())
html_content = url_info.read()

bs4_data = BeautifulSoup(html_content, 'html.parser')

print(bs4_data)

main_div= bs4_data.find('div', class_='jsrp_jsrp_leftPanel__OTRuh jsrp_leftPanel')


# print(main_div)

job_div= main_div.findAll('div',class_='jobCard_jobCard__jjUmu active white-box-border jobCard')

# print(job_div)

# print(len(main_div))

for job in job_div:
    job_title=job.find('h2')
    print(job_title.text)