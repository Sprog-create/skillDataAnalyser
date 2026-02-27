
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_jobs(keyword, location, pages=5):
    jobs = []

    for page in range(pages):
        url = f"https://remoteok.com/api"  # RemoteOK has a free public API, great for starting
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()

        for job in data[1:]:  # first item is metadata
            jobs.append({
                "title": job.get("position", ""),
                "company": job.get("company", ""),
                "description": job.get("description", ""),
                "tags": job.get("tags", [])
            })

    df = pd.DataFrame(jobs)
    df.to_csv("data/raw/jobs.csv", index=False)
    return df


scrape_jobs("python developer", "remote")