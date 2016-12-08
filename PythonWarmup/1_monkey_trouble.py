def monkey_trouble(a_smile,b_smile):
    trouble = False
    if(a_smile and b_smile):
        trouble = True
    elif(not a_smile and not b_smile):
        trouble = True
    return trouble;

monkey_trouble(False, False)
monkey_trouble(True,False)
monkey_trouble(False, True)

