# 📝 NLP Toolkit – Fine-tuned T5 with LoRA  

This repository contains an **NLP Toolkit** built by fine-tuning the **T5-base model** from [Hugging Face Transformers](https://huggingface.co/) for three key text generation tasks:  

- **Text Summarization**  
- **Paraphrasing**  
- **Grammar Correction**  

The model is fine-tuned using **Parameter-Efficient Fine-Tuning (PEFT)** techniques, specifically **LoRA (Low-Rank Adaptation)**, to reduce training cost and memory usage while maintaining strong performance.  

---

## 🚀 Features  
- Multi-task support with a single T5 backbone.  
- Fine-tuned for **Summarization, Paraphrasing, and Grammar Correction**.  
- Implemented with **LoRA for PEFT**, making training efficient on limited hardware.  
- Easy-to-use inference pipeline with Hugging Face `transformers`.  
- Scalable and extendable for other NLP tasks.  

---

## ⚙️ Technical Details  
- **Base Model:** `t5-base`  
- **Frameworks Used:**  
  - [Hugging Face Transformers](https://huggingface.co/transformers/)  
  - [PEFT](https://huggingface.co/docs/peft/index) (for LoRA)  
  - [Datasets](https://huggingface.co/docs/datasets/)  
- **Fine-tuning Method:** LoRA-based PEFT → reduces trainable parameters while keeping most of the base model frozen.  
- **Tasks:**  
  - Summarization → trained on text-summary pairs.  
  - Paraphrasing → trained on paraphrase sentence pairs.  
  - Grammar Correction → trained on incorrect vs. corrected text datasets.  

---
