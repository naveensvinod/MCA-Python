str = "this is a sample of text is"
c = dict()
txt = str.split(" ")
for t in txt:
    if t in c:
        c[t] += 1
    else:
        c[t] = 1
print(c)