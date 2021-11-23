# Arrange a word such that character(ASCII value) is in ascending order.


sample_string = input("Enter String")
ascii_values = [ord(i) for i in sample_string]
sorted_values = ascii_values.sort()
char_values = [chr(i) for i in ascii_values]
result = ''.join(char_values)
print(result)

# other simple method:

# sample_string = input("Enter String")
# sorted_string = list(sample_string)
# sorted_string.sort()
# print(''.join(sorted_string))
