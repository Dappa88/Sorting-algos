def RecurBubble(arr,end,j):
    swapped = False
    
    if end > len(arr) -2 and j >(len(arr)-end)-1:
        return arr
    if j > len(arr)-1:
        print("hello world")
        return RecurBubble(arr,end+1,1)
    if arr[j] < arr[j-1]:
        swapped = True
        arr[j],arr[j-1] =arr[j-1],arr[j]
        return RecurBubble(arr,end,j+1)
    else:
        return RecurBubble(arr,end,j+1)
    if (not swapped):
        return arr
       
       
       
print(RecurBubble([5,4,3,2,1],0,1))
      
     
     