def BubbleSort(arr):
    swap = False
    for i in range(0,len(arr)-1):
        for j in range(1, (len(arr)-i)):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                print(" i am zwappeing")
                swap = True
        if (not swap) :
             break
             
    return arr
   
  
print(BubbleSort([1,2,3,5,4]))