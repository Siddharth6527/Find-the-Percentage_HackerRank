n = int(input())
#initializing required variables
data_list=[]
count = 0
avg=0
if (n>=2 and n<=10):
    #check for n
    for i in range(0,n):
        data=input().split()
        #Length of arrays should be 3
        for z in data:
            count+=1
            if count==4:
                #converting str to int values and checking marks range
                for j in range(1,4):
                    data[j]=float(data[j])
                    if (0<=data[j] and data[j]<=100):
                        avg+=data[j]
                avg/=3
                data.append(avg)
        #reset the temp-values        
        avg=0
        count=0
        data_list.append(data) 
#getting the required name
req_name=input()
for a in data_list:
    if a[0]==req_name:
        print("{:.2f}".format(a[4]))

#by Siddharth Verma
