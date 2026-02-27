import pandas as pd
from bs4 import BeautifulSoup
import os

os.makedirs("data/processed", exist_ok=True)


def clean_description(text):
    if not isinstance(text, str):
        return ""
    # remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text(separator=" ").lower()


SKILLS = [
    "python", "sql", "machine learning", "deep learning", "pandas",
    "numpy", "tensorflow", "pytorch", "flask", "fastapi", "docker",
    "kubernetes", "aws", "react", "javascript", "java", "excel",
    "power bi", "tableau", "nlp", "opencv", "git", "mongodb",
    "postgresql", "django", "nodejs", "typescript", "figma",
    "spark", "hadoop", "airflow", "redis", "graphql", "rust",
    "golang", "swift", "kotlin", "flutter", "azure", "gcp"
]


def extract_skills(text):
    return [skill for skill in SKILLS if skill in text]


def process_jobs():
    df = pd.read_csv("data/raw/jobs.csv")
    df["clean_description"] = df["description"].apply(clean_description)
    df["skills_found"] = df["clean_description"].apply(extract_skills)
    df.to_csv("data/processed/jobs_processed.csv", index=False)
    print(f"Processed {len(df)} jobs!")

    # preview
    print("\nSample cleaned description:")
    print(df["clean_description"][0][:300])
    print("\nSkills found in first job:", df["skills_found"][0])


process_jobs()