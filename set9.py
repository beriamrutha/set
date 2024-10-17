'''
Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''
def find_duplicates_and_unique_set():
    n = int(input("Enter the number of values: "))
    input_values = []
    for _ in range(n):
        value = int(input())
        input_values.append(value)
    value_count = {}
    for value in input_values:
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1
    duplicate_count = sum(1 for count in value_count.values() if count > 1)
    unique_values = set(input_values)
    print(f"Duplicate Values: {duplicate_count}")
    print(" ".join(map(str, sorted(unique_values))) + " ")
find_duplicates_and_unique_set()
