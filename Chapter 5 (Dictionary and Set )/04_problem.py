"""
What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
"""

u=set()
u.add(10)
u.add(10.0) # 10 == 10.0
u.add("10")

print(len(u))