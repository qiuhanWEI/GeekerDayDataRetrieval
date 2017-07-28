#coding=utf-8

import linecache
import hashlib

# 先在当前目录建立好name、phone、email三个文件夹

def hash(string):
    a = hashlib.md5(string).hexdigest()
    a = int(a,16)%100
    return a

content = linecache.getlines('card_person.data')

for k in range(100):
    print('name:' + str(k))
    f = open('name/card_person_' + str(k) + '.data', 'w')
    for i in content:
        j = hash(i.split('\t')[0])%100
        if j == k:
            f.write(i)
    f.close()

for k in range(100):
    print('phone:' + str(k))
    f = open('phone/card_person_' + str(k) + '.data', 'w')
    for i in content:
        j = hash(i.split('\t')[1])%100
        if j == k:
            f.write(i)
    f.close()

for k in range(100):
    print('email:' + str(k))
    f = open('email/card_person_' + str(k) + '.data', 'w')
    for i in content:
        j = hash(i.split('\t')[2])%100
        if j == k:
            f.write(i)
    f.close()