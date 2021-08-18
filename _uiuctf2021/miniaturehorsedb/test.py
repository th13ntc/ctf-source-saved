for i in range(0, 100000):
    if (len(chr(i)) == 1 and len(chr(i).lower()) == 2):
        print(str(i) + " " + chr(i) + " " + chr(i).lower())
