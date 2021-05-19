def merge_sort(arr, key, descending = False):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_list = merge_sort(left, key, descending)
    right_list = merge_sort(right, key, descending)

    return merge_two_sorted_list(left_list, right_list, key, descending)

def merge_two_sorted_list(left_list, right_list, key, descending):
    sorted_list = list()

    if descending:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                sorted_list.append(left_list.pop(0))
            else:
                sorted_list.append(right_list.pop(0))
    
    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                sorted_list.append(left_list.pop(0))
            else:
                sorted_list.append(right_list.pop(0))

    sorted_list.extend(left_list)
    sorted_list.extend(right_list)

    return sorted_list

if __name__ == "__main__":
    arr = [
            { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
            { 'name': 'rajab', 'age': 12,  'time_hours': 3},
            { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
            { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list = merge_sort(arr, key='time_hours', descending=True)
    print(sorted_list)
    print("\n")
    sorted_list = merge_sort(arr, key='age')
    print(sorted_list)