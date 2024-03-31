countries=("Kenya","Uganda","Tanzania","Rwanda")
print(countries)
print(countries[0:3])
countrylist=list(countries)
print(countrylist)

countrylist.append("Malawi")
print(countrylist)
countrylist.append("Ethiopi")
print(countrylist)

countrylist.remove("Uganda")
print(countrylist)

country=tuple(countrylist)
print(country)