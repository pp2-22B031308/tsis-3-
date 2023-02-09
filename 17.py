def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return (chickens, rabbits)
    return None

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
if result:
    print(f'There are {result[0]} chickens and {result[1]} rabbits on the farm.')
else:
    print('No solution found.')

