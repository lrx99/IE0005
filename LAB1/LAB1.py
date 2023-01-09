#Q1
try:
    blocklist = open('blocklist.txt', 'r+')
except FileNotFoundError:
    print('Wrong Directory')
d = set(blocklist.read().split())
for x in d:
    print(x)

#Q2
visitors = open('visitors.txt')
c = set(visitors.read().split())

print(len(c))

for y in c&d:
    print(y)

#Q3
offender = {'alice@wonderland.co.uk'}

for z in offender-d:
    blocklist.write('\n' + z)

blocklist.close()
visitors.close()