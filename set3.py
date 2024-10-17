'''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.
'''
def print_different_values():
    set1_input = input("Enter the first set of values separated by space: ").split()
    set1 = set(map(int, set1_input))  
    set2_input = input("Enter the second set of values separated by space: ").split()
    set2 = set(map(int, set2_input))  
    different_values = set1.symmetric_difference(set2)
    sorted_different_values = sorted(different_values)
    print(" ".join(map(str, sorted_different_values)) + " ")  
print_different_values()
