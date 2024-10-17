'''
Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
'''
def update_set():
    set1_input = input("Enter the first set of values separated by space: ").split()
    set1 = set(map(int, set1_input))  
    set2_input = input("Enter the second set of values separated by space: ").split()
    set2 = set(map(int, set2_input))  
    set1.update(set2)
    updated_set = sorted(set1)
    print(" ".join(map(str, updated_set)) + " ")  
update_set()
