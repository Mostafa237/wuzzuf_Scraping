from bs4 import BeautifulSoup
import requests
import csv
import attrs
from itertools import zip_longest

result = requests.get("https://wuzzuf.net/search/jobs/?q=data+analysis&a=hpb")

src = result.content
# print(type(src))

soup = BeautifulSoup(src, "lxml")
# jop title , jop skills , company names , locations name
jop_title = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", {"class": "css-17s97q8"})
locations_name = soup.find_all("span", {"class": "css-5wys0k"})
jop_skills = soup.find_all("div", {"class": "css-y4udm8"})

jops_lis = []
companys_lis = []
locations_lis = []
skills_lis = []
links_lis = []
salary_lis = []

for item in range(len(jop_title)):
    jops_lis.append(jop_title[item].text)
    links_lis.append(jop_title[item].find("a").attrs["href"])
    links_lis[item] = "https://wuzzuf.net" + links_lis[item]
    companys_lis.append((company_names[item].text))
    locations_lis.append(locations_name[item].text)
    skills_lis.append((jop_skills[item].text))



header = ["jops", "companys", "locations", "skills", "linkes"]
rows = list(zip(jops_lis, companys_lis, locations_lis, skills_lis, links_lis))
with open("C:/Users/desha/PycharmProjects/pythonProject1/dataAnalysis_info.csv", "w") as file:
    wr = csv.writer(file)
    wr.writerow(header)
    wr.writerows(rows)
