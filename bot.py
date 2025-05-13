import requests
from bs4 import BeautifulSoup
import json

LOGIN_URL = "https://app.dataannotation.tech/users/sign_in"
PROJECTS_URL = "https://app.dataannotation.tech/workers/projects"

session = requests.Session()

cookie = ""

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://app.dataannotation.tech/users/sign_in',
    'sec-ch-ua': '"Chromium";v="135", "Not-A.Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'cookie': cookie,
}

res = requests.get('https://app.dataannotation.tech/workers/projects', headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

# Step 3: Find the <div> with project data
target_div = soup.find("div", id="workers/WorkerProjectsTable-hybrid-root")
data_props = target_div.get("data-props")

# Step 4: Decode JSON and extract projects
decoded = json.loads(data_props)
projects = decoded["dashboardMerchTargeting"]["projects"]

# Print project names
for project in projects:
    print(f"{project})")
