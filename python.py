class FlightTable:
    def _init_(self, data):
        self.data = data

    def search(self, search_type, city1=None, city2=None):
        if search_type == 1:
            return [row for row in self.data if city1 in row[1:3] or city1 in row[2:4]]
        elif search_type == 2:
            return [row for row in self.data if row[1] == city1]
        elif search_type == 3:
            return [row for row in self.data if row[1] == city1 and row[2] == city2]

data = [
    ["AI161E90", "BLR", "BOM", 5600],
    ["BR161F91", "BOM", "BBI", 6750],
    ["AI161F99", "BBI", "BLR", 8210],
    ["VS171E20", "JLR", "BBI", 5500],
    ["AS171G30", "HYD", "JLR", 4400],
    ["AI131F49", "HYD", "BOM", 3499]
]

ft = FlightTable(data)

print("Enter the search parameter:")
print("1. Flights for a particular City")
print("2. Flights From a city")
print("3. Flights between two given cities")
search_type = int(input())

if search_type == 1:
    print("Enter the City name:")
    city = input()
    result = ft.search(search_type, city)
elif search_type == 2:
    print("Enter the City name:")
    city = input()
    result = ft.search(search_type, city)
elif search_type == 3:
    print("Enter the From City name:")
    city1 = input()
    print("Enter the To City name:")
    city2 = input()
    result = ft.search(search_type, city1, city2)

if len(result) > 0:
    print("Flight ID\tFrom\tTo\tPrice")
    for row in result:
        print(f"{row[0]}\t\t{row[1]}\t{row[2]}\t{row[3]}")
else:
    print("No flights found.")