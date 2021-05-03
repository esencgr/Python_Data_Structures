from util import time_it

@time_it
def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index 
    return -1

@time_it
def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1 
    mid_index = 0 
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2 
        mid_number = number_list[mid_index]
        
        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1 

        else:
            right_index = mid_index - 1  
    
    return -1 

if __name__ == "__main__":
    
    numbers = [number for number in range(100001)]
    number_to_find = 100000

    index = linear_search(numbers, number_to_find)
    print(f"Number found at index : {index} using linear search")

    index = binary_search(numbers, number_to_find)
    print(f"Number found at index : {index} using linear search")
