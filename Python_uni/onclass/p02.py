import re

pattern_ipv4 = re.compile(r'((1?\d{,2}|2[0-4][0-9]|25[0-5])\.){3}(1?\d{,2}|2[0-4][0-9]|25[0-5])')

user = input("請輸入IP位址: ")

if matched := pattern_ipv4.match(user):
    print(matched.group())
else:
    print("Unpass")