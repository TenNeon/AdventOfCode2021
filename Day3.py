import collections
import math

def count_bits(input):
    bits = {}
    for line in input:
        for j in range(0, len(line)-1 ):
            # j is an index
            if j in bits.keys():
                bits[j] += 1 if line[j] == "1" else 0
            else:
                bits[j] = 1 if line[j] == "1" else 0
    return bits
   
def most_common_in_position(lines, position_index):
    count0 = 0
    count1 = 0
    lineCount = len(lines)
    threshold = lineCount // 2 if lineCount % 2 == 1 else lineCount//2 + 1

    for line in lines:
        if  line[position_index] == "1":
            count1 += 1
        else:
            count0 +=1
         
        if count0 >= threshold:
           return 0
        if count1 >= threshold:
           return 1
            
    return "equal"

def only_x(lines,i,x):
    result = []
    for line in lines:
        if int(line[i]) == int(x):
            result.append(line)
    return result

def o2_number(lines, i = 0):
    most_common_i = most_common_in_position(lines,i)
    most_common_i = 1 if most_common_i == "equal" else most_common_i
    #print("most common in position",i, most_common_i)
    lines = only_x(lines,i,most_common_i)
    #print(lines)
    if len(lines) > 1:
        return o2_number(lines, i + 1)
    else:
        return int(lines[0].strip('\n'),2)
    
def co2_number(lines, i = 0):
    most_common_i = most_common_in_position(lines,i)
    most_common_i = 1 if most_common_i == "equal" else most_common_i
    least_common_i = 0 if most_common_i == 1 else 1
    #print("least common in position",i, least_common_i)
    lines = only_x(lines,i,least_common_i)
    #print(lines)
    if len(lines) > 1:
        return co2_number(lines, i + 1)
    else:
        return int(lines[0].strip('\n'),2)

def day3a(file = "Input/3A.txt"):

    with open(file) as f:
        lines = f.readlines()
        threshold = math.ceil(len(lines) / 2)
        bits = count_bits(lines)
          
        print(bits, threshold)
        
def day3b(file = "Input/3A.txt"):
    with open(file) as f:
        lines = f.readlines()
        o2 = o2_number(lines)
        co2 = co2_number(lines)
        print("O2: ",o2)
        print("CO2: ",co2)
        print(o2*co2)