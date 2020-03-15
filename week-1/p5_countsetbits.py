"""Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Example 1:
Input: 2
Output: [0,1,1]"""

def bitcount(num,count):
    if(num==0):
       # print(count)
        return count
    else:
        
        return bitcount(num & (num-1),count+1)
def Testcase(inputs,index):
    l=[]
    count=0
    expectop=[[0,1,1],[0],[0,1,1,2,1,2]]
    for i in range(inputs+1):
        k=bitcount(i,0)
        l.append(k)
    #print(l)
    if(l!=expectop[index]):
        print("ERROR",index+1)
        count+=1
    return count


if __name__=="__main__":
    l,z=[],[]
    inputs=[2,0,5]
    count=0
    #inputs=list(map(int,inputs))
    for i in range(0,len(inputs)):
        count+=Testcase(inputs[i],i)
    if(count==0):
        print("code sucessful")