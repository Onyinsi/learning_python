east_african_cities ={"Nairobi","Kigali","Kampala","Dar es salaam","Kinshasa","Bujumbura","Juba"  }

print(east_african_cities)

print(f"there are {len(east_african_cities)} cities in the set")

print(type(east_african_cities))

west_african_cities = {"Lagos","Accra",}
south_african_cities = {"Cape town","Gaborone"}

master_cities_list = {"new york"}
master_cities_list.update(east_african_cities)
print(master_cities_list)

super_cities = {"new york","Washington"}