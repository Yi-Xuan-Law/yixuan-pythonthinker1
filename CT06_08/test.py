# name=input("What is your name?")   #ask user what is their name
# print("nice to meet you, " + name)  #nice to meet you, person's name


start=int(input("What is your start number?"))   #ask user what is the start number
stop=int(input("What is your stop number?"))
increament=int(input("What is the increament?"))

for i in range(start, stop, increament):
    print(i)
