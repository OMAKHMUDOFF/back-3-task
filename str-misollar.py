"""1 misol"""

phoneNum = input("Telofon raqamingizni to'liq kiriting : ")
print(phoneNum[4:6])

"""2 misol"""

text = "Bugun ob-havo yaxshi, demak barchamiz Lola bilan aylanishga chiqsak bo'ladi"
textLength = len(text)
print(text[38:42])  # 1
print(text.replace("Lola", "Tohir"))  # 2
print(textLength)  # 3
print(text.startswith("A"))  # 4
print(text.endswith("i"))  # 5
newText = text.replace("B", "M", 1)
print(newText.startswith("M"))  # 6
newText = text.replace("i", "", -1)
print(newText.endswith("i"))  # 7
print(text.upper())  # 8
if textLength % 2 == 0:
    print("Juft")
else:
    print("Toq")
print(text.count("a"))  # 10
print(text.count("u"))  # 11
print(
    "Bugun ob-havo {}, demak barchamiz Lola bilan aylanishga chiqsak bo'ladi".format(
        "yomon"
    )
)  # 12


"""3 misol"""
car = "Tohirda 15 ta yangi malibu bor. lekin uning dadasi damas minishni yoqtiradi. shunday emasmi?"
print(car.find("malibu"))
print(car[20:26])  # 1
print(car.find("damas"))  # 2
print(car[51:56])
print(car.replace("malibu", "damas"))  # 3
print(car.replace("damas", "malibu"))  # 3

"""4 misol"""
text = "anvarning otasiga haydovchidir. lekin undagi ko'p pul bor"
print(text[0:5] + text[9:42] + text[44:])  # 1
print(text.replace("a", "A", 1).replace("l", "L", 1))  # 2
print(len(text.replace(" ", "")))  # 3

"""5 misol"""
text1 = "Multfilm kinodan yaxshiroq chunki multfilmdagi voqea noreal va undagi sahnalar noreal"
text2 = "Kinodagi haqiqiy lekin undagi sahnalar noreal, odamlar noreallikdagi reallikka ko'proq ishonishadi"

print((text1 + text2).count(" "))  # 2
print(len((text1 + text2).split(" ")))  # 3
print(text.count("multfilm"))  # 4

"""String slice, replace"""

str = "anvarning otasiga haydovchidir. lekin undagi ko'p pul bor"
str2 = "salom"
aka = "aka oka uka ona ota aka uka uka aka"
number = "1739"

print("+" + str[1:] + str[:56] + "+")  # 1
# print(list(str))
# print(str.replace("", "0"))  # 2 oxshamadi
# print(len(str) // 2)
print("+" + str[1:27] + "+" + str[29:56] + "+")  # 3
print(
    f"Bosh elem = {str[0]}\nO'rta elem = {str[len(str) // 2]}\nOxirgi elem = {str[len(str)-1]}"
)  # 4
print(str[:28] + str2 + str[28:56])  # 5
print(aka.count("aka"))
print(f"{number} -> {number[2] + number[3] + number[0] + number[1]}")  # 7
# print(str.replace(str[1:], "$"))  # 8
palindrome = "tarvuz"
print(palindrome ==  palindrome[::-1])  # 9
# 10
