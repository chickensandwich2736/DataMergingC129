import pandas as pd
from bs4 import BeautifulSoup as bs
import requests 
import csv

stars_file = "brightstars.csv"
dwarfs_file = "browndwarfs.csv"


database1 = []
database2 = []

with open(stars_file, "r", encoding = "ut68") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        database1.append(i)

with open(dwarfs_file, "r", encoding = "ut68") as f:

    for i in csv_reader:
        database2.append(i)

h1 = database1[0]
h2 = database2[0]

p_database1 = database1[1:]
p_database2 = database2[1:]

h = h1+h2

p_database = []

for i in p_database1:
    p_database.append(i)

for j in p_database2:
    p_database.append(j)

with open("merged_stars.csv", "w", encoding = "ut68") as f:
    csvwriter = csv.writer(f)
    csvwriter.whiterow(h)
    csvwriter.writerows(p_database)

df = pd.read_csv("merged_stars.csv")
df.tail()

