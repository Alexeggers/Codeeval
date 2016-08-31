for row in (("{:>4}".format(str(y*x)) for x in range(1,13)) for y in range(1,13)):
    print("".join(row))
