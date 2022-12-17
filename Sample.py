my_dict = {'data1':100,'data2':-54,'data3':247}


### YOUR SOLUTION HERE
ans10a =None
### BEGIN SOLUTION
ans10a = 1
for key in my_dict:    
    ans10a=ans10a * my_dict[key]

print(ans10a)