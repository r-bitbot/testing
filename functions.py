#functions
print("functions:")
print(len("python"))  
print(sum([1, 2, 3]))  

#string functions
text = "hello, python!"
print("string functions:")
print(text.strip())  
print(text.replace("python", "world"))  

#list functions
numbers = [3, 1, 4, 2]
print("sort list:")  
numbers.append(4)
print(numbers) 
numbers.remove(2)
print(numbers)
print(numbers.pop(1))  
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#dictionary functions
person = {"name": "Ruchi", "age": 20}
print("dictionary functions:")
print(person.keys())  
print(person.values())
print(person.items())
print(person.get("name")) 
print(person.get("number", "Not Found"))
person.update({"number": 9876543210})
print(person)

#lambda function
square = lambda x: x ** 2
print("lambda function:")
print(square(4))  