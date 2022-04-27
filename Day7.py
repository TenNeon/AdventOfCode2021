
def insert_item(items, i, count = 1):
    if i in items:
        items[i] += count
    else:
        items[i] = count
    return items


def calculate_cost(crabs,min,max,i):
    # cost is sum of distances to cell
    cost = 0
    keys = crabs.keys();
    for key in keys:
        dist = abs(key-i)
        cost += dist * crabs[key]  
    return cost

def crabulate_cost(crabs,min,max,i):
     # cost is sum of distances to cell
    cost = 0
    keys = crabs.keys();
    for key in keys:
        dist = abs(key-i)
        # Sum_n = n*(n+1)/2
        fuel_cost = dist * (dist+1) // 2
        cost += fuel_cost * crabs[key]  
    return cost

    
def make_dict(file):
    crabs_list = []
    with open(file) as f:
        lines = f.readlines()
        crabs_str = lines[0].split(",")
        for i in crabs_str:
            crabs_list.append(int(i))
            
    crabs_list.sort()
    min = crabs_list[0]
    max = crabs_list[-1]
    
    crabs = {}
    for i in crabs_list:
        crabs = insert_item(crabs,int(i),1)
    
    return crabs, min, max
    
def partA(file = "Input/7A.txt"):
    if file == "test":
        file = "Input/7A_test.txt"

        

    crabs, min, max = make_dict(file)
    
    costs = []
    for i in range(min,max+1):
      costs.append(int(calculate_cost(crabs,min,max,i)))
    
    min = 9999999
    for i in costs:
        min = i if i < min else min
        
    print (min)
    
def partB(file = "Input/7A.txt"):
    if file == "test":
        file = "Input/7A_test.txt"

    crabs, min, max = make_dict(file)
    
    costs = []
    for i in range(min,max+1):
      costs.append(crabulate_cost(crabs,min,max,i))
      
    print(costs)
    min = 9999999999
    for i in costs:
        min = i if i < min else min
        
    print (min)