# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

true_word = t + r + u + e
love_word = l + o + v + e
combined_words = int(str(true_word) + str(love_word))

if (combined_words < 10) or (combined_words > 90):
    print(f"Your score is {combined_words}, you go together like coke and mentos.")
elif combined_words >= 40 and combined_words <= 50:
    print(f"Your score is {combined_words}, you are alright together")
else:
    print(f"Your score is {combined_words}")