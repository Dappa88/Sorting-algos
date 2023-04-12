def RecurSelectionSort(arr,end,j,compare):
    if end > len(arr)-2:
        return arr
    if arr[j] < arr[compare] and compare == (len(arr)-end)-1:
        return RecurSelectionSort(arr,end+1,0,1)
    if arr[j] > arr[compare] and compare == (len(arr)-end)-1:
       print("i am here",compare)
       arr[j],arr[compare] = arr[compare],arr[j]
       print(" i am arrayj",arr[j])
       print("arr",arr)
       return RecurSelectionSort(arr,end+1,0,1)
    if arr[j] > arr [compare]:
       return RecurSelectionSort(arr,end,j,compare+1)
    else:
       if compare>(len(arr)-end)-1:
           return RecurSelectionSort(arr,end+1,1,2)
       if arr[j] < arr[compare]:
           arr[j],arr[compare] = arr[compare] ,arr[j]
           return RecurSelectionSort(arr,end,j,compare+1)
       
       return RecurSelectionSort(arr,end,j+1,compare +1)
       
       
       
print(RecurSelectionSort([7,5,8,1,9],0,0,1))
       
    
      
      