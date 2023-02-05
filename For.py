#for

liste = [3,4]

for i in liste:
    print(i)



for s in range(10):
 print(s)


liste1 = ["a","b","c"]
liste2 = [1,2,3]

for harf in liste1:
    for rakam in liste2:
        print(harf,rakam)



liste3 = [1,2,3,4,5,6,7,8,9,]

for c in liste3:
    if c == 3:
        print("3ü atladık")
        continue
    print(c)



liste5 = range(100)

for g in liste5:
  if g % 3 !=0:  
    continue
  if g == 81:
    break
print(g)