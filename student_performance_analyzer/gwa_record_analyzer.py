import os

class FileValidator:
    def __init__(self, target_file_name):
        self.target_file_name = target_file_name 

    def is_file_ready(self):
        return os.path.exists(self.target_file_name)

class GwaAnalyzer(FileValidator):
    def __init__(self):
        super().__init__("student_performance_analyzer/gwa_records.txt")
        