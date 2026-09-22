# add 2 lists using map and lambda
numbers1 = [3,4,6]
numbers2 = [4,5,6]
result = map(lambda x, y: x+ y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))
#using map
nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of numbers in list")
print(square)