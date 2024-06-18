#this program counts the occurrences of a specific element in a list.

def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

my_list = [1, 2, 3, 4, 2, 2, 3, 1, 1, 5]
element_to_count = 2
print(f"The element {element_to_count} appears {count_occurrences(my_list, element_to_count)} times in the list.")
