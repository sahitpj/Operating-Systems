

f = open('users.txt')
l = f.readlines()

s = list(set(l))
print len(s)
