from models.paraphraser import TextParaphraser

paraphraser = TextParaphraser()

text = "Artificial Intelligence is transforming the world rapidly."

print("Original:", text)
print("Paraphrased:", paraphraser.paraphrase(text))
