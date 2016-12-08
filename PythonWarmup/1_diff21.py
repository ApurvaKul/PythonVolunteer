def diff21(n):
    c = 0
    c=abs(21-n)
    if(n>21):
        return 2*c;
    else:
        return c;

print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(32))
