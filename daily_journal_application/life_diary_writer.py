class JournalBase:
    def __init__(self, target_file_name):
        self.target_file_name = target_file_name
    def write_journal_content(self):
        pass
class MultipleLineDiary(JournalBase):
    def __init__(self):
        super().__init__("Daily_Journal_Application/mylife.txt")
    def write_journal_content(self):
        with open(self.target_file_name, "a") as output_file:
            continue_writing_input = True

            while continue_writing_input:
                user_input = input("Enter your line: ")
                output_file.write(user_input + "\n")

                user_repeat_choice = input("Do you want to add another line? (yes/no): ").lower()
                if user_repeat_choice != "y":
                     continue_writing_input = False

        print(f"Content successfully written to {self.target_file_name}.")

if __name__ == "__main__":
    diary_instance = MultipleLineDiary()
    diary_instance.write_journal_content()