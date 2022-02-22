import time,sys,os,random  #import libraries
def typingPrint(text):   #defining function for typewriter effect
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
def clearScreen():
  os.system("clear")

# all above are imported things we need
# get name of player
def start_game():
    def intro():
        global intro
        global name
        
        print("""
          _______   _______  _______ .______     _______. _______     ___                     
         |       \ |   ____||   ____||   _  \   /       ||   ____|   /   \                    
         |  .--.  ||  |__   |  |__   |  |_)  | |   (----`|  |__     /  ^  \                   
         |  |  |  ||   __|  |   __|  |   ___/   \   \    |   __|   /  /_\  \                  
         |  '--'  ||  |____ |  |____ |  |   .----)   |   |  |____ /  _____  \                 
         |_______/ |_______||_______|| _|   |_______/    |_______/__/     \__\                
                                                                                              
.___________..______       _______     ___           _______. __    __  .______       _______ 
|           ||   _  \     |   ____|   /   \         /       ||  |  |  | |   _  \     |   ____|
`---|  |----`|  |_)  |    |  |__     /  ^  \       |   (----`|  |  |  | |  |_)  |    |  |__   
    |  |     |      /     |   __|   /  /_\  \       \   \    |  |  |  | |      /     |   __|  
    |  |     |  |\  \----.|  |____ /  _____  \  .----)   |   |  `--'  | |  |\  \----.|  |____ 
    |__|     | _| `._____||_______/__/     \__\ |_______/     \______/  | _| `._____||_______|           
        \n\n""")
        print("The story begins, as many stories do, at the start, a ship has just pulled into the dock you are walking beside, you go over to see whether there are any interesting stories from the high seas\n\n")
        name = input("Welcome aboard. what be ye name there?: \n\n")
        answers = input("Are you part of the crew [1] or are you the captain [2]?\n\n")
        if answers == "1":
            print(f"You and the crew find the captain dead, with a knife through his heart, before you can escape you are voted in as the new captain, a hat forced upon your head and a telescope into your hand. I guess from now on you shall be known as Captain {name}. You and this fine crew are going to set off and the search for Captain Deepsea's lost treasure.\n\n ")
        else:
            print(f"You have become captain {name}. The intrepid leader of this fine crew and set off and the search for captain Deepsea's lost treasure.\n\n")
            
        # start the game now
        first_act() 
    def first_act():
        print("So which direction should we travel captain?\n")
            
        direction = input("Press n for north, s for south, e for east and w for west : \n")
            
            
        if direction.lower() == "n":
            print("If you say so")
            north()
        elif direction.lower() == "e":
            print("One night on the open seas you feel a storm abrewing. You proceed with caution, the fog falls quickly and engulfs you....\n")
            east()
        elif direction.lower() == "s" :
            print("The south is trecherous Captain, but if ye say so\n")
            print("You travel along for many months, and your supplies are running low, so you stop in a port to buy some food and water. After a few days of debauchery you return to the ship and need to decide which direction you go now........\n")
            level_two()
        elif direction.lower() == "w":
            print("The Western way takes you many months to complete, eventually you circumnavigate the entire world!\n")
            west() 
        else:
            print("Make a decision") 
            first_act()             
    def north():
              
        answer1 = input("\033[1;31;40mYou want to go North? Are you sure? \n") #first option to select following only if statement 

        if  answer1 == "y".lower():
            typingPrint("""\n\033[1;32;40m Crew member: captain we shouldn't be traveling north as this time of winter .It will b all frozen and we don't have that much food stock. we cant survive through this horrible weather while waiting for summer time to come!!!\n""")
            time.sleep(0.01) #typewriter speed
            typingPrint("\n\n\033[1;32;40mAre you absoloutely sure you want to continue?????????\n") # code in start will give style and color to print statement in terminal
            time.sleep(0.01)
        else:
            print("Good choice. Phew. That was a close one. We will go towards the East instead!")
            
            east()
            
            #level 1 option created with if else statement
                        
            answer2 =input("\n\033[1;31;40m Type 1 for yes or 2 for no ")
                        
            if answer2 == "1":
                print("""\033[1;35;37m  
                        
                                            _  _                       
                                    __'__     __'__      __'__
                                /    /    /    /     /    /
                                /\____\    \____\     \____\             
                                / ___!___   ___!___    ___!___               
                            // (      (  (      (   (      (
                            / /   \______\  \______\   \______
                        /  /         
                        /   /    / ___!___ //___!___   ___!____    
                    /    /   |         ||         ||         ||
                    /_____/     \        \\        \\          \\
                        \      \ _______| _______ | __________\\    /                       
                            \         |          |         |         /
                            \________!__________!_________!________/
                            \|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_/|
                            \    _______________                /
                ^^^%%%^%^^^%^%%^\_/_)/_)_/_)__)/_)/)/)_)_'_'_'_'_//)/)/)/)%%%^^^%^^%%%%^
                ^!!^^!%%!^^^!^^^!!^^^%%%%%!!!!^^^%%^^^!!%%%%^^^!!!!!!%%%^^^^%^^%%%^^^!""")

                    
                typingPrint("""\n\033[1;32;40m Your ship got stuck in a ice burg.....you and your crew died starving in cold. Your ship was found by other ships when they startd travelling towards north!!!""")
                game_over()
   
                    #   if you choose to listen to your crew  
            elif answer2 == "2":
                print("""\n\n\033[1;32;40m it was very sensible of you to trust and listen your crew advice ...smart move. you gain your crew trust and now they fully trust you.You are the captain they will die for.....
                            \n""")
                print("""\033[1;35;37m 
                               _____
                            .-" .-. "-.
                        _ / '=(0.0)=' \_
                        /`   .='|m|'=.   `,
                        \_________________/
                    .--.__///`'-,__~\\\\~`
                / /6|__\// a (__)-\\\\
                    \ \/--`((   ._\   ,)))
                    /  \\  ))\  -==-  (O)(
                /    )\((((\   .  /)))))
                /  _.' /  __(`~~~~`)__
                //"\\,-'-"`   `~~~~\\~~`"-.
                //  /`"              `      `
                //

                        """)
                level_two()  
           
            else:
                typingPrint("\n\n\033[1;32;40m Don't try to be extra smart. Crew life depends on you!\n")
                time.sleep(0.01) 
                intro()
                    
                        
        #level 2 
    def level_two():

            answer3 = input("\n\033[1;31;40m Pick e for east or w for west or s for south \n") 
                  
            if answer3 == "e":
                print("One night on the open seas you feel a storm abrewing. You proceed with caution, the fog falls quickly and engulfs you....\n")
                east()
                
            elif answer3 == "w":
                typingPrint("\n\033[1;32;40m You wish to head West?. Are you sure you wish to proceed?\n")
                time.sleep(0.01)  
                   
                x = input("\n\n\033[1;32;40mStill want to go?\n")
                if x == "y":
                    west()
                else:
                    print("The Western way takes you many months to complete, eventually you circumnavigate the entire world!\n")
                    east()
            elif answer3 == "s":
                typingPrint("""\n\n\033[1;32;40mYour crew members trusted you. You headed south with great confidence  and discover a new island called Skull Island. You and your crew loved its beauty that you decide to make this island your home \n""")
                time.sleep(0.01)
                congratulations()
            else:
                typingPrint("\n\n\033[1;32;40m If you cant type e, w or s you have no right to play this game ")
                time.sleep(0.5) 
                intro()  
                    
    def east():
                typingPrint("Through the mist and fog you can see the outline of a ship in the distance\n")
                typingPrint(" Do you....\n")
                typingPrint(" a - approach the ship\n")
                typingPrint(" b - ignore the ship and continue\n")
                typingPrint(" c - head back to the start\n")
                time.sleep(0.01)

                answer4 = input (" ")

                if answer4 == "a":
                    ship()
                    
                elif answer4 =="b":
                    typingPrint("You get attacked by a Kraken and your ship gets destroyed\n")
                    time.sleep(0.01)
                    game_over()
                    
                elif answer4 == "c":
                    typingPrint("You are sent back to the start\n")
                    time.sleep(0.01)
                    first_act()  
                    
                else:
                    typingPrint("Don't you know how to type a,b or c!? \n")
                    time.sleep(0.01)
                    ("This will show you.....\n")
                    east()


    def ship():
                typingPrint("The ship is friendly and the captain provides you and your crew members with some food\n")
                typingPrint(" You come across some weapons and have the chance to take them, do you? y/n\n")
                time.sleep(0.01)
                answer = input (" ")
                if answer == "y":
                    typingPrint("You take the weapons and return to your ship before the other Captain notices.\n")
                    typingPrint("You sail away and happily inspect your new weapons\n")
                    typingPrint("All of a sudden your ship is attacked by a giant sea monster. A Kraken!!!\n")
                    time.sleep(0.01)
                    typingPrint("You defeated the kraken with the weapons you picked up and set sail into the wide open ocean\n")
                    time.sleep(0.01)
                    congratulations()
                elif answer == "n":
                        typingPrint("your ship is attacked by a kraken and gets destroyed\n")
                        time.sleep(0.01)
                else :
                        typingPrint("hint, it's either y or n \n")
                        time.sleep(0.01)
                        ship()
            
    def west():
        global name
    
        print("\nAfter a long, treacherous journey, headed west....")
        print("\nYou arrive at a port, and as you step off your ship, you see a lone fellow traveller, looking inebriated and worse for wear..\n")
                   
        answer = input("You decide whether to:\n \na) interact with the stranger, \nb) return to board the ship \n\n")

        if answer == 'a':
            print ("You choose to speak with the mysterious stranger \n")
            print("He suddenly seems to wake up from his drunken stupor and looks at you intently.")
            game()
        elif answer == "b":
            print ("You choose to return to your ship\n")
            print("You set sail again and avoid the perils and the treasures of the West, as the dark falls, a thick mist rolls in")
            east()
        else:
             print("Please choose interact with stranger, board ship or remain\n") 
             west()

    def game(): 
                answer = input("\n ..be ye?\n \na) lad, \nb) wench ..or.. \nc) otherwise.. \n\n: ")
                if answer == 'a':
                    input("\nWhat be your name laddy? :\n")
                    print(f"Ahh ye be {name}. I've heard of you in these here parts. Let me do you a deal, play me at a game and I'll let you continue on your merry way")
                    games_start()
                elif answer == 'b':
                    input ("\nWhat be your name wench? :\n")
                    print(f"Ahh ye be {name}. I've heard of you in these here parts. Let me do you a deal, play me at a game and I'll let you continue on your merry way")
                    games_start()
                elif answer == 'c':
                    input ("Well whether ye be..\nAgender,Androgyne,Androgynous,Bigender,Cis,\nCisgender,Cis Female,Cis Male,Cis Man,Cis Woman,Cisgender Female,Cisgender Male,Cisgender Man"
                    "\nCisgender Woman,Female to Male,FTM,Gender Fluid,Gender Nonconforming,Gender Questioning,\nGender Variant,Genderqueer,Intersex,Male to Female,MTF,Neither,Neutrois,Non-binary"
                    "\nOther,Pangender,Trans,Trans*,Trans Female,Trans* Female,Trans Male,Trans* Male,Trans Man,\nTrans* Man,Trans Person,Trans* Person,Trans Woman,Trans* Woman,Transfeminine"
                    "\nTransgender,Transgender Female,Transgender Male,Transgender Man,Transgender Person,\nTransgender Woman,Transmasculine,Transsexual,Transsexual Female,Transsexual Male"
                    "\nTranssexual Man,Transsexual Person,Transsexual Woman or Two-Spirit \n..welcome to ye, now state ye name.. \n\n")
                    print(f"Ahh ye be {name}. I've heard of you in these here parts. Let me do you a deal, play me at a game and I'll let you continue on your merry way")
                    games_start()
                else:
                    input("\nOh a smarypants ay? just stick to the script rapscallion and state your name..\n")
    def games_start():
                    word_list = [
                            ("compass"),("crew"),("deckhands"),("eyepatch"),("firstmate"),("galleon")
                            ]

                            # WHERE THE GAME PULLS WORDS FROM

                    random_word = random.choice(word_list)

                    guesses = ''

                    turns = 12

                    while turns > 0:

                        failed = 0

                            # THE RULES FOR THE WORD GAME

                        for char in random_word:

                                    if char in guesses:
                                        print (char)

                                    else:
                                            print ("_")

                                            failed += 1

                            # FIRST PART OF THE ACTUAL GAME..

                        if failed == 0:
                                    print("----------------------------------------------------------------------------------------------------------------------------")
                                    print(f"\nCongratulations matey.. You've bested me, the word i was thinking of was {random_word}\n")
                                    print("\nHeres the directions to the east, but.. BEWARE THE KRAKEN!! ..Travel At Ye Own Peril\n")
                                    print("----------------------------------------------------------------------------------------------------------------------------")
                                    print("You head back to your ship and climb aboard with the knowledge the stranger gave you\n")
                                    print("To begin with you head out into the open seas, as darkness falls a thick fog closes in around you")
                                    east()

                        guess = input("\nguess a letter:\n\n\n")

                        guesses += guess

                        if guess not in random_word:

                            turns -= 1

                            print (f"\nUnlucky young scallywag {name}")

                            print ("\nYou have", + turns, 'more guesses\n')

                            if turns == 0: 
                                restart = input("You lose")
                                game_over()
                                if restart == "":
                                    games_start()
                                else:
                                    game_over()           

    
                                                            
                    congratulations()                
                    
    def congratulations():
                    print("""\033[1;35;37m
        ___    ____  ______    __    __          _______. __    __  .______     ____    ____  __  ____    ____  _______  _______  
       \   \  /   / /  __  \  |  |  |  |        /       ||  |  |  | |   _  \    \   \  /   / |  | \   \  /   / |   ____||       \ 
        \   \/   / |  |  |  | |  |  |  |       |   (----`|  |  |  | |  |_)  |    \   \/   /  |  |  \   \/   /  |  |__   |  .--.  |
         \_    _/  |  |  |  | |  |  |  |        \   \    |  |  |  | |      /      \      /   |  |   \      /   |   __|  |  |  |  |
           |  |    |  `--'  | |  `--'  |    .----)   |   |  `--'  | |  |\  \----.  \    /    |  |    \    /    |  |____ |  '--'  |
           |__|     \______/   \______/     |_______/     \______/  | _| `._____|   \__/     |__|     \__/     |_______||_______/ 
                                                                                                                                                        
                    """)
                    print(".......for now.........")
                        
                        
                    time.sleep(0.01)
                    typingPrint("\nGood bye!\n")
                    typingPrint("This screen will clear itself in 3..")
                    time.sleep(1)
                    typingPrint("2..")
                    time.sleep(1)
                    typingPrint("1..")
                    time.sleep(1)
                    quit   
       
         
                        
    def game_over():    
                print("You failed in your vain attempt to find the treasure. The sad truth is....there never was any treasure......")
                print(".....or was there?")
                print("""
                      
    
                         ______
                      .-"      "-.
                     /             l
         _           |              |          _
        ( \         |,   .-.  .-.  ,|         / )
        > "=._       | )(__/  \__)( |     _.=" <
        (_/"=._"=._ |/      /\     \| _.="_.="\_)
                "=._ (_     ^^     _)"_.="
                    "=\__|IIIIII|__/="
                    _.="|\IIIIII/ |"=._
        _     _.="_.="\          /"=._"=._     _
        ( \_.="_.="     `--------`     "=._"=._/ )
        > _.="                            "=._ <
        (_/                                    \_)

                      """)                
                print("""    
                     _______       ___      .___  ___.  _______      ______   ____    ____  _______ .______         
                    /  _____|     /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||  _  \        
                    |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__  |  |_)  |       
                    |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __| |      /        
                    |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____|  |\  \----.   
                     \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|   
                            
                            """)
   
                typingPrint("\n\n\033[1;32;40mGood bye!\n")
                typingPrint("This screen will clear itself in 3..")
                time.sleep(1)
                typingPrint("2..")
                time.sleep(1)
                typingPrint("1..")
                time.sleep(1)
 
    intro()
start_game()