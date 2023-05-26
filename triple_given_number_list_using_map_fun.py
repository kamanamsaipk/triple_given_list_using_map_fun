given_numbers = [1,2,3,4,5,6,7,8,]
def triple_num(given_numbers):
    return list(map(lambda x:x*3,given_numbers))
tripled_numbers = triple_num(given_numbers)
print(tripled_numbers)

