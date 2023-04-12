def SelectionSort(arr):
    for i in range(0,len(arr)-2):
        for j in range(0,len(arr)-i):
            print("i am i",i)
            if arr[i] >= arr[j]:
                max = i
            else:
                max = j
        
        print(" i am max",max)
        
        
        print("i am the arr[max]",arr[max])
        
        arr[max],arr[(len(arr)-i)
        -1] = arr[(len(arr)-i)-1],arr[max]
         
    return arr
         
         
print(SelectionSort([5,4,3,2,1]))
         
                # the index of j
                # after the inner loop you swao the value with the last value
                #arr[len(arr)-i is equal to ur answer and the max index is equal to that one(swap them)