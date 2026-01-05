from transformers import pipeline

class GrammarCorrector:
    def __init__(self):
        """
        Load grammar correction model once.
        """
        self.corrector = pipeline(
            "text2text-generation",
            model="prithivida/grammar_error_correcter_v1"
        )

    def correct(self, text, max_length=128):
        """
        Correct grammar in the given text.

        Parameters:
        - text (str): input text with grammatical errors
        - max_length (int): max length of corrected text

        Returns:
        - corrected text (str)
        """

        if not text or len(text.strip()) == 0:
            return "Error: Input text is empty."

        result = self.corrector(
            text.strip(),
            max_length=max_length,
            do_sample=False
        )

        return result[0]["generated_text"]