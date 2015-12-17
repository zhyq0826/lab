
def counter(start_at=0):
    count = start_at
    while 1:
        # other = yield foo,
        # when a value is sent to me,
        # set other to that value."
        # You can "send" values to a generator using the generator's send method.
        print 'before yield count', count
        val = yield count
        print 'after yield val', val
        print 'after yield count', count
        if val is not None:
            count = val
        else:
            count += 1

def main1():
    c = counter(5)
    print '---one call---'
    print c.next()    #
    print '---one call---'
    print c.next()
    print '---one call---'
    # both sends a value to the generator and returns the value yielded by the generator
    # (mirroring how yield works from within the generator function
    print c.send(10)
    print '---one call---'
    print c.next()
    print c.send(None)
    print c.next()

if __name__ == '__main__':
    main1()