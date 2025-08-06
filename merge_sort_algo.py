# # thi is kindof a dfs search no?

# def merge_sort(lis:list[int]):
#     """
#     Sort given list of ints in ascending order

#     Input: list[int]
#     Return: list[int]

#     Steps:
#         Divide (find midpoint of list and divdide into sublists)
#         Recursively sort these sublists
#         Merge the sorted sublists to make output
#     """

#     if len(lis) <= 1:
#         return lis
    
#     l, r = split(lis)
#     # recusrive function here
#     left = merge_sort(l)
#     right = merge_sort(r)

#     merged = merge(left, right)
#     return merged

# def split(lis:list):
#     """
#     Divides unsorted lists at midpoint, into sublist(s)

#     Returns 2 sublists: left and right
#     """    
#     mp = len(lis) // 2
#     left = lis[:mp] # start to mp
#     right = lis[mp:] # mp to end

#     return left, right

# def merge(l:list, r:list):
#     """
#     Merges two lists/ arrays, sorting in the proscess

#     Return: new, sorted list
#     """
#     return_list = []

#     i = 0
#     j = 0

#     while i < len(l) and j < len(r):
#         if l[i] < r[j]:
#             return_list.append(l[i])
#             i += 1
#         else:
#             return_list.append(r[j])
#             j += 1
#     while i < len(l):
#         return_list.append(l[i])
#         i += 1
#     while j < len(r):
#         return_list.append(r[j])
#         j += 1
#     return return_list

x = [34556, 76, 345, 21332, 4655675, 78, 543, 23, 1234, 4, 312, 35, 57, 78, 90, 87]

# y = merge_sort(x)
# print(y)





# re-try/ learning of merge-sort algo

# defining the parent function that is recursive (call again, and again untill things are split & sorted)
def merge_sort(l:list):
    if len(l) <= 1:
        return l
    l, r = split(l)
    left = merge_sort(l)
    right = merge_sort(r)

    merged_lsit = merge(left, right)
    return merged_lsit

def split(l:list):
    mp = len(l) // 2

    left = l[:mp]
    right = l[mp:]

    return left, right

def merge(l, r):
    return_list = []
    i = 0
    j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            return_list.append(l[i])
            i += 1
        else:
            return_list.append(r[j])
            j += 1
    # accound for odd lists
    while i < len(l):
        return_list.append(l[i])
        i += 1
    while j < len(r):
        return_list.append(r[j])
        j += 1
    
    return return_list

merged_list = merge_sort(x)
print(merged_list)

