import requests
import pandas as pd
from openpyxl import Workbook

# API URL
api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

# Fetch the data from the API
response = requests.get(api_url)
# Check the API response status and process the data
if response.status_code == 200:
    jobs_data = response.json()
else:
    print(f"Failed to fetch data from API. Status code: {response.status_code}")
    jobs_data = []  # Use an empty list if the response is not successful

# Generalized function to count jobs by a key (e.g., Technology or Location)
def get_number_of_jobs(key, value):
    return value, sum(1 for job in jobs_data if value.lower() in job[key].lower())

# Example: Get number of jobs for specific Technology and Location
print(get_number_of_jobs("Key Skills", "Python"))
print(get_number_of_jobs("Location", "Los Angeles"))

# List of technologies to analyze
technologies = [
    "Data Analysis", "Python", "Java", "C++", "SQL", "JavaScript",
    "Machine Learning", "Data Science", "Cloud Computing", "AWS",
    "DevOps", "Cybersecurity", "Artificial Intelligence", "Big Data",
    "Kubernetes", "Docker"
]

# Create a new workbook
workbook = Workbook()
# Select the active worksheet
worksheet = workbook.active

# Create a DataFrame for technologies and their job counts
technology_job_counts = []

for tech in technologies:
    tech_name, job_count = get_number_of_jobs("Key Skills", tech)
    technology_job_counts.append((tech_name, job_count))

df_jobs = pd.DataFrame(technology_job_counts, columns=["Technology", "Number of Job Postings"])

# Save the data to an Excel file
output_file = "job-postings.xlsx"
df_jobs.to_excel(output_file, index=False)

print(f"Job postings by technology saved to {output_file}.")

# Programming languages to analyze
languages = [
    "C", "C#", "C++", "Java", "JavaScript", "Python",
    "Scala", "Oracle", "SQL Server", "MySQL Server",
    "PostgreSQL", "MongoDB"
]


# Function to count job postings for a specific language
def get_number_of_jobs(language):
    return language, sum(1 for job in jobs_data if language.lower() in job["Key Skills"].lower())

# Collect job counts for each language
language_job_counts = [get_number_of_jobs(lang) for lang in languages]

# Convert the results to a DataFrame
df_languages = pd.DataFrame(language_job_counts, columns=["Language", "Number of Job Postings"])

# Save the results to an Excel file
output_file = "language_job_postings.xlsx"
df_languages.to_excel(output_file, index=False)

print(f"Job postings for programming languages saved to {output_file}.")