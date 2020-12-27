counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print(counties_dict)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for key, value in counties_dict.items():
    print(f"{key} county has {value} voters.")
