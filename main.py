from bs4 import BeautifulSoup
import requests
import time
from pathlib import Path


# SCRAPING LOCALLY
# with open('index.html', 'r') as html_file:
#     content = html_file.read()
#     # instatiate BS
#     soup = BeautifulSoup(content, 'lxml')
#     # Grab all h5 elements and output text attribute

#     # You can apparently just grab everything as a child attribute of
#     # any parent element... it's a little wild west but if it's consistent
#     # it's really powerful
#     cards = soup.find_all('div', {'class': 'card'})
#     for card in cards:
#         print(f"{card.h5.text}: {card.a.text.split(' ')[-1]}")

# SCRAPING REMOTELY
# html_text = requests.get(
#     'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# soup = BeautifulSoup(html_text, 'lxml')
# items = soup.find_all('h3', {'class': 'joblist-comp-name'})
# for item in items:
#     print(item.text)


# jobs = soup.find_all('h3', {'class': 'joblist-comp-name'})

# for title in section_titles:
#     print(title)
# for job in jobs:
#     print(job.text)

# print(f'{len(jobs)} jobs')


def print_listings(count):
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', {'class': 'clearfix job-bx wht-shd-bx'})
    with open(Path(__file__).parent / f'posts/file{count}.txt', 'w') as file:

        for index, job in enumerate(jobs):
            company_name = job.find('h3').text.strip()

    # print(company_name.text.strip(), skills.text.strip())
            skills = ' '.join([skill.strip() for skill in job.find(
                'span', {'class': 'srp-skills'}).text.split()])
            job_link = job.find('a')['href']
            file.write(f'Company Name: {company_name.upper()}\n')
            file.write(f'Required Skills: {skills}\n')
            file.write(f'Job Link: {job_link}\n\n')
            print(f'File saved: Iteration {index}')


if __name__ == '__main__':
    count = 1
    while True:
        print_listings(count)
        count += 1
        time_to_wait = 10
        print(f'Waiting {time_to_wait} minutes... ')
        time.sleep(time_to_wait * 60)
