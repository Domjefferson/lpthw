def add(a,b):
    print(f"adding {a} +{b}")
    return a + b
 def subract (a,b):
     print(f"subtracting {a} - {b}")
     return a - b
def multiply(a,b):
    print(f"multiplying {a} * {b}")
    return a * b
def divide (a,b):
    print(f"dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions !")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(310 ,2)

print (f"age: {age}, height:{height},weight{weight}iq:{iq}"")

#A puzzle for the extra credit, type it in anyway value
print("here is a puzzle ")

what = add(age, subract(height,multiply(weight,divide(iq,2))))

print("that becomes:", what , "can you do it by hand")
