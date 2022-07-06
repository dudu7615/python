from random import shuffle


a = '''AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890 ,./;'\[]-=`~!@#$%^&*()_+{}:"|<>?'''
c = []
for b in a:
    c.append(b)

print(c)
shuffle(c)
print(c)
shuffle(c)
print(c)
shuffle(c)
print(c)
shuffle(c)
print(c)
