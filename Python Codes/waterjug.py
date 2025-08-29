print("Water Jug problem")
x=int(input("Enter X:"))
y=int(input("Enter Y:"))
while True:
    print("Select the rule to apply: ")
    print("1: Fill Jug X")
    print("2: Fill Jug Y ")
    print("3: Empty Jug X")
    print("4: Empty Jug Y")
    print("5: Fill Jug X from Jug Y")
    print("6: Fill Jug Y from Jug X")
    print("7: Empty Jug Y into Jug X")
    print("8: Empty Jug X into Jug Y")
    rule=int(input("Enter the rule to be fired: "))
    if rule==1:
        if x<4:
            x=4
    if rule==2:
        if y<3:
            y=3
    if rule==3:
        if x>0:
            x=0
    if rule==4:
        if y>0:
            y=0
    if rule==5:
        if x+y>=4 and y>0:
            x,y=4,y-(4-x) #x value is same but y= y-(4-x)
    if rule==6:
        if x+y>=3 and x>0:
            x, y=3,x-(3-y)
    if rule==7:
        if x+y<=4 and y>0:
            x, y=x+y, 0
    if rule==8:
        if x+y<=3 and x>0:
            x, y=0, x+y
    print("Jug X=", x)
    print("Jug Y=",y)
    if (x==2):
        print("The result is the goal state")
        break
