#Function to add two numbers
def add(x,y):
	return(x+y)
#Function to subtract two numbers
def add(x,y):
	return(x-y)
#Function to multipy two mnumbers
def add(x,y):
	return(x*y)
#Function to divide two numbers
def add(x,y):
	return(x/y)
print("please select operation \n"\
	"1.Add\n"\
	"2.Subtraction\n"\
	"3.Multplication\n"\
	"4.Divide\n")
select = int(input("Select operations from 1,2,3,4:"))

num_1 = int(input("Enter fisrt number:"))
num_2 = int(input("Enter second number:"))

if select == 1:
    print(num_1,"+",num_2,"=",add(num_1,num_2))

elif select == 2:
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))

elif select == 3:
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))

elif select == 4:
    print(num_1,"/",num_2,"=",divide(num_1,num_2))

else:
    print("invalid input")