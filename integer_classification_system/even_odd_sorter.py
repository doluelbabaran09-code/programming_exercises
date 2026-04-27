import os

class FileValidator:
    """Base class to handle file existence checks."""
    def __init__(self, target_file_name):
        self.target_file_name = target_file_name