def press_grind_coffee():
    print("grind for 20 seconds")

press_grind_coffee()

def say_hello():
    print("hello")

say_hello()


def widrawls_from_bank(amount,acc):
    print(f"widraw {amount} from acc {acc}")
 
widrawls_from_bank(300,123456789)

#activity 1

def coffee_order(size,drink):
    print(f"i want {size} {drink}")
coffee_order("large","latte")


def add_up(num1,num2):
    return num1 +num2
add_up(0,0)
print(add_up(5,5))

#activity 1
counter = 0
def take_order(topping):
    global counter 
    print(f"pizza with {topping}")
    counter += 1
take_order("pine apple")
print(counter)

#output pizza with pine apple
#1

#activity 2
pin = 1234
remaining_amount =1000
def cash_machine(pin_num ,amount):
      
      global remaining_amount,pin
      
    
      if pin_num == pin and  amount <= remaining_amount:
         remaining_amount = remaining_amount - amount
         print("Pin number is correct.withdrawls granted") 
      else:
         print("wrong pin number")
      

cash_machine(1234,12)
print("remaining amount in your acc is",remaining_amount)

#output 
     #Pin number is correct.withdrawls granted
     #remaining amount in your acc is 300
