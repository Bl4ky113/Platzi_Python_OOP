class Car ():
    def __init__ (self, model, brand, color, type_motor, type_fuel, num_fuel, num_motor_pistons):
        self.model = model
        self.brand = brand
        self.color = color

        self._motor = Motor(type_motor, type_fuel, num_fuel, num_motor_pistons)

        self.lights = {
            "left": Light("ambar"),
            "right": Light("ambar"),
            "frontals": Light("white")
        }

        self._status = "stoped"

    def turn_alert_lights (self):
        if not self.lights["left"].show_status() or not self.lights["right"].show_status():
            # If one or more lights are off, both turn on
            self.lights["left"].turn_on()
            self.lights["right"].turn_on()
        else:
            # Else if both are on, the get turn off
            self.lights["left"].turn_off()
            self.lights["right"].turn_off()

    def turn_light (self, side="frontals"):
        if not self.lights[side].show_status():
            self.lights[side].turn_on()
        else:
            self.lights[side].turn_off()

class Motor ():
    def __init__ (self, type, type_fuel, num_fuel, num_pistons):
        self.type = type
        self.type_fuel = type_fuel
        self.num_fuel = num_fuel
        self.num_pistons = num_pistons

class Light ():
    def __init__ (self, color):
        self.color = color
        self._status = False

    def turn_on (self):
        self._status = True

    def turn_off (self):
        self._status = False

    def show_status (self):
        return self._status