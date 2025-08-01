from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urljoin
import os
import re
import pprint 
import pdftotext
from io import BytesIO


# make a directory to put in the pdfs from  the link 'https://learncodethehardway.com/setup/python/ttb/'
DOWNLOAD_DIR = 'ttb_pdfs'
DIRECTORY = os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# request and download the website
resp = request.urlopen('https://learncodethehardway.com/setup/python/ttb/')
content = resp.read()

# access all links to the pdfs and download them download the pdfs 
pdf_links =[]
pdf_num = 1
BASE_URL = 'https://learncodethehardway.com/setup/python/ttb/'
soup = BeautifulSoup(content,'html5lib' )
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.lower().endswith('.pdf') and pdf_num <= 5:
        full_url = urljoin(BASE_URL,href)
        pdf_links.append(full_url)
        pdf_num += 1
    else:
        pass



# download the files from the link


for pdf_link in pdf_links:
    filename = os.path.basename(pdf_link)
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    if not os.path.exists(filepath):
        print(f"📥 Downloading {filename}...")
        try:
            file = request.urlopen(pdf_link)
            file_bytes = file.read() # these are bytes
            
            # add the downloaded file the disk by copying the downlaoded content to the file
            with open(filepath, 'wb') as f:
                f.write(file_bytes)
                
            pdf_data = pdftotext.PDF(BytesIO(file_bytes))
            print(f"✅ Downloaded: {filename}")
            # processs file content to list of lines
            lines = "".join(pdf_data).split("\n")
            num = 1
            for line in lines:
                # do data munging on them
                #e.g finding all digits with spaces of commas
                digits = re.search(r'^[,\d\s]+$',line)
                if digits:
                    print(f"We've got this [{num}]: {digits.group()}")
                    num += 1
                else:
                    pass
                

        except Exception as e:
            print(f"❌ Failed to download {pdf_link}: {e}")
    else:
        print(f"✅ Already downloaded: {filename}")
        
            
    
    
    

