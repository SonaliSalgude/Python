fruits = {1:"Grapes",2:"Mango",3:"Apple",4:"Banana"}
print("Given dictionary",fruits);

d2=fruits.copy()
print("New dictionary",d2)

d3 = {'coding':'good','thinking':'better'}
print(d3.get('coding'))

d4 = { 1: 'C', 2: 'C++', 3: 'Java' }
print("Dictionary items:")
print(d4.items())

print(d4.keys())

d5 = {4:'Python'}
d4.update(d5)
print("Updated Dictionary",d4)

d6 = {"Marathi":1,"English":2,"Maths":3,"History":4}
print(d6.values())