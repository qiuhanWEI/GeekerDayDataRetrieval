# coding=utf-8
import linecache
import hashlib
import time

FILE_NUMBER = 100
ATTRIBUTES_NAME = ['name', 'phone', 'email']


def hash(string):
    a = hashlib.md5(string).hexdigest()
    a = int(a, 16) % FILE_NUMBER
    return a

def selectInDB(attributes):
    name = attributes['name']
    phone = attributes['phone']
    email = attributes['email']
    attributes = [name, phone, email]
    # print (attributes)
    result_list = []
    for index, attribute_name in enumerate(ATTRIBUTES_NAME):
        file_name = attribute_name + '/card_person_' + str(hash(attributes[index])) + '.data'
        print file_name
        lines = linecache.getlines(file_name)
        print (len(lines))
        for line in lines:
            if attributes[index] == line.split('\t')[index]:
                result_list.append(line)
    result_list = list(set(result_list))
    for i in range(len(result_list)):
    	result_dict = {}
        result_dict['name']=result_list[i].split('\t')[0]
        result_dict['phone']=result_list[i].split('\t')[1]
        result_dict['email']=result_list[i].split('\t')[2]
        result_dict['company']=result_list[i].split('\t')[3]
        result_dict['department']=result_list[i].split('\t')[4]
        result_dict['position']=result_list[i].split('\t')[5]
        result_list[i] = result_dict
    return result_list

def deleteInDB(attributes):
    name = attributes['name']
    phone = attributes['phone']
    email = attributes['email']
    attributes = [name, phone, email]
    print ('attr')
    print (attributes)
    for index, attribute_name in enumerate(ATTRIBUTES_NAME):
        # if attributes[index] == '':
        #     continue
        file_name = attribute_name + '/card_person_' + str(hash(attributes[index])) + '.data'
        lines = linecache.getlines(file_name)
        for index_c, line in enumerate(lines):
            if attributes[index] == line.split('\t')[index]:
            	lines.pop(index_c)
        print (file_name)
        with open(file_name, 'w') as f:
            f.writelines(lines)
    return 'success'

def updateInDB(attributes):
    name = attributes['name']
    phone = attributes['phone']
    email = attributes['email']
    company = attributes['company']
    department = attributes['department']
    position = attributes['position']
    attributes = [name, phone, email]

    singleInfo = name + '\t' + phone + '\t' + email +'\t' + company + '\t' + department + '\t' + position + '\n'
    for index, attribute_name in enumerate(ATTRIBUTES_NAME):
        file_name = attribute_name + '/card_person_' + str(hash(attributes[index])) + '.data'
        lines = linecache.getlines(file_name)
        for index_c, line in enumerate(lines):
            if attributes[index] == line.split('\t')[index]:
            	lines[index_c] = singleInfo
            	# result_list.append(singleInfo)
        f=open(file_name,'w')
       	f.writelines(lines)
       	f.close()
    return 'success'

def insertInDB(attributes):
    name = attributes['name']
    phone = attributes['phone']
    email = attributes['email']
    company = attributes['company']
    department = attributes['department']
    position = attributes['position']
    attributes = [name, phone, email]

    singleInfo = name + '\t' + phone + '\t' + email +'\t' + company + '\t' + department + '\t' + position + '\n'
    for index, attribute_name in enumerate(ATTRIBUTES_NAME):
        file_name = attribute_name + '/card_person_' + str(hash(attributes[index])) + '.data'
        lines = linecache.getlines(file_name)
        lines.append(singleInfo)
        f=open(file_name,'w')
       	f.writelines(lines)
       	f.close()
    return 'success'


if __name__ == '__main__':
    # print ('李沙童')

    # print (selectInDB({'name': '李沙童', 'phone': '', 'email': ''}))

    # print (deleteInDB({'name': '王良瑜', 'phone': '', 'email': ''}))

	print(insertInDB({'name': '张三', 'phone': '13863052614', 'email': 'aaokaeqweqwe@sonoscape.net','company': 'dasdasd', 'department': 'dsadasda', 'position': 'asdasda'}))
	# insertInDB({'name': '张三', 'phone': '13863052614', 'email': 'aaokaeqweqwe@sonoscape.net','company': 'dasdasd', 'department': 'dsadasda', 'position': 'asdasda'})
