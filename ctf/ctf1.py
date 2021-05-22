with open("ctf/assets/ctf1.dat") as f:
    lines = f.readlines()
    counter = 0
    for line in lines:
        if line.count("0") % 3 == 0 or line.count("1") % 2 == 0:
            counter += 1
    print(counter)
