#!/usr/bin/python
# 
# with open(in_filename) as in_file, open(out_filename, 'a') as out_file:
#    for line in in_file:
#      print('1')
#      out_file.write(parsed_line)
     
import myclass
a = myclass.Human(180,80)
# b = myclass.Human(170,70)
# print(a+b)
# print(a.height,a.weight)
# print(b.height,b.weight)
# #a+=b
# b+=a
# print(a.height,a.weight)
# print(b.height,b.weight)

print(a._height,a._weight)
#print(a.BMI())