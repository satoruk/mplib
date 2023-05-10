class LoadCellBase:
  def read(self) -> int:
    raise NotImplementedError("read() is not implemented")

  def reset(self):
    raise NotImplementedError("reset() is not implemented")

  def power_down(self):
    raise NotImplementedError("power_down() is not implemented")

  def power_up(self):
    raise NotImplementedError("power_up() is not implemented")
