class Question:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices

class Survey:
    def __init__(self, title, instructions, questions):
        self.title = title
        self.instructions = instructions
        self.questions = questions

satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out the following survey to let us know how we're doing.",
    [
        Question("How would you rate our service?", ["Excellent", "Good", "Average", "Poor"]),
        Question("How likely are you to recommend us to a friend?", ["Very likely", "Somewhat likely", "Not likely"]),
        Question("How satisfied are you with our product quality?", ["Very satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very dissatisfied"]),
        Question("How satisfied are you with our customer support?", ["Very satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very dissatisfied"])
    ]
)
