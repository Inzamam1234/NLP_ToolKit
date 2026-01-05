from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        """
        Load the summarization pipeline once.
        This avoids reloading the model again and again.
        """
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    def summarize(self, text, max_length=130, min_length=30):
        """
        Summarize the input text.

        Parameters:
        - text (str): input text to summarize
        - max_length (int): maximum summary length
        - min_length (int): minimum summary length

        Returns:
        - summary_text (str)
        """

        if not text or len(text.strip()) == 0:
            return "Error: Input text is empty."

        # Hugging Face models work better with trimmed text
        text = text.strip()

        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )

        return summary[0]["summary_text"]
