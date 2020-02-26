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
dataexcelcity = list(city)
baris0 = list(dataexcelcity[0].keys())

import xlsxwriter
book = xlsxwriter.Workbook("world_city.xlsx")
sheet = book.add_worksheet("city")
row = 1
col = 0
for i in baris0 : 
    sheet.write(0,col,i)
    col += 1
col = 0
for i in range(0,len(dataexcelcity)) :
    for j in dataexcelcity[i]:
        sheet.write(row, col, dataexcelcity[i][j])
        col += 1
    col = 0
    row += 1
book.close()

country= dbku.cursor(dictionary = True)
country.execute('select * from country')
dataexcelcountry = list(country)
baris0 = list(dataexcelcountry[0].keys())

import xlsxwriter
book = xlsxwriter.Workbook("world_country.xlsx")
sheet = book.add_worksheet("country")
row = 1
col = 0
for i in baris0 : 
    sheet.write(0,col,i)
    col += 1
col = 0
for i in range(0,len(dataexcelcountry)) :
    for j in dataexcelcountry[i]:
        sheet.write(row, col, dataexcelcountry[i][j])
        col += 1
    col = 0
    row += 1
book.close()

countrylanguage= dbku.cursor(dictionary = True)
countrylanguage.execute('select * from countrylanguage')
dataexcelcountrylanguage = list(countrylanguage)
baris0 = list(dataexcelcountrylanguage[0].keys())

import xlsxwriter
book = xlsxwriter.Workbook("world_countrylanguage.xlsx")
sheet = book.add_worksheet("countrylanguage")
row = 1
col = 0
for i in baris0 : 
    sheet.write(0,col,i)
    col += 1
col = 0
for i in range(0,len(dataexcelcountrylanguage)) :
    for j in dataexcelcountrylanguage[i]:
        sheet.write(row, col, dataexcelcountrylanguage[i][j])
        col += 1
    col = 0
    row += 1
book.close()