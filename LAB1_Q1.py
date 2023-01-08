try:
    blocklist = open('C://Users//LRXCalvin//Desktop//blocklist.txt')
except FileNotFoundError:
    print('Wrong Directory')
print(blocklist.read())
blocklist.close()