block = open('C://Users//LRXCalvin//Desktop//blocklist.txt', 'a')

offender = 'alice@wonderland.co.uk'

block.write('\n' + offender)

block.close()