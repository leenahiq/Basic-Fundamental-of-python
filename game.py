def start_game():
    def introduction(): # introduction
        print("Welcome!")
        # Move on to function1
        function1()
    def function1(): # character
        # We succeeded, move on
        pass
        # Call function2
        function2()
    def function2(): # level 1
        print("Do you want to continue?")
        choice = input("Please enter your name")
        # Enter KEIRA and get the introduction, otherwise move on
        if choice.upper() == "keira":
            introduction()
        else:
            function3()
    def function3(): # level 2
        # We did a thing!
        pass
    introduction()
start_game()


print("""
              _,.
            ,` -.)
           ( _/-\\-._
          /,|`--._,-^|            ,
          \_| |`-._/||          ,'|
            |  `-, / |         /  /
            |     || |        /  /
             `r-._||/   __   /  /
         __,-<_     )`-/  `./  /
        '  \   `---'   \   /  /
            |           |./  /
            /           //  /
        \_/' \         |/  /
         |    |   _,^-'/  /
         |    , ``  (\/  /_
         \,.->._    \X-=/^
         (  /   `-._//^`
         `Y-.____(__}
          |     {__)
                ()
    """)


print("""

        \|\||
       -' |||/
      /7   |||/
     /    |||||/
     \-' |||||||/`-.____________
      -|||||||||           /    `.
        |/||||             \      |
 _______/    /_       ______\      |__________-
(,__________/  `-.___(,_____________----------_)
    
    """)




