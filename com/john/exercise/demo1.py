

for le in 'python':
    if le == 'h':
        pass
        print 'pass block'
    print 'now',le

print 'end'

try:
    fh = open('t.txt', 'w')
    fh.write('ceshi')
except IOError:
    print "cant find file"
else:
    print 'write done'
    fh.close()