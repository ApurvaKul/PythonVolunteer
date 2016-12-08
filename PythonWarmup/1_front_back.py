def front_back(str):
    if(len(str)>0):
        ustring = str
        front = str[0]
        last = str[len(str)-1]
        ustring= last[0]+ustring[1:]
        ustring = ustring[:len(ustring)-1]+front
        return ustring;
    else:
        return str;


print(front_back(""))
