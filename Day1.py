
# 1602
def Day1A():
    with open('Input/1A.txt') as f:
        lines = f.readlines()
    
        count = 0
        print(lines[0].strip(), "N/A - no previous measurement)")
        for i in range(1, len(lines)):
            current = int(lines[i].strip())
            prev = int(lines[i-1].strip())
            if current > prev:
                count += 1
            print("{} ({}) {}".format(current, "increased" if current > prev else "decreased", count))
        print(count)
        
# 1995
def Day1B():
    with open('Input/1A.txt') as f:
        lines = f.readlines()
        
        count = 0
        
        for i in range(0, len(lines)-3):
            A = int(lines[i].strip())
            D = int(lines[i+3].strip())
            window1 = A
            window2 = D
            count += 1 if window2 > window1 else 0
            
        print(count)