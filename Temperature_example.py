def from_celcius(tempCelcius):
    tempFarenheit = (tempCelcius * 9/5) + 32
    return tempFarenheit


class Temperature:
    def __init__(self, tempFarenheit):
        self.temperature = tempFarenheit


an_object = Temperature(50)
f = from_celcius(an_object.temperature)
