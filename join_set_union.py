csv = 'Eric,Don Eric,Rick,Rex:Rebecca;Romulo,Randall'

print(csv)
friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
print('replace', csv.replace(';',',').replace(':',',').split(','))

# set.intersection
# set.difference
# set.union
# set.symmetric_difference or x ^ y
# example = list(set(example_list))