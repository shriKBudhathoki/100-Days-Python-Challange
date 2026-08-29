#Can you change the values inside a list which is contained in set s 
# s={8,7,12,"Harry",[1,2]}

s={8,7,12,"Harry",[1,2]}
s[4]="Ram"
print(s)

"""

because sets don't have indexes.


1. You cannot put a list inside a set
==> TypeError: unhashable type: 'list'

8 → ✅
7 → ✅
12 → ✅
"Harry" → ✅
[1, 2] → ❌ list is mutable

2. You cannot access a set using an index

Even if we changed the list to a tuple:

s = {8, 7, 12, "Harry", (1, 2)}

this would still be wrong:

s[4] = "Ram"



Unlike a list:

my_list = [8, 7, 12, "Harry"]
my_list[3] = "Ram"   # ✅


"""
