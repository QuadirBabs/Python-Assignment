square = lambda num: num * num
print(square(4)) 

def FuncBuild(X):
    return lambda num: num + X
addTwo = FuncBuild(10)
AddFifty = FuncBuild(115)
print(addTwo(40))
print(AddFifty(12))

number = [3,7,10,25,33]
square_nums = map(square,number)
print(list(square_nums))
