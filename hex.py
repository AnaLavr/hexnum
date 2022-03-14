def to_hex(n):
    hex_num=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    
    if n<16:
        return (hex_num[n])
    else :
        div= n//16
        rem = n%16
        return (str(hex_num[div])+str(hex_num[rem]))   
    
#print (to_hex(28))         #end of task 1

def hex_color (red,green,blue): 
    r=''
    g=''
    b=''
    if red<16:
        r='0'
    if green<16:
        g='0'
    if blue<16:
        b='0'
    r+=str(to_hex(red))
    g+=str(to_hex(green))
    b+=str(to_hex(blue))
    return r+g+b  
    
print ('#' + hex_color (10,32,255))
    
        
