from flask import Flask, render_template, request, jsonify

# Import your NLP modules
from models.summarizer import TextSummarizer
from models.paraphraser import TextParaphraser
from models.grammar_corrector import GrammarCorrector

app = Flask(__name__)

# Load models ONCE (very important)
summarizer = TextSummarizer()
paraphraser = TextParaphraser()
grammar_corrector = GrammarCorrector()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_text():
    data = request.get_json()

    text = data.get("text", "")
    task = data.get("task", "")

    if not text.strip():
        return jsonify({"result": "Error: Empty input text"})

    if task == "summarize":
        result = summarizer.summarize(text)

    elif task == "paraphrase":
        result = paraphraser.paraphrase(text)

    elif task == "grammar":
        result = grammar_corrector.correct(text)

    else:
        result = "Invalid task selected"

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
