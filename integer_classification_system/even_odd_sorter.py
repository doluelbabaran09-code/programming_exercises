import os

class FileValidator:
    """Base class to handle file existence checks."""
    def __init__(self, target_file_name):
        self.target_file_name = target_file_name
    def is_file_ready(self):
        """Behavior: Checks if the source file exists."""
        return os.path.exists(self.target_file_name)
    