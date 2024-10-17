'''
 Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
'''
def get_and_print_sorted_values():
    n = int(input("Enter the number of values: "))
    values_set = set()
    for _ in range(n):
        value = int(input())
        values_set.add(value)  # Add value to the set
    sorted_values = sorted(values_set)
    print(" ".join(map(str, sorted_values)))
get_and_print_sorted_values()
