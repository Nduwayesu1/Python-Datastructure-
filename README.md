## Python-Datastructure-



## 1. Python Lists
A list is a collection that is ordered, mutable, and allows duplicate values.

## Example: Creating and Using Lists 
```python
# Creating a list
my_list = [10, 20, 30, 40, 50]

# Accessing elements
print(my_list[0])  # Output: 10

# Modifying a list
my_list.append(60)  # Adds 60 to the list
print(my_list)      # Output: [10, 20, 30, 40, 50, 60]

# Removing an element
my_list.remove(30)  
print(my_list)      # Output: [10, 20, 40, 50, 60]



# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science"
}

print(student)  # Output: {'name': 'Alice', 'age': 22, 'course': 'Computer Science'}




## Introduction to Functions  

A function in Python is a reusable block of code designed to perform a specific task.  

 **Key Benefits of Functions**:  
- Code Reusability**  
- Modularity**  
- Readability and Maintainability**  
- Efficient Debugging**  

---

##  Defining Functions  

### Example: Creating and Calling a Function  
```python
def greet():
    print("Hello, Welcome to Python!")

greet()  # Output: Hello, Welcome to Python!


## Creating a Class and Object  

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


#  use class object to access the methods and atributes  and store the results in a variable
results=calc.addition()
print(f" The sum of {num1} and {nums2} is {results}")
