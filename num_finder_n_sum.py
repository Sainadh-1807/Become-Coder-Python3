mylist = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
for num in mylist:
  if num>0:
    if num%2==0:
          print("Even number : ",num)
    else :
          print("Odd number : ",num)
  else:
      print("negative number :  ",num)
sumlist=0
for sum in mylist:
    sumlist = sumlist+sum
    print('Sum of numbers : ', sumlist)