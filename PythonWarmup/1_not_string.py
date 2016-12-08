def not_string(str):
    if(str[0:3] == "not" or str[0:3] == "Not"):
        return str;
    else:
        u_str  = "not "
        u_str = u_str[:4] + str
        return u_str;

print(not_string("Hi"))
print(not_string("not me"))

