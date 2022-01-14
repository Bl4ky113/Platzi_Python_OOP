class Computer:
    def __init__ (self, processor, graphs, ram, storage, storage_type, screen_size):
        self.processor = processor
        self.graphs = graphs
        self.ram = ram
        self.storage = storage
        self.storage_type = storage_type
        self.screen_size = screen_size

class Desktop (Computer):
    def __init__ (self, processor, graphs, ram, storage, storage_type, screen_size, mouse, keyboard):
        super().__init__(processor, graphs, ram, storage, storage_type, screen_size)
        self.mouse = mouse
        self.keyboard = keyboard

class Cellphone (Computer):
    def __init__ (self, processor, graphs, ram, storage, storage_type, screen_size, btns, battery, camera):
        super().__init__(processor, graphs, ram, storage, storage_type, screen_size)
        self.btns = btns
        self.battery = battery
        self.camera = camera

class Laptop (Computer):
    def __init__ (self, processor, graphs, ram, storage, storage_type, screen_size, trackpad, keyboard, battery):
        super().__init__(processor, graphs, ram, storage, storage_type, screen_size)
        self.trackpad = trackpad
        self.keyboard = keyboard
        self.battery = battery
