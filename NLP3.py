
# Python-এ দুটি Identity Operator আছে:

# * `is` → দুটি ভেরিয়েবল একই অবজেক্টকে নির্দেশ করলে `True` দেয়।
# * `is not` → দুটি ভেরিয়েবল ভিন্ন অবজেক্টকে নির্দেশ করলে `True` দেয়।

# উদাহরণ:

#python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False
print(a == c)      # True


# **ব্যাখ্যা:**

# * `a is b` → `True`, কারণ `a` এবং `b` একই অবজেক্টকে নির্দেশ করছে।
# * `a is c` → `False`, কারণ `a` ও `c` আলাদা অবজেক্ট, যদিও তাদের মান একই।
# * `a == c` → `True`, কারণ তাদের মান (value) সমান।

# **সংক্ষেপে:**

# * `==` → মান (value) তুলনা করে।
# * `is` → অবজেক্টের পরিচয় (identity) তুলনা করে।





a = [1,2,3]
b = [1,2,3]
c = a

print(a == b)
print(a is b)

print(type(a))
print(type(b))
print(id(a))
print(id(b))

print(a is c)
print(a==c and a is c)



result = None

if result is None:
    print("no result")

if result == None:
    print("No result")


x = 256
y = 256

print(x is y)

x = 299
y = 299

print(x is y)


# আপনি যদি array/list-এর ক্ষেত্রে is ব্যবহার করেন, তাহলে False আসার কারণ হলো দুটি আলাদা list/array একই মান ধারণ করলেও তারা সাধারণত আলাদা অবজেক্ট।

# উদাহরণ:

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

# এখানে:

# a == b → True, কারণ দুই list-এর মান একই।
# a is b → False, কারণ a এবং b মেমরিতে দুটি ভিন্ন object।

#Membership Operator
# Python-এ Membership Operator ব্যবহার করা হয় কোনো উপাদান (element) একটি sequence-এর (যেমন list, tuple, string, set) মধ্যে আছে কিনা তা পরীক্ষা করার জন্য।

# দুটি Membership Operator আছে:

# in → উপাদানটি থাকলে True দেয়।
# not in → উপাদানটি না থাকলে True দেয়।

name = "AAbdullaah"
print('A' in name)


fruits = ['apple', 'banana', 'mango']

print("apple" not in fruits)



allowed_user = ['admin','Noman','Arafat','Riya','sojib']
user = "admin"
if user in allowed_user:
    print("Access granted!!")




#Bitwise operator 


# 1. Bitwise AND (&)

# দুটি বিটই 1 হলে ফল 1।

a = 5      # 101
b = 3      # 011

print(a & b)   # 1
# 101
# 011
# ---
# 001 = 1



# 2. Bitwise OR (|)

# যেকোনো একটি বিট 1 হলে ফল 1।

print(5 | 3)   # 7
# 101
# 011
# ---
# 111 = 7



# 3. Bitwise XOR (^)

# দুটি বিট ভিন্ন হলে 1।

print(5 ^ 3)   # 6
# 101
# 011
# ---
# 110 = 6


# 4. Bitwise NOT (~)

# সব বিট উল্টে দেয়। ~5 এর ফল -6 কেন হয়, এটা বুঝতে হলে Two's Complement ধারণাটা জানতে হবে।

# ধরি:

# 5 = 00000101

# Bitwise NOT (~) সব বিট উল্টে দেয়:

# ~5

# 00000101
# ↓
# 11111010

# এখন 11111010 একটি negative number (Two's Complement representation)।

# এর মান বের করতে:

# সব বিট উল্টাও:

# 11111010
# ↓
# 00000101

# 1 যোগ করো:

# 00000101 + 1 = 00000110
# অর্থাৎ মান = 6
# যেহেতু এটি negative representation ছিল, তাই ফল:
# -6

# তাই:

# print(~5)

# আউটপুট:

# -6

print(~5)   # -6



# 5. Left Shift (<<)

# বিটগুলোকে বামে সরায়। হ্যাঁ, << (Left Shift) অপারেটর বিটগুলোকে বামে সরিয়ে দেয়।

# উদাহরণ:

# print(5 << 1)

# প্রথমে 5-কে বাইনারিতে লিখি:

# 5 = 101

# এখন << 1 মানে সব বিটকে ১ ঘর বামে সরানো:

# 101  →  1010

# এখন 1010-এর দশমিক মান:

# 1×2³ + 0×2² + 1×2¹ + 0×2⁰
# = 8 + 0 + 2 + 0
# = 10

# তাই:

# print(5 << 1)   # 10

# আরও উদাহরণ:

# print(5 << 2)   # 20
# 5      = 101
# 5 << 2 = 10100

# 10100 = 20

# সহজ নিয়ম
# n << 1 = n × 2
# n << 2 = n × 4
# n << 3 = n × 8

print(5 << 1)   # 10
# 5  = 101
# 10 = 1010



# 6. Right Shift (>>)

# বিটগুলোকে ডানে সরায়। হ্যাঁ >> (Right Shift) অপারেটর বিটগুলোকে ডানে সরিয়ে দেয়।

# উদাহরণ:

# print(5 >> 1)

# প্রথমে 5 কে বাইনারিতে লিখি:

# 5 = 101

# এখন >> 1 মানে সব বিট ১ ঘর ডানে সরানো:

# 101 → 10

# এখন 10 এর দশমিক মান:

# 1×2¹ + 0×2⁰ = 2

# তাই:

# print(5 >> 1)   # 2
# সহজ নিয়ম
# n >> 1 = n ÷ 2
# n >> 2 = n ÷ 4
# n >> 3 = n ÷ 8

print(5 >> 1)   # 2



a = 5
b = 3

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2

# মনে রাখার সহজ উপায়:

# & → AND (দুটোই 1)
# | → OR (যেকোনো একটি 1)
# ^ → XOR (ভিন্ন হলে 1)
# ~ → NOT (উল্টে দেয়)
# << → বামে সরায় (গুণ 2-এর মতো)
# >> → ডানে সরায় (ভাগ 2-এর মতো)








#conditionaal / control flow : Python-এর control flow-এর প্রধান অংশগুলো হলো:

# if
# if-else
# if-elif-else
# Nested if
# for loop
# while loop
# break
# continue
# pass


#example 1

age = 21

if age>=18:
    print("you are adult!!!")
elif age == 15:
    print("You have to wait")
else:
    print("you are not adult!!")

#example 2

age = 17
if age==17:
    print(f"your age is {age}")
elif age == 12:
    print(f"your age is {age}")
else:
    print("You are adult")


#nested if 


age = 20

has_id = True

if age>=18:
    if has_id:
        print("pass!!!")
    else:
        print("Don't have ID")
else:
    print("you are not aadult!!!!!")


#Python-এ Ternary Operator (বা Conditional Expression) এক লাইনে if-else লেখার জন্য ব্যবহার করা হয়।

age = 12

status = "Adult" if age>=18 else "Not Adult"  # jeta true seta first e lekha hbe

print(status)

# match case

#example 1

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _: #underscore default dite hoy
        print("Invalid day")



#exaample 2


 letter = "a"

match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")       





