import re

pattern_phone = re.compile(r"09\d{2}-\d{3}-\d{3}|\+886-9\d{2}-\d{3}-\d{3}")

user = input("請輸入手機號碼: ")

matched = pattern_phone.findall(user)
print("符合格式的電話號碼:", matched)

