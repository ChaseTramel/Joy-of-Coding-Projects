# A python program that creates an ASCII pyramid
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

def pyramid(symbol, number):
    for i in range(number):
        print(symbol * (i + 1))
    return

pyramid("^", 40)
