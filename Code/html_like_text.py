from urllib.request import urlopen
import re

# Обработка HTML как текста

html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('UTF-8')
s = str(html)
m = re.findall(r'\<code>(\w+)<\/code\>', s)
a = set()
for i in m:
    r = m.count(i)
    if r > 1:
        a.add(i)
    else:
        continue
print(*(sorted(a)))



