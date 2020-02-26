import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '0101steven',
    database = 'world'
)

city= dbku.cursor(dictionary = True)
city.execute('select * from city')
datajsoncity = list(city)

import json
with open ('world_city.json','w') as myjson :
    json.dump(datajsoncity, myjson)

country= dbku.cursor(dictionary = True)
country.execute('select * from country')
datajsoncountry = list(country)

import json
with open ('world_country.json','w') as myjson :
    json.dump(datajsoncountry, myjson)

countrylanguage= dbku.cursor(dictionary = True)
countrylanguage.execute('select * from countrylanguage')
datajsoncountrylanguage = list(countrylanguage)

import json
with open ('world_countrylanguage.json','w') as myjson :
    json.dump(datajsoncountrylanguage, myjson)
