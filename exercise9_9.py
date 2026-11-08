class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class Battery:
    """Upaya sederhana untuk memodelkan baterai mobil listrik."""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki baterai berukuran {self.battery_size}-kWh.")

    def get_range(self):
        """Mencetak pernyataan tentang jangkauan jarak berdasarkan ukuran baterai."""
        if self.battery_size == 40:
            range_distance = 150
        elif self.battery_size == 65:
            range_distance = 225
        print(f"Mobil ini dapat menempuh jarak sekitar {range_distance} mil dengan pengisian penuh.")

    def upgrade_battery(self):
        """Memeriksa ukuran baterai dan mengubahnya menjadi 65 jika belum."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai telah ditingkatkan menjadi 65 kWh.")
        else:
            print("Baterai sudah berukuran 65 kWh.")

class ElectricCar(Car):
    """Representasi aspek mobil yang khusus untuk kendaraan listrik."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_electric_car = ElectricCar('nissan', 'leaf', 2024)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()

my_electric_car.battery.get_range()

my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()