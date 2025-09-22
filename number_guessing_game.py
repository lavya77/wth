import random
print("Welcom!!")
a= int(input("Enter the lower limit of number you want to guess"))
b=int(input("Enter the upper limit of number you want to guess"))
print("Your Limit is", a ,"to", b);
desired_num=random.randint(a,b)
print(desired_num);
count = 0;
while True:
    num = int(input("Enter a number you want to guess"))
    count+=1
    if num > desired_num:
        print("Your guess id too high");
    elif num < desired_num:
        print("Your guess is too low");
    else:
        print("Wow!! You guessed correct! in {count}",count);
        break

