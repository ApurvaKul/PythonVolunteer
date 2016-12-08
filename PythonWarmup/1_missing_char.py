def missing_char(str, n):
    if(n<len(str)):
        if(n == 0):
            ustr = str[n+1:len(str)]
            return ustr;
        else:
            ustr=str[:n]
            ustr = ustr[:n]+str[n+1:len(str)]
            return ustr;
    else:
        return "Not valid number";

print(missing_char("I am a Girl",5))