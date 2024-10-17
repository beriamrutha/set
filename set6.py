'''
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
'''
def count_unique_elements():
    input_values = input("Enter the set values separated by space: ").split()
    unique_values = set(input_values)
    unique_count = len(unique_values)
    print(unique_count)
count_unique_elements()
