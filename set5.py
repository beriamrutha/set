'''
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output.
'''
def print_similar_values():
    set1_input = input("Enter the first set of values separated by space: ").split()
    set1 = set(map(int, set1_input))  
    set2_input = input("Enter the second set of values separated by space: ").split()
    set2 = set(map(int, set2_input))  
    common_values = set1.intersection(set2)
    sorted_common_values = sorted(common_values)
    print(" ".join(map(str, sorted_common_values)) + " ") 
print_similar_values()
