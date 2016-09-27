from sys import argv

with open(argv[1], "r") as file:
    test_cases = [int(x.strip()) for x in file.read().splitlines() if x]

def check_coins(counter,case,coin):
    counter += int(case/coin)
    case = case%coin
    return counter,case

for case in test_cases:
    counter = 0
    for coin in range(5,0,-2):
        counter, case = check_coins(counter, case, coin)
    print(counter)
    
