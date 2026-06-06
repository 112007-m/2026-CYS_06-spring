print(type(S))

a = set([1,2,3,4])
print(a)
print(type(a))

S = {"CE","CS","CYS","ISE","AE"}
print(S)
for i in S:
    print(i)
if "CE" in S:
    print("CE in S")
else:
    print("CE is not in S")


S.add("RT")
print(S)

S.discard("RT")
print(S)


S.remove("CE")
print(S)

S.pop("CE")
print(S)


S.clear()
print(type(S))

s1 = {"Fizza","Mishkat","Hania"}
s2 = {5,4,18}
s3 = {"A","B","C"}
s4 = {1,"cat",[1,2,3]}
print(set.union(s1,s2,s3))


s1.update(s3)
print(s1)

set.intersection_update(s1,s2,s3)
print(s1)

s1 = {2,3,4}
s2 = {5,4,18}
s1.intersection_update(s2)
print(s1)

w = s1.symmetric_difference(s2)
print(w)

s = s1.difference(s2)
print(s1)

a = s1.isdisjoint(s2)
print(a)

s1 = {1,2,3}
s2 = {4,5,6}
a = s1.isdisjoint(s2)
print(a)


s2 = {1,2,3}
s1 = {1,2,3,4,5}
a = s2.issubset(s1)
print(a)