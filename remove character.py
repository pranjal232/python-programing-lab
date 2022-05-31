String1 = "r@jveer$ingh1234"
String2 = ''
for i in String1:
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        String2+=i
print('Alphabets in string are :' + String2)
