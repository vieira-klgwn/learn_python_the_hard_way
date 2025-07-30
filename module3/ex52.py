from bs4 import BeautifulSoup
from urllib import request 
import os
import re

pages = 0
page_list = []
if not os.path.exists('ttb_page.html'):
    while pages < 5:
        with open(f'ttb_page{pages}.html','wb') as f:
        resp = request.urlopen('https://learncodethehardway.com/setup/python/ttb/')
        body = resp.read() # make each body be appended in a list.
        f.write(body)
        page_list.append(body) # appending to the list, I don't know if this is correct
        pages += 1
    
else:
    read_pages = 0
    while read_pages < 5:
        with open(f'ttb_page{read_pages}.html', encoding='utf-8') as f:
        body = f.read()
        page_list.append(body) # appending to the list, I don't know if this is correct
        read_pages += 1
        
    

# now let us parse the html (body) we have into a text so we can interact with it
# if the code above works, then the aproach here can be using a loop that loops in each of the five files, and another one that loops in each line of the file. Remember that to loop in each line of the file requires also joining and stripping as in ex51

soup = BeautifulSoup(body,'html5lib')

print("The whole object is here: ",soup)
print("This is the title",soup.title)

# let us play with the data that we have ,using regex, 

content_body = soup.body

lines = "".join(content_body).strip('\n')
# now let us use regex

num = 1
for line in lines:
    search = re.search('(Report Period)', line)
    if search:
        print(f"[{num}]: {search.group()}")
        num += 1
    else:
        pass


        





