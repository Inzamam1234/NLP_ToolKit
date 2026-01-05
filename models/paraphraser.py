from transformers import pipeline

class TextParaphraser:
    def __init__(self):
        """
        Load the paraphrasing model once.
        """
        self.paraphraser = pipeline(
            "text2text-generation",
            model="t5-base"
        )

    def paraphrase(self, text, max_length=100):
        """
        Paraphrase the given text.

        Parameters:
        - text (str): input text to paraphrase
        - max_length (int): max length of paraphrased text

        Returns:
        - paraphrased text (str)
        """

        if not text or len(text.strip()) == 0:
            return "Error: Input text is empty."

        # T5 works using instructions
        prompt = "paraphrase: " + text.strip()

        result = self.paraphraser(
            prompt,
            max_length=max_length,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )

        return result[0]["generated_text"]