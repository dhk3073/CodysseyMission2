class Quiz:
        def __init__(self, question, options, answer, explanation):
                self.question = question
                self.options = options
                self.answer = answer
                self.explanation = explanation

        def display(self):
                print(f"Q : {self.question}")

                for i, option in enumerate(self.options, start=1):
                        print(f"{i}.{option}")
