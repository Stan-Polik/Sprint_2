points = 0

class PointsForPlace:
    def __init__(self,place = 0):
        self.place = place
    def get_points_for_place(self, place= 0):
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            points = 101 - place
            return points

class PointsForMeters:
    def __init__(self,meters = 0):
        self.meters = meters
    def get_points_for_meters(self, meters = 0):
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            points = int(meters * 0.5)
            return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self,place = 0, meters = 0):
        PointsForPlace.__init__(self, place)
        PointsForMeters.__init__(self, meters)
    def get_total_points(self, place = 0, meters = 0):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))