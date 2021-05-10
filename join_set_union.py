csv = 'Eric,Don Eric,Rick,Rex:Rebecca;Romulo,Randall'
import sys


print(csv)
friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
print('replace', csv.replace(';',',').replace(':',',').split(','))

# set.intersection
# set.difference
# set.union
# set.symmetric_difference or x ^ y
# example = list(set(example_list))

for i in range(10):
    for j in range(10):
        print(j)    
    print("Outer break will be executed")    
    break 

