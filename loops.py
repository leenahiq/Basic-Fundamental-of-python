import random
fav_drink = ["coke","pepsi","miranda"]

for drink in fav_drink:
    print(drink)


#rang()is built in function 

for i in range(10):
  print(i)

 #if you want to print string then number in rang 
  
for i in range(10):
   print("leenah")


   #giving starting point ending point 

   #for i in range(0,10):
    #print(i)

 
   #for i in range(1,11):
   # print(i)

# third argument

    #for i in range(0,10,2):
    # print(i)
# now it will take 1 starting point and add 2 in this case it will giv odd numbers

     #for i in range(1,10,2):
      #print(i)



      #activity 1
fav_film = ["avengers","iron man","ps i love you","dont look up"]  

def film_check():
    global fav_film
    if fav_film[2] == "ps i love you":
          print("yeh!!! its ps i love you")
    else:
          print("boooo")
film_check()

    #activity 2
     
#or i in reversed(range(10)):
    #print(i)


    #while loop 
num = 0
while num <10:
    num += 1
    print(num)


    rand_num = random.randint(0,20)

my_num = 18

while rand_num != my_num:
    print(rand_num)
    rand_num = random.randint(0,20)

print(f"You've found {my_num}!")


#activity1

for i in range(13):
    print("hello world")

num = 13

while num <13:
 num += 1
 print(num)


 # task 2 

# we need the programme to run 6 times
for i in range (6):
    # the numbers need to be between 1 and 30
    rand_num = random.randint(1, 30)
    
    # for each number generated see if it can be divided by 7
    if rand_num % 7 == 0:
        print(f"{rand_num} is divisible by 7")
    else:
        print(f"{rand_num} is not divisible by 7")


        cards = [
    "Diamond", 
    "Heart",
    "Spade", 
    "Club"
    ]

my_card = "Diamond"

current_card = random.choice(cards)

while my_card != current_card:
    print(current_card)
    current_card = random.choice(cards)

print(f"You found {my_card}!")