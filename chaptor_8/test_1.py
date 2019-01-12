if __name__ == '__main__':
    for i in range(0, 100):
        print i
        if i % 2 == 1:
            continue
        print "hello", i
        if i > 50:
            print "Breaking! JOJO!"
            break
