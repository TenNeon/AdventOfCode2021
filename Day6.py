


def partA(file = "Input/6A.txt", days = 256):
    if file == "test":
        file = "Input/6A_test.txt"
    fish_list = []
    with open(file) as f:
        lines = f.readlines()[0]
        fish_list = lines.split(',')
        
    fish = {}

    
    
    for i in fish_list:
        fish = insert_fish(fish,int(i),1)
        
    print(0, fish)
    for i in range(1,days+1):
        fish = fishLife(fish)
        print(i, fish)
        
    countFish(fish)

def countFish(fish):
    count = 0
    for i in fish:
        count += fish[i]
        
    print("count", count)


def insert_fish(fish, i, count = 1):
    if i in fish:
        fish[i] += count
    else:
        fish[i] = count
    return fish

def fishLife(fish):
    keys = fish.keys();
    new_fish = {}
    
    for i in keys:
        if i == 0:
            # reproduce push as 7
            # new fish is 8
            new_fish = insert_fish(new_fish, 6, fish[i])
            new_fish = insert_fish(new_fish, 8, fish[i])
        else:
            # decrement, push to new_fish as that value
            new_fish = insert_fish(new_fish, i-1, fish[i])
            
    return new_fish
            
        
        
    # process each key as a life cycle