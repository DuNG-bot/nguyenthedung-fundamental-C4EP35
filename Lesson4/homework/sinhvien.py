sv1={
    'name':'Nguyen Dinh A',
    'age':19,
    'add':'Thanh Xuan',
    'Math':7.4,
    'Physics':4.9,
    'Chem':9.2,
    'Phone':['0912439530','0835838123','0934581928'] 
}
sv2={
    'name':'Ngo Dinh B',
    'age':20,
    'add':'Cau Giay',
    'Math':10.0,
    'Physics':3.4,
    'Chem':0.5,
    'Phone':['0912094330','0891028123','0934943728']
}
sv3={
    'name':'Nguyen Tan C',
    'age':19,
    'add':'Ba Dinh',
    'Math':7.8,
    'Physics':6.2,
    'Chem':9.2,
    'Phone':['091924859','0835847633','0998347928']
}
sv4={
    'name':'Tran Van D',
    'age':21,
    'add':'Tay Ho',
    'Math':5.5,
    'Physics':4.8,
    'Chem':2.1,
    'Phone':['0912423430','0894738123','0934581927']
}
sv5={
    'name':'Ly Nam F',
    'age':19,
    'add':'Hai Ba Trung',
    'Math':7.1,
    'Physics':4.3,
    'Chem':8.7,
    'Phone':['0912433948','0833338123','0934581000']
}

people=[]
people.append(sv1)
people.append(sv2)
people.append(sv3)
people.append(sv4)
people.append(sv5)

for i in people:
    diemTB = (i['Math']+i['Physics']+i['Chem'])/3
    print('Diem trung binh cua',i['name'],'la:',diemTB)
bezt = people[0]['Math']

for v in range (len(people)):
    if bezt < people[v]['Math']:
        bezt = people[v]['Math']

for s in range (len(people)):
    if bezt == people[s]['Math']:
        print('Thi sinh co diem toan cao nhat la:',people[s]['name'])

phone = input('Nhap so dien thoai: ')

for l in people:
    if phone in l['Phone']:
        print('Ten cua ng do la:',l['name'])