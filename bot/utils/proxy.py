import requests

TOKEN = '6424697766:AAEb6104bqGTl_GLQkRN9amSAyhDhj0PEWM'

url = f"https://api.telegram.org/bot{TOKEN}/getMe"

protocol = 'mtp'
host = 'exp.proxy.digitalresistance.dog'
port = 443
secret = '7tQdjNmPALIE6YAJmOz4Mi53d3cuZ29vZ2xlLmNvbQ'

proxy = {
    'http': f"mtp://{secret}@{host}:{port}",
    'https': f"mtp://{secret}@{host}:{port}"
}

try:
    response = requests.get(url, proxies=proxy)
    if response.status_code == 200:
        print("Прокси сервер работает с Telegram.")
    else:
        print("Прокси сервер не работает с Telegram.")
except Exception as e:
    print(f"Ошибка при подключении к Telegram через прокси: {e}")
