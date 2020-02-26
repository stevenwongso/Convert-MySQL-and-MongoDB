import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '***',
    database = 'world'
)

city= dbku.cursor(dictionary = True)
city.execute('select * from city')
datacsvcity = list(city)
keys = list(datacsvcity[0].keys())
kolom1= dict(zip(keys,keys))

import csv
with open('world_city.csv','w',newline='') as mycsv :
    writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = keys)
    writer.writerows([kolom1])
    writer.writerows(datacsvcity)

country= dbku.cursor(dictionary = True)
country.execute('select * from country')
datacsvcountry = list(country)
keys = list(datacsvcountry[0].keys())
kolom1= dict(zip(keys,keys))

import csv
with open('world_country.csv','w',newline='') as mycsv :
    writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = keys)
    writer.writerows([kolom1])
    writer.writerows(datacsvcountry)

countrylanguage= dbku.cursor(dictionary = True)
countrylanguage.execute('select * from countrylanguage')
datacsvcountrylanguage = list(countrylanguage)
keys = list(datacsvcountrylanguage[0].keys())
kolom1= dict(zip(keys,keys))

import csv
with open('world_countrylanguage.csv','w',newline='') as mycsv :
    writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = keys)
    writer.writerows([kolom1])
    writer.writerows(datacsvcountrylanguage)

