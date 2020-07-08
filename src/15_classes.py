# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.wpname = name
    def __str__(self):
        return "Name: "+self.wpname+"\nLatitude: "+str(self.latitude)+"\nLongitude: "+str(self.longitude)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.gdifficulty = difficulty
        self.gsize = size
    def __str__(self):
        return "Name: "+self.wpname+"\nLatitude: "+str(self.latitude)+"\nLongitude: "+str(self.longitude)+"\nDifficulty: "+str(self.gdifficulty)+"\nSize: "+str(self.gsize)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505,-121.51521,"Catacombs")

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)
print()

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)
# Print it--also make this print more nicely
print(geocache)
