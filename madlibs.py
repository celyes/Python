import random

random_list = []
length = 20
while len(random_list) < 20:
    random_list.append(random.randint(0,10))

count_list = [0]*11
index = 0
count = 0
while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number]+1
    index = index + 1
print random_list
print 'Number | Occurrences'
num = 0
while num < len(count_list):
    num_spaces = len("Number")
    print ' ' * (num_spaces - 1 ) + str(num) + ' | ' + str(count_list[num])
    num += 1