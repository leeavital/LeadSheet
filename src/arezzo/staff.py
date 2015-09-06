class Staff():

  def __init__(self, instrument):
    self.measures = []
    self._instrument = instrument

  def addMeasure(self, measure):
    self.measures.append(measure)

  # yarg theses are the same
  def GMCode(self):
    return self._instrument

  def instrument(self):
    return self._instrument
