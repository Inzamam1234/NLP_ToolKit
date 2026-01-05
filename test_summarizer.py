from models.summarizer import TextSummarizer

summarizer = TextSummarizer()

text = """
Artificial Intelligence is a branch of computer science that focuses on creating
machines capable of performing tasks that typically require human intelligence.
These tasks include learning, reasoning, problem-solving, and understanding language.
"""

print(summarizer.summarize(text))
