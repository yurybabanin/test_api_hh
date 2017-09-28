import urllib.request, json, sqlite3


with urllib.request.urlopen('https://api.hh.ru/areas/1202') as url2:
    data1 = json.loads(url2.read().decode())
con = sqlite3.connect('database.db', timeout=10)
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS citis(id INTEGER UNIQUE,name TEXT)')
con.commit()
d = []
i = 0
while i < len(data1['areas']):
    d.insert(i, [data1['areas'][i]['id'], data1['areas'][i]['name']])
    i +=1

cur.execute("SELECT * FROM citis")
res = cur.fetchall()

if len(data1['areas']) != len(res):
    cur.executemany("INSERT INTO citis(id, name) VALUES (?, ?)", d)
    con.commit()


# print(cur.fetchall())
con.close()
url = 'https://api.hh.ru/vacancies?area=4&text=Java&per_page=500'

with urllib.request.urlopen(url) as url1:
    data = json.loads(url1.read().decode())

# print(data['items'][1]['name'])


print(len(data['items']))
i=0
while i < len(data['items']):
    print(data['items'][i]['name'])
    # print('\n')
    # print(' ')
    i = i + 1