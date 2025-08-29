str1="Hello123"
print(str1.isalnum())  # True, because all characters are alphanumeric
str2="Hello 123"
print(str2.isalnum())  # False, because of the space
str3="Hello@123"
print(str3.isalnum())  # False, because of the special character '@'
str4="/u00B23"
print(str4.isalnum())  # False, because of the special character '/'
print(str4.isupper())  # False, because it contains lowercase letters and special characters
str5="HELLO"
print(str5.isupper())  # True, because all characters are uppercase
tuple1 = (str1, str2, str3, str4, str5)
print(tuple1)
tuple2=()
print(tuple2)
tuple3=("B")
print(tuple3)
lang=("Python", "Java", "JavaScript")
print(lang[0:5])
print(max(tuple1))
str="Lang"
t1=tuple(str)
print(t1)