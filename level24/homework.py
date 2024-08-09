my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list)

first_three = my_list[:3]
print("First three elements:", first_three)

last_three = my_list[-3:]
print("Last three elements:", last_three)

middle_four = my_list[3:7]
print("Middle four elements:", middle_four)

first_three_neg = my_list[-10:-7]
print("First three elements (negative indices):", first_three_neg)

last_three_neg = my_list[-3:]
print("Last three elements (negative indices):", last_three_neg)

middle_four_neg = my_list[-7:-3]
print("Middle four elements (negative indices):", middle_four_neg)

string = 'Python is da GOAT'

word1 = string[0:6]
word2 = string[7:9]
word3 = string[10:12]
word4 = string[13:16]

print("Word 1:", word1)
print("Word 2:", word2)
print("Word 3:", word3)
print("Word 4:", word4)

greeting = 'Hello World!'

for i in greeting:
    print(i)

i = 1

while i <= 10:
    print(i)
    i += 1

x = 1

while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

total = 0
num = 1

while total < 50:
    total += num
    num += 1

print('Sum:', total)