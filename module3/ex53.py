import requests
from pprint import pprint
import sys
import csv
import sys

api_url = "http://learncodethehardway.com/api/course"
# get all courses
r = requests.get(api_url)
data = r.json()
# pprint(data)

r = requests.get(api_url, params={
    "course_id": 1, "full":'true'
})

data = r.json()
if isinstance(data, dict):
    #wrap it up in a list
    data = [data]
else:
    exit(1)

# import data to csv
with open('downloaded.csv','w', newline='', encoding='utf-8') as f:
    # getting field names
    fieldnames = data[0].keys()
    print("The keys are {}".format(fieldnames))

    # getting the writer
    writer = csv.DictWriter(f, fieldnames= fieldnames)

    # now write the column names or let's call them headers for now
    writer.writeheader()

    # now write the row names
    writer.writerows(data)
    
    

