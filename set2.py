'''
Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
Note: There is no trailing space at the end of output.
'''
def get_and_print_sorted_values():
    input_values = input("Enter the values separated by space: ").split()
    values_set = set(map(int, input_values))
    sorted_values = sorted(values_set)
    print(" ".join(map(str, sorted_values)))
get_and_print_sorted_values()
