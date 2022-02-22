import time,sys,os  #import libraries 
def typingPrint(text):   #defining function for typewriter effect  
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
def clearScreen():  #defining function for clearing screen after game finish 
  os.system("clear")



def select_north():   # defining function for whole north chunk
    global select_north
print("""\033[1;33;40m   @@@@@@@   @@@@@@   @@@@@@@   @@@@@@@   @@@@@@   @@@  @@@  @@@     @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@       @@@@@@   @@@@@@@@   @@@@@@   
  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@  @@@@ @@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@   @@@@@@@@  @@@@@@@@  """)
time.sleep(1) 
print("""\033[1;33;40m !@@       @@!  @@@  @@!  @@@    @@!    @@!  @@@  @@!  @@!@!@@@     @@!  @@@  @@!       @@!       @@!  @@@     !@@       @@!       @@!  @@@ 
 !@!       !@!  @!@  !@!  @!@    !@!    !@!  @!@  !@!  !@!!@!@!     !@!  @!@  !@!       !@!       !@!  @!@     !@!       !@!       !@!  @!@   """)
time.sleep(1) 
print("""\033[1;33;40m !@!       @!@!@!@!  @!@@!@!     @!!    @!@!@!@!  !!@  @!@ !!@!     @!@  !@!  @!!!:!    @!!!:!    @!@@!@!      !!@@!!    @!!!:!    @!@!@!@!  
 !!!       !!!@!!!!  !!@!!!      !!!    !!!@!!!!  !!!  !@!  !!!     !@!  !!!  !!!!!:    !!!!!:    !!@!!!        !!@!!!   !!!!!:    !!!@!!!!  """)
time.sleep(1) 
print("""\033[1;33;40m :!!       !!:  !!!  !!:         !!:    !!:  !!!  !!:  !!:  !!!     !!:  !!!  !!:       !!:       !!:               !:!  !!:       !!:  !!!  
 :!:       :!:  !:!  :!:         :!:    :!:  !:!  :!:  :!:  !:!     :!:  !:!  :!:       :!:       :!:              !:!   :!:       :!:  !:!  """)
time.sleep(1) 
print("""\033[1;33;40m  ::: :::  ::   :::   ::          ::    ::   :::   ::   ::   ::      :::: ::   :: ::::   :: ::::   ::          :::: ::    :: ::::  ::   :::  
  :: :: :   :   : :   :           :      :   : :  :    ::    :      :: :  :   : :: ::   : :: ::    :           :: : :    : :: ::    :   : :  """)
time.sleep(1) 
                                    


a = input("\n\033[1;31;40m press enter to proceed with the mission ") #first option to select following only if statement 
    
if  a == "yes":
        typingPrint("""\n\033[1;32;40m crew member: captain we shouldn't be traveling north as this time of winter .It will b all frozen and 
    we don't have that much food stock. we cant survive through this horrible weather while waiting for summer time to come!!!
    """)
elif a == "no":
        typingPrint("\n \n\033[1;32;40m Good bye!\n")
        typingPrint("This screen will clear itself in 3..") # code will clear the screen automatically
        time.sleep(1)
        typingPrint("2..")
        time.sleep(1)
        typingPrint("1..")
        time.sleep(1)
        clearScreen()
        select_north()

   

   

time.sleep(0.01) #typewriter speed
typingPrint("\n\n\033[1;32;40m do you wish to proceed north?????????") # code in start will give style and color to print statement in terminal
time.sleep(0.01)
        #level 1 option created with if else statement
x =input("\n\033[1;31;40m Type 1 for yes or 2 for no ")
if x == "1":
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

    
        typingPrint("""\n\033[1;32;40m your ship got stuck in a ice burg.....you and your crew died starving in cold.
            your ship was found by other ships when they started travelling towards north!!! 
            \n"Shall we try that again?""") 
        
        typingPrint("\n \n\033[1;32;40m Good bye!\n")
        typingPrint("This screen will clear itself in 3..") # code will clear the screen automatically
        time.sleep(1)
        typingPrint("2..")
        time.sleep(1)
        typingPrint("1..")
        time.sleep(1)
        clearScreen()
        select_north()                
        
elif  x == "2":
            typingPrint("""\n\n\033[1;32;40m it was very sensible of you to trust and listen your crew advice ...
              smart move. you gain your crew trust and now they fully trust you.You are the captain they will die for.....
            """)
            time.sleep(0.01) 
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
            typingPrint("\033[1;32;40m select your options")
else:
            typingPrint("\n\n\033[1;32;40m don't try to b extra smart crew life depends on you")
            time.sleep(0.01) 
        #level 2 
y = input("\n\033[1;31;40m pic 1 for east or 2 for west or  3 for south ")
if y == "1":
        typingPrint("""\n\033[1;32;40m
        \nafter roaming for 8 months you've found an island .this was the island you
        and your crew was searching for years now you must finish what you came for """)
        time.sleep(0.01)
        print("""\033[1;35;37m   
     __   __  _______  __   __    _     _  _______  __    _ 
    |  | |  ||       ||  | |  |  | | _ | ||       ||  |  | |
    |  |_|  ||   _   ||  | |  |  | || || ||   _   ||   |_| |
    |       ||  | |  ||  |_|  |  |       ||  | |  ||       |
    |_     _||  |_|  ||       |  |       ||  |_|  ||  _    |
      |   |  |       ||       |  |   _   ||       || | |   |
      |___|  |_______||_______|  |__| |__||_______||_|  |__|
        
        End to new beginning.........
        """)
        time.sleep(0.0001)
        typingPrint("\n\033[1;32;40m Good bye!\n")
        typingPrint("This screen will clear itself in 3..")
        time.sleep(1)
        typingPrint("2..")
        time.sleep(1)
        typingPrint("1..")
        time.sleep(1)
        clearScreen()
