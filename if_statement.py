value = 200

if value > 75: # block statement
    print("kangaroo")
    print("koala")
elif value > 50:
    print("wombat")
    print("wallaby")
    if value > 60:
        print("quokka")
else:
    print("platypus")

print("ALL DONE")

#  A ? B : C

#  B if A else C

DEBUG = ""

font_color = "red" if DEBUG else "green"
print("red" if DEBUG else "green")

# == != < > >= <= 

# foo <> bar

# and or not

a = 5
b = 10
print(a and b)
print(a or b)

if (value > 50) and (value < 80):
    pass
