# *********************************************
#                 Typing Speed
# *********************************************

from time import time

paragraph = input("type the paragraph you want to train on \n")
output = paragraph.split()

print(f"this is paragraph to type: \n {paragraph}")
input("When you are ready type ENTER,and when you finish type ENTER \n")


start = time()
user_input = input("Counter started: 1 2 3 ...\n").split()
end = time()

difference = end-start

print(f"Time elapsed is {difference} seconds")
print(paragraph.split())

errors = 0
correct_words = 0

for i in range(len(user_input)):
    if (user_input[i] != output[i]):
        errors += 1
    else:
        correct_words += 1

incorrect_words = len(output)-correct_words
accuracy = correct_words*100/len(user_input)
speed = len(user_input)*60/difference
print(
    f"Details:\n correct words : {correct_words} \n\
    incorrect words: {incorrect_words} \n\
    errors: {errors} \n\
    Speed : {speed} wpm")
print("accuracy: {:2f}%".format(accuracy))
