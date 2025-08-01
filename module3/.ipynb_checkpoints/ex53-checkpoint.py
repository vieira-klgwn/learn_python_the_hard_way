import requests
from pprint import pprint
import sys
import csv

api_url = "http://learncodethehardway.com/api/course"
# get all courses
r = requests.get(api_url)
data = r.json()
# pprint(data)

r = requests.get(api_url, params={
    "course_id": 1, "full":'true'
})

data = r.json()
pprint(data)


