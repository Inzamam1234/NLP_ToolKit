from models.grammar_corrector import GrammarCorrector

corrector = GrammarCorrector()

text = "She dont like to playing football in evening."

print("Original:", text)
print("Corrected:", corrector.correct(text))
