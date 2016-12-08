def front3(str):
    if(len(str)<3):
        ustring = str + str + str
        return ustring;
    else:
        ustring = str[0:3]
        ustring = ustring + ustring + ustring
        return ustring;

print(front3("Ja"))