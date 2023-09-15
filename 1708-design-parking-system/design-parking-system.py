class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.max_big = big
        self.max_medium = medium
        self.max_small = small
        self.curr_big = 0
        self.curr_medium = 0
        self.curr_small = 0


    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.curr_big + 1 <= self.max_big:
            self.curr_big += 1
            return True
        elif carType == 2 and self.curr_medium + 1 <= self.max_medium:
            self.curr_medium += 1
            return True
        elif carType == 3 and self.curr_small + 1 <= self.max_small:
            self.curr_small += 1
            return True
        else:
            return False



        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)