# 1) The parking lot has multiple levels. Each level has multiple rows of spots.
# 2) The parking lot can park motorcycles, cars, and buses.
# 3) The parking lot has motorcycle spots, compact spots, and large spots.
# 4) A motorcycle can park in any spot.
# 5) A car can park in either a single compact spot or a single large spot.
# 6) A bus can park in five large spots that are consecutive and within the same row. It cannot park in small spots.

# Key Points:
# Each Vehicle has plate number or license
# Lot should have occupied spots list using plate number or license
# We use "small", "medium", "large" for "car", "truck", "bus"


class Vehicle:

    # Pass vehicle size
    def __init__(self, size, license_plate):
        self.license_plate = license_plate
        self.size = size
        self.lot = ParkingLot.get_instance()

    # private method
    def find_spots(self):
        # Remove spot from its list
        spot = self.lot.get_spots(self.size).pop(0)

        return spot

    def park(self):
        spot = self.find_spots()

        if spot:
            self.lot.occupied_spots[self.license_plate] = spot

    def leave(self):
        # Use license plate num to get the spot object
        spot = self.lot.occupied_spots[self.license_plate]
        self.lot.occupied_spots.pop(self.license_plate, None)
        spot.remove_vehicle()


class ParkingLot:

    SMALL_SLOTS_NUM = 10
    MEDIUM_SLOTS_NUM = 10
    LARGE_SLOTS_NUM = 10
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if not ParkingLot.__instance:
            __instance = ParkingLot()

        return __instance

    def __init__(self):

        self.small_spots = []
        self.medium_spots = []
        self.large_spots = []
        self.occupied_spots = {}  # license plate number => spot

        for i in range(self.SMALL_SLOTS_NUM):
            self.small_spots.append(ParkingSpot(i, "small"))

        for i in range(self.MEDIUM_SLOTS_NUM):
            self.medium_spots.append(ParkingSpot(i, "medium"))

        for i in range(self.LARGE_SLOTS_NUM):
            self.large_spots.append(ParkingSpot(i, "large"))

    def get_spots(self, size):
        if size == "small":
            return self.small_spots
        elif size == "medium":
            return self.medium_spots
        elif size == "large":
            return self.large_spots


class ParkingSpot:

    def __init__(self, spot_id, size):
        self.id = spot_id
        self.vehicle_size = size
        self.vehicle = None

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.vehicle = None


v1 = Vehicle("small", "ABC123")
v2 = Vehicle("small", "DEF123")
v3 = Vehicle("small", "GHI123")

v1.park()
v2.park()
v3.park()

for spot in ParkingLot.get_instance().small_spots:
    print spot.vehicle

print(ParkingLot.get_instance().occupied_spots.keys())