elif y == "2":
        typingPrint("\n\033[1;32;40m think again are you sure to proceed (press enter) ")
        time.sleep(0.01)
        input(" ")
        typingPrint("\n\n\033[1;32;40m you should think hundred time to go this direction  ")
        time.sleep(0.01)
        input("\n\n\033[1;32;40m still wants to go (y/n)")
        typingPrint(""" \n\n\033[1;32;40m In the beginning of your travel every thing goes very well you survived horrible storm 
        until you fought with kraken unluckily kraken was way too strong and you and your crew couldn't
        survive but you fought with great honour history will remember you!!!!""")
        time.sleep(0.01)
        print("""\033[1;35;37m                                       ,
                                                          ,o
                                                          :o
                                _....._                  `:o
                              .'       ``-.                \o
                              /  _      _   \                \o
                            :  /*\    /*\   )                ;o
                            |  \_/    \_/   /                ;o
                            (       U      /                 ;o
                              \            /                  /o
                              \   _m_     (                  /o
                              \          (                ,o:
                              )          \,           .o;o'           ,o'o'o.
                              ./          /\o;o,,,,,;o;o;''         _,-o,-'''-o:o.
              .             ./o./)        \    'o'o'o''         _,-'o,o'         o
              o           ./o./ /       .o \.              __,-o o,o'
              \o.       ,/o /  /o/)     | o o'-..____,,-o'o o_o-'
              `o:o...-o,o-' ,o,/ |     \   'o.o_o_o_o,o--''
              .,  ``o-o'  ,.oo/   'o /\.o`.
              `o`o-....o'o,-'   /o /   \o \.                       ,o..         o
              ``o-o.o--      /o /      \o.o--..          ,,,o-o'o.--o:o:o,,..:o
                              (oo(          `--o.o`o---o'o'o,o,-'''        o'o'o
                              \ o\              ``-o-o''''
              ,-o;o           \o  |
              /o/               /o /
              (o(               /o /                |
              \o\.       ...-o'o /             \   |
                  \o`o`-o'o o,o,--'       ~~~~~~~~\~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  ```o--'''                       \| /
                                                  |/
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                  |
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              
              
               _______       ___      .___  ___.  _______      ______   ____    ____  _______ .______         
              /  _____|     /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \        
              |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |       
              |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /        
              |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.   
               \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|   
                      
              
                  
              
                      
                      """)
        typingPrint("\n\n\033[1;32;40mGood bye!\n")
        typingPrint("This screen will clear itself in 3..")
        time.sleep(1)
        typingPrint("2..")
        time.sleep(1)
        typingPrint("1..")
        time.sleep(1)
        clearScreen()

       
      
elif y == "3":
        typingPrint("""\n\n\033[1;32;40myour crew members trusted you.you headed south with great confidence 
        discover new island called skull island you and your crew loved it very much 
        you decided to make this island your home """)
        time.sleep(0.01)
        print("""\033[1;35;37m
                        ______
                     .-"      "-.
                    /             l
        _          |              |          _
        ( \        |,  .-.  .-.  ,|         / )
        > "=._     | )(__/  \__)( |     _.=" <
        (_/"=._"=._|/     /\     \| _.="_.="\_)
              "=._ (_     ^^     _)"_.="
                  "=\__|IIIIII|__/="
                 _.="| \IIIIII/ |"=._
        _     .="_.="\          /"=._"=._     _
       ( \_="_.="     `--------`     "=._"=._/ )
        > _.="                            "=._ <
        (_/                                   \_)
    
    
     __   __  _______  __   __    _     _  _______  __    _ 
    |  | |  ||       ||  | |  |  | | _ | ||       ||  |  | |
    |  |_|  ||   _   ||  | |  |  | || || ||   _   ||   |_| |
    |       ||  | |  ||  |_|  |  |       ||  | |  ||       |
    |_     _||  |_|  ||       |  |       ||  |_|  ||  _    |
      |   |  |       ||       |  |   _   ||       || | |   |
      |___|  |_______||_______|  |__| |__||_______||_|  |__|
        
    
                                    
    """)
        time.sleep(0.01)
        typingPrint("\n\033[1;32;40m Good bye!\n")
        typingPrint("This screen will clear itself in 3..")
        time.sleep(1)
        typingPrint("2..")
        time.sleep(1)
        typingPrint("1..")
        time.sleep(1)
        clearScreen()
else:
        typingPrint("\n\n\033[1;32;40m if you cant type 1, 2 or 3 you have no rights to play this game ")
        time.sleep(0.5)
        typingPrint("""\033[1;35;37m game over 
     _______       ___      .___  ___.  _______      ______   ____    ____  _______ .______         
    /  _____|     /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \        
    |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |       
    |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /        
    |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.   
     \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|   
                                                                                                    
        """)
        time.sleep(0.0001)
        typingPrint("\nGood bye!\n")
        typingPrint("\n\033[1;32;40m This screen will clear itself in 3..")
        time.sleep(1)
        typingPrint("2..")
        time.sleep(1)
        typingPrint("1..")
        time.sleep(1)
        clearScreen()
select_north()
