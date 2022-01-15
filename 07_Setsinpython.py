'''
Important
a={}   This is an empty dictionary
b=set() This is an empty dictionary
'''
b=set()
b.add(45)
b.add(23)
b.add(453)
b.add(23455)
#b.add([4'5'6]
#list cant be added into set as list in non hashable
#but tupple can be added as tupple cant be changed and so set
b.add((3,7,8,9))

print(b)
