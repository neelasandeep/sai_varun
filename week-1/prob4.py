def bitnum(num,count):
    if(num==0):
       # print(count)
        return count
    else:
        
        return bitnum(num & (num-1),count+1)

if __name__=="__main__":
    l,z=[],[]
    inputs=[2,0,5]
    #inputs=list(map(int,inputs))
    for i in range(0,len(inputs)):
        for j in range(0,inputs[i]+1):
            k=bitnum(j,0)
            l.append(k)
        z.append(l)
        l = []
    for i in range(0,len(z)):
        print(z[i])    