def search(list, n):

    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u)// 2

        if list[mid] == n:

            return True

        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid
                


list = [3,4,5,6,7]
n = 3 
print(list)
if search(list,n):

    print('found')
else:
    print("not found")
