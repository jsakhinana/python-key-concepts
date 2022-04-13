myset={1,35,356,344,34,1,35,35,"Raj"}

# set is unordered
# set cannot have duplicates

print(myset)

myset.add(99)
myset.discard(344)

print(myset)

for x in myset:
    print(x)