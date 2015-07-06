"""
Generate all combinations of a list of choices.
"""

mylist = list('monde')
mylist2 = [1,2,3]

"""
1) generate all subsets
2) generate all possible permutations based on each set
"""

possibilities = set()

def subsets(arr):
    result = [''.join(arr)]
    if len(arr) > 1:
        for el in arr:
            result += subsets(''.join(set(arr) - set(el)))
    return result

print subsets(mylist)