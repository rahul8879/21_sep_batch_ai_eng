def square(array):
    '''
    This function takes an array of numbers and returns a
      new array with the squares of each number.

      input : array of numbers
      output : array of numbers ( squared )

      eg [1, 2, 3] => [1, 4, 9]
      square([1, 2, 3])==>[1, 4, 9]
    '''
    result = []
    for num in array:
        result.append(num ** 2)
    return 


# array =[2,3,7,5,4]
# target = 9
# Two sum problem
# I need to return the combination ==> sum ==> 9

def target_sum(array, target=7):
    print('value of target',target)
    num_dict = {}
    for i, num in enumerate(array):
        print(f"i: {i}, num: {num}, num_dict: {num_dict}")
        # complement = target - num
        # if complement in num_dict:
        #     return (num_dict[complement], i)
        # num_dict[num] = i
    # return None

# # print(square([1, 2, 3, 4, 5]))
# print(target_sum([2, 3, 7, 5, 4],9))