import math
def eval_loop():
    
    while True:
        input1 = input("Enter a string: ")
        if input1 == 'done':
            break
        else:
            print(eval(input1))
    

eval_loop()
