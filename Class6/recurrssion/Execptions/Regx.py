import Regx as re
print(re.macth(r'^[a-zA-Z0-9]+$', 'Hello123'))  # True
print(re.macth(r'^[a-zA-Z0-9]+$', 'Hello 123'))  # False
print(re.macth(r'[A-Z]+', 'Hello'))  # True
print(re.macth(r'[A-Z]+', 'hello'))  # False
print(re.macth(r'\d+', '12345'))  # True
print(re.macth(r'\d+', 'abc'))  # False

print(re.match(r'^\d', '5days'))
print(re.match(r'.+', ''))
#some more explaination of regex
print(re.match(r'\d{3}', '4abc123333'))
print(re.match(r'\d{2,4}', '1abc'))
print(re.match(r'\d{2,4}', '12345abc'))