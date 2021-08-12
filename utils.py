from _typeshed import SupportsItemAccess

#fibonaci sequence function. Use one integer argument
#using this argument we need get n'th number of Fibonaci sequence.
# fibonaci array will contain all number. f variable will value of that number.

def fibonaci(sequence):
    fibonaci_array = []
    i = -1
    y=0
    while y >= 0:
        
        if y>=2:
           i = i+1  
           f = (y-1)+(y-2)
           fibonaci_array.append(f)
        if i == sequence:
            return f"Fibonaci number from sequence {sequence} = {fibonaci_array[y]}"
        else:
            continue
    
    
             
        


    
