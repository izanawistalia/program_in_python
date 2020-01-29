import re #import library for regular expression

test = 'randOm string is given inside  random string you in_si-de@example.com more random stings and yourname@neha.in this is more rubbish'
pattern = re.compile('[a-zA-Z0-9\-\_\@\.]+@+[a-zA-Z0-9]+\.+[a-zA-Z0-9]+')

result = pattern.findall(test)

print(result)

