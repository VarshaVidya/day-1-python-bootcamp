# Python DAY-1 👇

# To Comment
#ctrl+/

#simple printing
print("Hello World!")

#print on new line
print("\n")  #print on new line
print("Hello World! \nHello World!")

#String concatenation
print("\n")  #print on new line
print("Hello" + " World!")
print("OR")
print("Hello" + " " + "World!")

#Input function
print("\n")
print("Hello " + input("Input the word World ") + "!")

# Finding the length of the input
print("\n")
length = len(input("What is your name? "))
print("Number of characters in your name is ")
print(length)

# Switching two variables
print("\n")
a = input("a: ")
b = input("b: ")
t = b
b = a
a = t
print("After switching the values in the variables")
print("a: " + a)
print("b: " + b)

#Rules to name a variable
print("\n")
print("Rules to name a variable")
print("1. No Keywords")
print("1. No Spaces ")
print("1. Underscores allowed")
print("1. Relevant to the purpose")

#DAY 1 Band name generator program
print("Welcome to the band name generator")

city = input("What is the name of the city you grew up in ? \n")

pet = input("What is the name of your pet ? \n")

print("The name of your band could be " + city + " " + pet)
