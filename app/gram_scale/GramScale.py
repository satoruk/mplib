from load_cell.base import LoadCellBase

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

class GramScale(LoadCellBase):
  def __init__(self, load_cell:LoadCellBase, buff_size=5, rate=1.0):
    self.buff = []
    self.buff_size = buff_size
    self.load_cell = load_cell
    self.offset = 0
    self.rate = rate

  def read(self) -> int:
    value = self.load_cell.read()
    self.buff.append(value)
    if len(self.buff) > self.buff_size:
      self.buff.pop(0)
    return int(mean(self.buff))

  def tare(self, times=15):
    sum = 0
    for i in range(times):
        sum += self.read()
    self.offset = sum / times

  def value(self):
    return (self.read() - self.offset) * self.rate