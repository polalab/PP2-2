"""Tuples"""

capitals = ('Warsaw', 'Riga', 'Amsterdam', 'Berlin')
print(capitals[1])

# Nested Tuples
country_capitals = (('Poland', 'Warsaw'), ('Latvia', 'Riga'), ('The Netherlands', 'Amsterdam'), ('Germany', 'Berlin'))

# Different types:

country_capitals_list = (['Poland', 'Warsaw'], ['Latvia', 'Riga'], ['The Netherlands', 'Amsterdam'], ['Germany', 'Berlin'])
# Now you can change inside:
country_capitals_list[3].append('The Hague')
print(country_capitals_list)
