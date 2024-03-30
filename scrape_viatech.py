import json
from urllib import request
from bs4 import BeautifulSoup

url = "https://members.viatec.ca/job-board/Search?term=&DateFilter=0&from=&to=&CategoryValues=235246"

with request.urlopen(url) as resp:
    htmlData = resp.read()

parsedData = BeautifulSoup(htmlData, "html.parser")

card_body = parsedData.find_all("div", class_="card-body gz-content-body")

hrefs = []
for i in card_body:
    links = i.find_all("a")
    job_title = links[0].text.strip()
    job_href = links[0].get('href')
    company_href = links[1].get('href') if len(links) > 1 else None
    if company_href:
      hrefs.append((job_title,job_href, company_href))
        
print(hrefs)

job_details = []

for job_title,job_href, company_href in hrefs:
    with request.urlopen(company_href) as job_links:
        job_data = job_links.read()

    jobData = BeautifulSoup(job_data, "html.parser")
    
    gz_pagetitle = jobData.find("h1", class_="gz-pagetitle")
    gz_pagetitle = gz_pagetitle.text.strip() if gz_pagetitle else ""
    
    gz_member_repname = ""
    gz_member_reptitle = ""
    gz_details_reps = jobData.find("div", class_="gz-details-reps")
    if gz_details_reps:
        gz_member_repname = gz_details_reps.find(class_="gz-member-repname").text.strip()
        gz_member_reptitle = gz_details_reps.find(class_="gz-member-reptitle").text.strip()

    job_details.append({
        "job title": job_title,
        "company": gz_pagetitle,
        "url": job_href,
        "contact": gz_member_repname,
        "contactTitle": gz_member_reptitle
    })
    
with open("joblist.json", "w") as file:
    json.dump(job_details, file, indent=4)

for job_detail in job_details:
    print(job_detail)