import os

class MathBase:
    def __init__(self, target_file_name):
        self.target_file_name = target_file_name
    def is_file_ready(self):
        return os.path.exists(self.target_file_name)
    