def day2a(file = "Input/2A.txt"):
    commands = []
    with open(file) as f:
        lines = f.readlines()
        x = 0
        d = 0
        for i in lines:
            command = i.strip('\n').split(' ')
            dist = int(command[1])
            dir = command[0]
            if dir == "forward":
                x += dist
            elif dir == "up":
                d += -dist
            elif dir == "down":
                d += dist

    print (x * d)
        
def day2b(file = "Input/2A.txt"):
    with open(file) as f:
        lines = f.readlines()
        x = 0
        d = 0
        a = 0
        for i in lines:
            command = i.strip('\n').split(' ')
            dist = int(command[1])
            dir = command[0]
            if dir == "forward":
                x += dist
                d += a * dist
            elif dir == "up":
                a += -dist
            elif dir == "down":
                a += dist
            #print(x,d,a)
        print(x * d)