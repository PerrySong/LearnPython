def collatz(number):
  if number % 2 == 0:
    print(number)
    return number // 2
  else:
    print(number)
    return number * 3 + 1

while True:
  number = int(input("please enter a number: "))
  if collatz(number) == 1:
    break
print("succeed")