num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")

num1 = num1[::-1]
num2 = num2[::-1]

length = max(len(num1),len(num2))

if num1 != num2:
    num1 = num1.ljust(length, '0')
    num2 = num2.ljust(length, '0')

carry = 0

ans = ''

for i in range(length):
    
    ans += str((int(num1[i])+int(num2[i])+carry)%10)
    
    if(int(num1[i])+int(num2[i])+carry>=10):
        carry = 1
    else:
        carry = 0

print("Sum: ",ans[::-1])