from bs4 import BeautifulSoup
import requests

url = 'http://digidb.io/digimon-list/'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
findtable =str(soup.find('table',id='digiList'))
soup = BeautifulSoup(findtable,'html.parser' )

findno = soup.find_all('td',width='5%')
datano = []
for i in findno :
    datano.append(i.text.replace('\xa0', ''))
# print(datano)

dataimg =[]
for img in soup.find_all('img'):
    dataimg.append(img.get('src'))
# print(dataimg)

findname = soup.find_all('td',width='21%')
dataname = []
for i in findname :
    dataname.append(i.text.replace('\xa0 ', ''))
# print(dataname)

findstage = soup.find_all('td',width='9%')
datastage = []
for i in findstage :
    datastage.append(i.text.replace('\xa0 ', ''))
# print(datastage)

findtam = soup.find_all('td',width='7%')
datatype = []
datamemory = []
dataattribute = []
temp = []
for i in range(len(findtam)) :
    if (i+1) % 3 == 0 :
        datamemory.append(findtam[i].text.replace('\xa0 ', ''))
    else :
        temp.append(findtam[i].text.replace('\xa0 ', ''))
    
# print(datamemory)

for i in range(len(temp)) :
    if (i+1) % 2 == 0 :
        dataattribute.append(temp[i])
    else :
        datatype.append(temp[i])

# print(dataattribute)
# print(datatype)

findeqslot = soup.find_all('td',width='8%')
dataeqslot = []
for i in findeqslot :
    dataeqslot.append(i.text.replace('\xa0', ''))
# print(dataeqslot)

indexhp = [8]
datahp = []
hp = 8
indexsp = [9]
datasp = []
sp = 9
indexatk = [10]
dataatk = []
atk = 10
indexdef = [11]
datadef = []
def_ = 11
indexint = [12]
dataint = []
int_ = 12
indexspd = [13]
dataspd = []
spd = 13

findstat = soup.find_all('td')

for i in findstat :
    hp += 13
    sp += 13
    atk += 13
    int_ += 13
    def_ += 13
    spd += 13
    indexhp.append(hp)
    indexsp.append(sp)
    indexatk.append(atk)
    indexdef.append(def_)
    indexint.append(int_)
    indexspd.append(spd)

for i in range(len(findstat)) :
    if i+1 in indexhp :
        datahp.append(findstat[i].text)
    elif i+1 in indexsp :
        datasp.append(findstat[i].text)
    elif i+1 in indexatk :
        dataatk.append(findstat[i].text)
    elif i+1 in indexdef :
        datadef.append(findstat[i].text)
    elif i+1 in indexint :
        dataint.append(findstat[i].text)
    elif i+1 in indexspd :
        dataspd.append(findstat[i].text)

findheader=soup.find_all('th')
dataheader = []
for i in findheader :
    dataheader.append(i.text)
dataheader.append('img')

data = []
for i in range(len(dataimg)) :
    data.append({
        dataheader[0] : datano[i] ,
        dataheader[1] : dataname[i] ,
        dataheader[2] : datastage[i] ,
        dataheader[3] : datatype[i] ,
        dataheader[4] : dataattribute[i] ,
        dataheader[5] : datamemory[i] ,
        dataheader[6] : dataeqslot[i] ,
        dataheader[7] : datahp[i] ,
        dataheader[8] : datasp[i] ,
        dataheader[9] : dataatk[i] ,
        dataheader[10] : datadef[i] ,
        dataheader[11] : dataint[i] ,
        dataheader[12] : dataspd[i] ,
        dataheader[13] : dataimg[i] ,
    })

import xlsxwriter
book = xlsxwriter.Workbook("digimon.xlsx")
sheet = book.add_worksheet("Database Digimon")
row = 1
col = 0
for i in dataheader : 
    sheet.write(0,col,i)
    col += 1
col = 0
for i in range(0,len(data)) :
    for j in data[i]:
        sheet.write(row, col, data[i][j])
        col += 1
    col = 0
    row += 1
book.close()