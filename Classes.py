class Calculation:
      
       # creating constructor to initialize the object of the class
       # self : represent the the instance of the class
       def __init__(self,num1,num2):
        
            self.num1=num1
            self.num2=num2

       def addition(self):

            return self.num1 + self.num2  
       


num1=int(input("Enter First Number:"))
nums2=int(input("Enter Second Number:"))

      
# creating the object of the class 
calc=Calculation(num1=num1,num2=nums2)


#  use class object to access the methods and atributes
results=calc.addition()
print(f" The sum of {num1} and {nums2} is {results}")