def fcat(a):
    if a==1:
        return a
    else:
        return a*fcat(a-1)
a = int(input("enter "))
print("fcatorial is",fcat(a))