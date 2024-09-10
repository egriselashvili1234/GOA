number = 1
jami = 0
for i in range(10):
    jami = jami + number
    print(jami)
    number += 1
print()
for number in range(1, 1001):
    if number == 100:
        continue
    print(number)
print()
for number in range(100, -1, -1):
    print(number)
print()
count = 1
while count <= 10:
    print(count)
    print("Hello world!")
    count += 1