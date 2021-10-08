***targil 8 page 25:
  
x = int(input("please enter a number"))
min = x

while x > 0:

    if x < min:
        min = x

    x = int(input("please enter a number"))

if min > 0:
    print(min)
    
    
****targil 9 page 25

x = int(input("please enter a number"))

max = x
i = 1
counter = i

while i < 3:
    x = int(input("please enter a number"))
    i = i + 1
    if x > max:
        max = x
        counter = i

print(counter)



****targil 10 page 25

x = int(input("please enter a number"))
digit = 0

if x < 0:
    x = x * (-1)
    
while True:
    if x <10:
        break
    else:
        x = x // 10

print(x)


****targil 11 page 25

x = int(input("please enter a number"))
digit = 1

if x < 0:
    x = x * (-1)

while True:
    if x < 10:
        break
    else:
        digit += 1
        x = x // 10

print(digit)

*****targil 12 page 25:
  
  x = int(input("please enter a number"))
sum = 0
digit = 0

if x < 0:
    x = x * (-1)

while True:
    if x > 0:
        digit = x % 10
        sum = sum + digit
        x = x // 10
    else:
        break

print(sum)

*****targil 2 page 29

1.  81
2.  64


targil 3 page 29 


sum = 0

while True:
    x = int(input("please enter a number"))

    if x < 0:
         break
    else:
         sum = sum + x

print(sum)

*****targil 2

while True:
     first_num = 0
     second_num = 0

     while first_num == 0:
          first_num = int(input("please enter first number: "))

     while second_num == 0:
          second_num = int(input("please enter second number: "))

     if first_num > second_num:
          print("bigger")
          continue
     else:
          break
