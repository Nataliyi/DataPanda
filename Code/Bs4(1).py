import requests as req
from bs4 import BeautifulSoup

# Работаем c BeautifulSoup(поиск по тегам)

resp = req.get('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
soup = BeautifulSoup(resp.text, 'html.parser') # делаем суп
table = soup.find_all('td')
m = 0
for i in table:
    m += int(i.text.strip())
