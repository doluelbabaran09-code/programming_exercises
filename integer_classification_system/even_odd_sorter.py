import os

class FileValidator:
    def __init__(self, target_file_name):
        self.target_file_name = target_file_name
    def is_file_ready(self):
        return os.path.exists(self.target_file_name)

class NumberProcessor(FileValidator):
    def __init__(self):
        super().__init__("integer_classification_system/numbers.txt")
    def classify_numbers(self):
        try:
            if not self.is_file_ready():
                raise FileNotFoundError(f"{self.target_file_name} is missing.")

            with open(self.target_file_name, "r") as source_text_file:
                integers_collection = [int(line.strip()) for line in source_text_file if line.strip()]

            with open("integer_classification_system/even.txt", "w") as even_file, open("integer_classification_system/odd.txt", "w") as odd_file:
                for current_integer in integers_collection:
                    if current_integer % 2 == 0:
                        even_file.write(f"{current_integer}\n")
                    else:
                        odd_file.write(f"{current_integer}\n")
            
            print("Successfully classified numbers into even.txt and odd.txt.")

        except ValueError:
            print("Error: numbers.txt must contain only integers.")
        except FileNotFoundError as e:
            print(e)
if __name__ == "__main__":
    sorter_instance = NumberProcessor()
    sorter_instance.classify_numbers()
