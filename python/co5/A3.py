def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
          factorslist.append(i)
    return(factorlist)
def isprime(n):
  return(factors(n) == [1,n])
def primeproduct(n):
  for i in range(1,n+1):
    if n%i == 0:
      if isprime(i) and isprime(n//i):
        return(True)
  return(False)
def delchar(s,c):
  if len(c) != 1:
    return(s)
  snew = ""
  for char in s:
    if char != c:
      snew = snew + char
  return(snew)
def shuffle(l1,l2):
  if len(l1) < len(l2):
    minlength = len(11)
  else:
    minlength = len(12)
  shuffled = []
  for i in range(minlength):
    shuffled.append(l1[i])
    shuffled.append(l2[i])
  shuffled = shuffled + l1[minlength:] + l2[minlength:]
  return(shuffled)