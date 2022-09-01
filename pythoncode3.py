siblings_brother=('Irfan', 'Javed', 'Ezaz', 'Waseem')
siblings_sister=('Ibtisaam','Shaheen', 'Sameena', 'Saba')

#joining two tuples
siblings = siblings_brother+siblings_sister
print(siblings)

#length of tuple siblings
count=len(siblings)
print(count)

#modifying and adding father's and mother's name
family_members = siblings + ('Hasina', 'Shamsh')
print(family_members)
