def likes(names):
    totalNames = 0
    for name in names:
        totalNames += 1
        
    if totalNames > 3:
        return(f"{names[0]}, {names[1]}, and {totalNames - 2} others like this")
    elif totalNames == 3:
        return(f"{names[0]}, {names[1]}, and {names[2]} like this")
    elif totalNames == 2:
        return(f"{names[0]} and {names[1]} like this")
    elif totalNames == 1:
        return(f"{names[0]} likes this")
    else:
        return("no one likes this")

print(likes(["Peter", "Ron", "Jake", "Alex", "Mike", "Wayne"]))