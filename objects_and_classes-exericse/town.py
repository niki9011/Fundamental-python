class Town:

    def __init__(self, town):
        self.town = town

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longtitude = longitude

    def __repr__(self):
        return f"Town: {self.town} | Latitude: {self.latitude} | Longitude: {self.longtitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
