employee = {
    "Name" : "Abhishek Ramesh Pakhare",
    "age" : 22,
    "Designation" : "Jr. Software Engineer"
}

print("My name is " + employee["Name"]+".")
print("my age is "+str(employee["age"])+".")
print("my designation is "+employee["Designation"]+".")




#converting number to string

phone_number = input("Enter your phone number : ")

digit_mapping ={
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}

output = ""

for digit in phone_number:
    output += digit_mapping.get(digit,"nope") + " "
print(output)