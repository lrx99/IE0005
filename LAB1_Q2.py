visit= open('C://Users//LRXCalvin//Desktop//visitors.txt')
block = open('C://Users//LRXCalvin//Desktop//blocklist.txt')

visitors, blocklist = visit.read().split(), block.read().split()
a, b = set(), set()

for x in visitors:
    a.add(x)
for y in blocklist:
    b.add(y)

print('Visitors: ' + str(a))
print('Denied access: ' + str(a&b))

visit.close()
block.close()