def sum_double(a, b):
    c = 0;
    if (a != b):
        c = a + b
        return c;
    else:
        c = 2 * (a + b)
        return c;


d=0
print(d);
d=sum_double(1, 2)
print(d)
d=sum_double(3, 2)
print(d)
d=sum_double(3, 3)
print(d)
