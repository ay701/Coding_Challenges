# Design an elevator bank for a building, with multiple elevators


class Building:
    ELEVATOR_NUM = 4
    __instance = None

    @staticmethod
    def get_instance():
        if not Building.__instance:
            __instance = Building()

        return __instance

    def __init__(self):
        self.elevators = []
        self.requests = {}  # Passenger Id => Passenger Object

        for i in range(self.ELEVATOR_NUM):
            self.elevators.append(Elevator(i))

    def find_elevator(self, passenger):
        elevator = None
        min_levels = 999

        for elevator in self.elevators:
            if elevator.in_service:
                tmp_levels = self.calc_levels(elevator, passenger)

                if tmp_levels < min_levels:
                    min_levels = tmp_levels

        return elevator

    def assign_elevator(self, passenger):
        elevator = self.find_elevator(passenger)

        if not elevator:
            self.get_instance().requests.pop()

    def calc_levels(self, elevator, passenger):
        # Remember to check capacity
        return None


class Elevator:
    MIN_LEVEL = -1  # Basement
    MAX_LEVEL = 10
    CAPACITY = 20
    STATUS_LIST = ["idle", "open", "loading", "unloading", "up", "down", "stop", "alarm"]

    def __init__(self, id, level=0, in_service=True, cur_status="idle"):
        self.id = id
        self.cur_level = level
        self.in_service = in_service
        self.cur_status = cur_status
        self.max_level = self.MAX_LEVEL
        self.min_level = self.MIN_LEVEL
        self.passengers = []

    def open(self):
        self.cur_status = "open"

    def close(self):
        self.cur_status = "close"

    def up(self):
        self.cur_status = "up"

    def down(self):
        self.cur_status = "down"

    def alarm(self):
        self.cur_status = "alarm"


class Passenger:
    global_id = 1  # static variable

    def __init__(self, name, cur_level):
        self.name = name
        self.cur_level = cur_level
        self.des_level = 0
        self.building = Building.get_instance()
        self.id = self.global_id
        self.global_id += 1

    def issue_alarm(self):
        self.building.alarmed()

    def issue_stop(self):
        self.building.requests[self.id] = self
        self.building.assign_elevator(self)

    def issue_request(self, des_level):
        self.building.requests[self.id].des_level = des_level


class Floor:
    def __init__(self, level, available=True):
        self.level = level
        self.available = available


class Request:
    def __init__(self):
        self.pass