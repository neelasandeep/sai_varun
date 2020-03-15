""" Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation)."""
def bitnum(a,b,c):
    count=0
    while (a|b):
        if(((a | b) & 1) ^(c & 1)):
            if((a & 1) & (b & 1)):
                count+=2
                #print(count)
            else:
                count+=1
               # print(count)
            #print(count)
        a=a>>1
        b=b>>1
        c=c>>1       
    return count
        
if __name__=="__main__":
    a=[2,3]
    b=[6,0]
    c=[5,0]
    error=0
    expectop=[3,2]
    #Testing starts here!!!
    for i in range(len(c)):
        output=bitnum(a[i],b[i],c[i])
        if(output!=expectop[i]):
            print("ERROR",i)
            error+=1
    if(error==0):
        print("code sucessful")
