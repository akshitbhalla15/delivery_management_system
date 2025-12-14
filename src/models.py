class Package:
    # Represents a package in the system
    def __init__(self, package_id, label_address, weight):
        self.package_id = package_id
        self.label_address = label_address
        self.weight = weight
        self.status = "Created" # Default status
        self.assigned_route_id = None

    # Updates the status of the package (e.g. Delivered)
    def update_status(self, new_status):
        self.status = new_status

class Route:
    # Represents a delivery route with multiple stops
    def __init__(self, route_id):
        self.route_id = route_id
        self.driver_id = None
        self.stops = []
        self.total_distance = 0.0
        self.optimized = False

    # Adds a new stop to the route
    def add_stop(self, address):
        self.stops.append(address)

    # Assigns a driver to this route
    def assign_driver(self, driver_id):
        self.driver_id = driver_id

class Driver:
    # Represents a driver who delivers packages
    def __init__(self, driver_id, name, capacity, password_hash):
        self.driver_id = driver_id
        self.name = name
        self.capacity = capacity
        self.password_hash = password_hash
        self.current_route_id = None

class InventoryManager:
    # Represents a manager who oversees the system
    def __init__(self, manager_id, name, password_hash):
        self.manager_id = manager_id
        self.name = name
        self.password_hash = password_hash

        self.status = "Available"