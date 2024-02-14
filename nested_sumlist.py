'''def nested_sum(list1):
    sum1 = 0
    for i in list1:
        
        sum1 = sum1+sum(i)

    return sum

nested1 = [[1,2,3],[2,2,3],[5,1,6]]
print(nested_sum(nested1))
'''
def nested_sum(lst_of_lst):
    total_sum = 0
    for inner_lst in lst_of_lst:
        total_sum += sum(inner_lst)
    return total_sum

# Example usage:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = nested_sum(nested_list)
print(result)
