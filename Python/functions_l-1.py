def cut_cake(num, parts):
    try:
        return num / int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return "Не допустимое действие!"   

x = cut_cake(2, 2)  
print(x)       

def do_something(x):
    try:
        print(x)    

x = 0
while x <= 10:
    do_something(x)
    x += 1 
       