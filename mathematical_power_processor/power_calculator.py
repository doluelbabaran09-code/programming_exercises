import os

class MathBase:
    def __init__(self, target_file_name):
        self.target_file_name = target_file_name
    def is_file_ready(self):
        return os.path.exists(self.target_file_name)

class PowerProcessor(MathBase):
    def __init__(self):
        super().__init__("mathematical_power_processor/integers.txt")
    def calculate_powers(self):
        try:
            if not self.is_file_ready():
                raise FileNotFoundError(f"{self.target_file_name} is missing, ")

            with open(self.target_file_name, "r") as input_file:
                integer_list = [int(line.strip()) for line in input_file if line.strip()]

            with open("mathematical_power_processor/double.txt", "w") as square_file, open("mathematical_power_processor/triple.txt", "w") as cube_file:
                for current_integer in integer_list:
                    if current_integer % 2 == 0:
                        square_file.write(f"{current_integer ** 2}\n")
                    else:
                        cube_file.write(f"{current_integer ** 3}\n")

            print("Successfully processed the integers annd saved the results to double.txt and triple.txt.")
         
        except ValueError:
            print("Error: integers.txt must contaio only valid integers.")
    
if __name__ == "__main__":
    processor_object = PowerProcessor()
    processor_object.calculate_powers()