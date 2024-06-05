def gridTravellerPathCount(a,b, data = {}):
    grid_size = str(min(a,b)) + '_' + str(max(a,b))
    if grid_size in data:
        return data[grid_size]        
    if(a==0 or b==0):
        return 0
    if(a==1 and b==1):
        return 1
    else:
        result = gridTravellerPathCount(a-1,b, data)+ gridTravellerPathCount(a,b-1, data)
        grid_size = str(min(a,b)) + '_' + str(max(a,b))
        data[grid_size] = result
        return result

print("Total Available paths on gridTraveller of given grid is " +str(gridTravellerPathCount(8,30)) + ".")