class MovingAverageFilter:
  def __init__(self, num) -> None:
    self.num = num
    self.values:list[float] = []

  def add_value(self, value:float):
    if(len(self.values) == self.num):
      self.values.pop(0)
    self.values.append(value)
    return sum(self.values) / len(self.values)