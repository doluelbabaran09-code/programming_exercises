import os

class FileValidator:
    def __init__(self, target_file_name):
        self.target_file_name = target_file_name 
    def is_file_ready(self):
        return os.path.exists(self.target_file_name)

class GwaAnalyzer(FileValidator):
    def __init__(self):
        super().__init__("student_performance_analyzer/gwa_records.txt")
    def find_highest_gwa(self):
        highest_gwa_value = -1.0
        top_performing_students = ""  
        try:
            if not self.is_file_ready():
                raise FileNotFoundError(f"{self.target_file_name} is missing")
            
            with open(self.target_file_name, "r") as source_text_file:
                for student_data_line in source_text_file:
                    name_and_gwa = student_data_line.strip().split(',')
                    if len(name_and_gwa) == 2:
                        current_student_name = name_and_gwa[0].strip()
                        current_student_gwa = float(name_and_gwa[1].strip())
                    if current_student_gwa > highest_gwa_value:
                        highest_gwa_value = current_student_gwa
                        top_performing_students = current_student_name

            print(f"The highest GWA is {highest_gwa_value} and the top performing student is {top_performing_students}.")
        except ValueError:
            print("Error: gwa_records.txt must contain valid names and GWA values separated by commas.")

if __name__ == "__main__":
    gwa_analyzer_instance = GwaAnalyzer()
    gwa_analyzer_instance.find_highest_gwa()
                  
            