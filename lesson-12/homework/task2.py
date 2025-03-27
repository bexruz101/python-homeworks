import requests
from bs4 import BeautifulSoup
import sqlite3


def scrape_and_store_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

  
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()


    c.execute(
        """CREATE TABLE IF NOT EXISTS jobs (
                    job_title TEXT,
                    company_name TEXT,
                    location TEXT,
                    job_description TEXT,
                    application_link TEXT,
                    UNIQUE(job_title, company_name, location)
                 )"""
    )


    listings = soup.find_all("div", class_="card-content")

    for listing in listings:
        job_title = listing.find("h2", class_="title").text.strip()
        company_name = listing.find("h3", class_="company").text.strip()
        location = listing.find("p", class_="location").text.strip()

   
        description_tag = listing.find("div", class_="content")
        job_description = (
            description_tag.text.strip()
            if description_tag
            else "No description available"
        )

        application_link = listing.find("a", href=True)["href"]

        
        try:
            c.execute(
                """INSERT INTO jobs (job_title, company_name, location, job_description, application_link)
                         VALUES (?, ?, ?, ?, ?)""",
                (job_title, company_name, location, job_description, application_link),
            )
        except sqlite3.IntegrityError:
            pass 

    conn.commit()
    conn.close()

    print("Job data successfully stored in the database!")



scrape_and_store_jobs()
