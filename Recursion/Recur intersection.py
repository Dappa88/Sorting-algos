def RecurIntersection(arr,end,j):
    if end > len(arr) -2:
        return arr
    if j < 1:
        return RecurIntersection(arr,end+1,end+2)
    #if j > j-1:
        #return RecurIntersection(arr,end+1,end+2)
    if arr[j]< arr[ j-1]:
       arr[j],arr[j-1] = arr[j-1],arr[j]
       
       
       return RecurIntersection(arr,end,j-1)
    return RecurIntersection(arr,end+1,end+2)
  
 
print(RecurIntersection([5,4,7,8,1],0,1))