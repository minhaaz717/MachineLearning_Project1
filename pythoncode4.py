it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("length of it_companies: {len(it_companies)}")

#adding twitter to it_companies
it_companies.add('Twitter')

#updating multiple companies
it_companies.update(['Accenture', 'Wipro', 'TCS', 'Capgemini'])
print(it_companies)

#deleting a company
it_companies.remove('Apple')
print(it_companies)
#remove() method will raise an error if the specific item does not exist where as discard() method does not raise an error

C=A.union(B) #union
print(C)

D=A.intersection(B) #intersection
print(D)

E=B.issubset(A) #False
print(E)

F=B.isdisjoint(A) #False
print(F)

#join set A with set B and set B with set A
A.update(B)
print(A)

B.update(A)
print(B)

#symmetric difference
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
H=A.symmetric_difference(B)
print(H)

#deleting sets
A.clear()
B.clear()

#Convert the ages to a set and compare the length of the list and the set
print(f"the length of the list: {len(age)}")
age=set(age)
print(f"the length of the set: {len(age)}")