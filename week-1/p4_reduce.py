"""4.Given a positive integer n and you can do operations as follow:
1.	If n is even, replace n with n/2.
2.	If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?
"""
def reduce(ip,count):
    if(ip==1):
        return count
    elif((ip%2)==0):
        return reduce(int(ip/2),count+1)
    elif ip & (ip+1)==0:
        return reduce(ip+1,count+1)
    else:
        return reduce(ip-1,count+1)
            
def testcase(actualop,expectop,index):
    count=0
    if(actualop!=expectop):
        print("ERROR",index+1)
        count+=1
    return count    




if __name__=="__main__":
    inputs=[8,7,9,15]
    tests=[3,4,4,5]
    for i in range(len(inputs)):
        k=reduce(inputs[i],0)
        count=testcase(k,tests[i],i)
    if(count==0):
        print("code sucessful")