# print("Hello from lesson 7")


# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))

# for number in range(1, 11):
#     print(number)

# for number in range(2 , 21 , 2):
#     print(number)

# for number in range(10 , 0 , -1):
#     print(number)

# for number in range(1, 11):
#     print(number)

# word=input("What is your word?")
# times=int(input("How many times do you want it to repeat?"))

# for i in range(times):
#     print(word)
# range is to count numbers

# sum=0
# for i in range(1,6):
#     sum = sum + int(input("what is number #"+ str(i)


# print(sum)

# times=int(input("What number is for the timestable?"))

# for i in range(1,13):
#     print(str(times) +  " x " + str(i)+" = " + str(times * i))


# layers=int(input("How many layers?"))
# for i in range(1, layers+1):
#     print(str(i)*i)


# sum=0
# for number in range(1, 6):
#     sum=sum+int(input("What is the score of the student "+ str(number) + "?"))

# print(sum/5)


sum=0
num = int(input("What is the number of students?"))
for number in range(1, num+1):
     sum=sum+int(input("What is the score of the student "+ str(number) + "?"))

print(sum/num)