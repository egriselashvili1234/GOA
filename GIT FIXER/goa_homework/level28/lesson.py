
text = "Hello, World!"

# .upper() - ტექსტი გარდაქმნის დიდ ასოებში
print(text.upper())


text2 = "GURAMI SQUAD BEST"

# .lower() - ტექსტი გარდაქმნის პატარა ასოებში
print(text2.lower()) 

text3 = "hELLO SPONGEBOB"

# .capitalize() - ტექსტის პირველი ასო გადააქცევს დიდად, დანარჩენები დარჩება პატარა
print(text3.capitalize())

text4 = "Nikoloz Best"

# .swapcase() - ტექსტის ყველა დიდი ასო პატარა და პირიქით
print(text4.swapcase())

# .find() - ეძებს სტრიქონს და აბრუნებს მის ინდექსს, თუ ვერ იპოვა, აბრუნებს -1
print(text.find("World"))  # 7
print(text.find("world"))  # -1

text5 = "Fish"

# len() - აბრუნებს სიმბოლოების რაოდენობას სტრიქონში
print(len(text5))
my_list = ["apple", "banana", "cherry"]

# 2. დაამატოთ ახალი ელემენტი სიის ბოლოში
my_list.append("pineapple")
print(my_list)  

# 3. დაამატოთ ახალი ელემენტი სიის ინდექსზე 1
my_list.insert(1, "Watermelon")
print(my_list)  

# 4. წაშალოთ ელემენტი სიის ინდექსზე 3
removed_element = my_list.pop(3)
print(removed_element)  
print(my_list)  

# 5. გამოთვალოთ სიის რაოდენობა
print(len(my_list))
