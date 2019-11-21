#main progam file #run
from AziziFunctions import*

'''
turtle.bgcolor("sienna")
'''
bob.speed(0)

jump(0,365)

#text of "Louis Vuitton"

bob.color("darkgoldenrod")
bob.write("Louis Vuitton", align="center", font=(None, 30, "bold"))


#outline for the "LV #for reference





jump (150,150)
for times in range(4):
    bob.right(90)
    bob.forward(300)

jump(0,0)


#The "L" In LV

#head

#Top part or head of the "L"

#right half head
jump(-10,95)

bob.left(180)
bob.forward(40)
bob.right(180)
bob.forward(80)
bob.right(100)
bob.forward(10)
bob.right(80)
bob.forward(15)

#left half head
jump(-50,95)

bob.left(100)
bob.forward(10)
bob.left(80)
bob.forward(15)

#body

#middle part of the "L"

#left head conversion

for times in range(5):
    bob.right(20)
    bob.forward(3)

bob.forward(125)

#right head conversion

jump(13,85)
bob.right(80)

for times in range(4):
    bob.left(20)
    bob.forward(3)
bob.forward(150)

#tail

#bottom part of "L"

#left tail conversion

bob.pu()
bob.right(180)
bob.forward(25)
bob.left(100)
bob.forward(31)
bob.left(80)
bob.forward(2)
bob.pd()

for times in range(16):
    bob.right(5)
    bob.forward(1.5625)


bob.forward(25)
bob.left(90)
bob.forward(20)
bob.left(90)
bob.forward(200)


#right tail conversion

#reverting the left tail conversion back to the right tail

bob.pu()
bob.right(180)
bob.forward(200)
bob.right(90)
bob.forward(20)
bob.right(90)
bob.forward(25)

for times in range(16):
        bob.left(5)
        bob.forward(1.5625)
jump(-20,-70)
bob.right(180)

#going from right body to right tail

bob.left(100)
bob.forward(50)

for times in range(15):
    bob.forward(7)
    bob.left(6)

bob.right(90)
bob.forward(10)
bob.right(90)
bob.forward(77)



#v

jump(30,120)

bob.left(90)
bob.forward(60)
bob.right(90)
bob.forward(10)

bob.right(90)
bob.forward(5)

for times in range(15):
    bob.forward(2)
    bob.left(5)

bob.forward(150)

bob.right(75)
bob.forward(30)
bob.right(55)
bob.forward(180)

for times in range(9):
    bob.left(6)
    bob.forward(2)

bob.forward(5)
bob.right(90)
bob.forward(16)
bob.right(89)
bob.forward(70)
bob.right(90)
bob.forward(10)
bob.right(90)
bob.forward(10)

for times in range(15):
    bob.forward(1)
    bob.left(8)


bob.left(3)
bob.forward(165)

bob.left(133)
bob.forward(143)

for times in range(15):
    bob.forward(.74)
    bob.left(6.6)

bob.forward(15)

bob.right(90)
bob.forward(16)


