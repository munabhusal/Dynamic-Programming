def gridTravellerPath(a,b):   
    if(a==0 or b==0):
        return 0
    if(a==1 and b==1):
        return 1
    else:
        result = gridTravellerPath(a-1,b)+ gridTravellerPath(a,b-1)
        return result
    
print("Total Available paths on gridTraveller of given grid is " +str(gridTravellerPath(8,10)) + ".")
