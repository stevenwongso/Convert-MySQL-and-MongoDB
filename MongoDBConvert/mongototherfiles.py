# import pymongo
# urldb = "mongodb://127.0.0.1:27017"
# mongoku = pymongo.MongoClient(urldb)
# dbku = mongoku['ptabc']
# colku = dbku['pegawai']

# data = {'nama':'Hadi','kota':'Bandung'}
# send = colku.insert_one(data)
# print(send.inserted_id) # untuk tau id data baru yang di insert

# data = [
#     {'nama': 'Zizi', 'kota': 'Kediri'},
#     {'nama': 'Zizi', 'kota': 'Surabaya'},
#     {'nama': 'Zizi', 'kota': 'Sleman'}
# ]
# insert data
# kirim = colku.insert_many(data)
# print(kirim.inserted_ids)

# colku.delete_one({'nama':'Hadi'})

# hapus = colku.delete_one({'nama':'Zizi'})
# print(hapus.deleted_count)

# hapus = colku.delete_many({'nama':'Zizi'})
# print(hapus.deleted_count)

# hapus = colku.delete_many({})
# print(hapus.deleted_count)

# data = [
#     {'nama': 'Andi', 'kota': 'Kediri'},
#     {'nama': 'Budi', 'kota': 'Surabaya'},
#     {'nama': 'Caca', 'kota': 'Sleman'}
# ]
# kirim = colku.insert_many(data)
# print(kirim.inserted_ids)

# colku.update_one(
#     {'nama':'Caca'},
#     {'$set': {'kota': 'Yogyakarta'}}
# )

# colku.update_many(
#     {},
#     {'$set': {'usia': 25}}
# )


'''CONVERT FILE'''
'''mongodb => json'''
# import json

# data = list(colku.find())
# for i in range(len(data)):
#     data[i]['_id'] = str(data[i]['_id'])

# with open ('mongodbku.json','w') as myjson :
#     json.dump(data, myjson)

'''mongodb => csv'''
# import csv 

# data = list(colku.find())
# for i in range(len(data)):
#     data[i]['_id'] = str(data[i]['_id'])

# with open('mongodbku.csv','w',) as mycsv :
#     writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = ['_id','nama','kota','usia'])
#     writer.writerows([{'_id':'_id', 'nama':'nama', 'kota':'kota','usia':'usia'}])
#     writer.writerows(data)

'''mongodb => excel'''
# import xlsxwriter

# book = xlsxwriter.Workbook("mongodbku.xlsx")
# sheet = book.add_worksheet("Database")

# data = list(colku.find())
# for i in range(len(data)):
#     data[i]['_id'] = str(data[i]['_id'])

# row = 1
# for i in range(len(data)):
#     sheet.write(row, 0, data[i]['_id'])
#     sheet.write(row, 1, data[i]['nama'])
#     sheet.write(row, 2, data[i]['kota'])
#     sheet.write(row, 3, data[i]['usia'])
#     row += 1

# book.close()
