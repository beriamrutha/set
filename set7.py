'''
Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
def find_max_min_values():
    input_values = input("Enter the set values separated by space: ").split()
    values_set = set(map(int, input_values))
    max_value = max(values_set)
    min_value = min(values_set)
    print(f"Maximum: {max_value}")
    print(f"Minimum: {min_value}")
find_max_min_values()
