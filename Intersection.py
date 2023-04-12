def Intersection(arr):
    i = 0
    while i <= len(arr)-2:
        j = i +1
        while  j < len(arr):
            if j < 1 :
                i +=1
                break
            if arr[j] < arr[j-1]:
                arr[j],arr[j -1] = arr[j-1],arr[j]
                j -=1
            else:
                i +=1
                break
    return arr
print(Intersection([5,7,4,9,1]))
 