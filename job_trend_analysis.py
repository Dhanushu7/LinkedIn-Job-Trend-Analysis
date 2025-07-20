
import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ---------------------------
# Setup
# ---------------------------
os.makedirs('datasets', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

# ---------------------------
# Step 1: Web Scraping
# ---------------------------
print("Starting job scraping...")

url = "https://www.indeed.com/jobs?q=data+analyst&l="
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for job_card in soup.find_all('div', class_='job_seen_beacon'):
    title = job_card.find('h2').text.strip() if job_card.find('h2') else 'N/A'
    location = job_card.find('div', class_='companyLocation').text.strip() if job_card.find('div', class_='companyLocation') else 'N/A'
    skills = title.lower().replace('-', ' ').split()
    jobs.append({'title': title, 'location': location, 'skills': skills})

df = pd.DataFrame(jobs)
df.to_csv('datasets/raw_jobs.csv', index=False)
print(f"Scraping complete. {len(df)} jobs saved to datasets/raw_jobs.csv")

# ---------------------------
# Step 2: Trend Analysis Visuals
# ---------------------------
print("Generating trend analysis visuals...")

all_skills = []
for skill_list in df['skills']:
    if isinstance(skill_list, str):
        skill_list = eval(skill_list)
    all_skills.extend(skill_list)

skill_counts = pd.Series(all_skills).value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=skill_counts.values, y=skill_counts.index, palette='viridis')
plt.title('Top 10 Skills (from Job Titles)')
plt.xlabel('Number of Jobs')
plt.ylabel('Skills')
plt.tight_layout()
plt.savefig('outputs/skill_demand_chart.png')
plt.show()

# ---------------------------
# Step 3: Skill vs Role Matrix
# ---------------------------
print("Creating skill vs role matrix...")

skills_expanded = df.explode('skills')
matrix = pd.crosstab(skills_expanded['title'], skills_expanded['skills'])

top_skills = skill_counts.index.tolist()
matrix = matrix[top_skills]

matrix.to_excel('outputs/skill_vs_role_matrix.xlsx')

# ---------------------------
# Step 4: Job Demand Recommendations
# ---------------------------
print("Generating job demand recommendations...\n")

top_5_skills = skill_counts.head(5).index.tolist()
top_locations = df['location'].value_counts().head(5)

print("Recommended Skills to Learn (Top 5):")
for idx, skill in enumerate(top_5_skills, 1):
    print(f"{idx}. {skill}")

print("\nTop Locations Hiring:")
for idx, (loc, count) in enumerate(top_locations.items(), 1):
    print(f"{idx}. {loc} ({count} jobs)")

with open('outputs/job_recommendations.txt', 'w') as f:
    f.write("Recommended Skills to Learn (Top 5):\n")
    for idx, skill in enumerate(top_5_skills, 1):
        f.write(f"{idx}. {skill}\n")
    f.write("\nTop Locations Hiring:\n")
    for idx, (loc, count) in enumerate(top_locations.items(), 1):
        f.write(f"{idx}. {loc} ({count} jobs)\n")

df.to_excel('outputs/cleaned_jobs.xlsx', index=False)

print("\nProject complete.")
