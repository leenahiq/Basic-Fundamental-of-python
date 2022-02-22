music = "rock"

if music == "classic":
    print("good")
elif music == "rock":
     print("cool")
elif music == "jaz":
      print("boring")
else:
       print("print some music on") 

my_age = 21

if my_age > 17:
    print("Yess I can serve you")
else:
     print("you arn't old enough")   

city = "MCR"
weather = "sunny"

if city == "MCR" and weather == "sunny":
    print("lets go to MCR")
elif city == "MCR" and weather == "cloudy":  
    print("naaaa") 
else:
    print("what shall i do")


age = 20
country = "UK"

if age > 17 and country == "UK":
   print("you dont need to isolate")
else:
   print("you need to isolate")

#challenge 1

password = "Iamlazzy&usless"

print(len(password))

if len(password) < 8:
     print("password is to short")
else:
    print(password)

# challenge 2

num = 15
if num%3 == 0 or num%5 == 0:
    print("this number is divisible by 3 and 5")
else:
    print("this number is not divisible of 3 and 5")


#challenge 3

num = 21
# both condition shoul b at top other wise wont work 
if num%3 == 0 and num%7 == 0:
    print("fizz buzz")
elif num%3 == 0:
    print("Fizz")
elif num%7 == 0:
    print("buzz")
else:
    print("number is not divisiblele by both number")


#challenge 4

word = "AMERICA"

if word[0] == word[-1]:
    print(True)
else:
    print(False)

#challenge 5 

time = 9
place_of_work = "i'm at work"
town_of_home =  "i'm at home"

if time == 7:
    print(town_of_home)
elif time == 8:
    print("i'm commutin")
elif time == 9:
     print(place_of_work)
else:
    print("unavailable")

#challenge 6

num1 = 2
num2 = 2
sum = num1 + num2

if  sum%2 == 0:
    print(" great your number is even")
else:
    print("your number is odd")

# challenge 7
# reverse the string using slice notation [::-1]
word = "abcdef"
print(word[::-1])


# we can check using slice notation that word or string is palindrome or not 
word1 = "racecar"
if word1 == word1[::-1]:
     print(True)
else:
     print(False) 


#hallenge 8: 
#Find the index of a last vowel in the string.

str = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi" 

print(str.count("a"),str.count("e"),str.count("i"),str.count("o"),str.count("u"))


