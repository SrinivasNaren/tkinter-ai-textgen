

# 🌟 Sentiment Analysis Demo with DistilBERT

> 🎉 A simple **Sentiment Analysis App** powered by Hugging Face’s [DistilBERT model](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
> 🧠 Understand how text sentiment classification has evolved **before and after Transformers**.

---

## ✨ Demo Preview

After running the app, a browser tab will open automatically showing your app 👇

![Demo Screenshot](./demo.png)

---

## 📖 Theory (Before vs After Transformers)

### 🕰 Before Transformers

* Used **RNNs, LSTMs, GRUs** → processed text word by word.
* Suffered from **long dependency problems** (hard to understand context in long sentences).
* Training was **slow & memory heavy**.

### ⚡ After Transformers

* **Self-Attention** → model looks at the whole sentence at once.
* **Parallel training** → much faster and scalable.
* Pretrained models like **BERT, DistilBERT, GPT** made NLP tasks super easy.

💡 **Thinkers vs Transformers**:
Old models were like **“word readers”** → slow & forgetful.
Transformers are like **“context thinkers”** → fast & smart.

---

## 🚀 Quick Start

1️⃣ Clone this repo:

```bash
git clone https://github.com/your-username/sentiment-analysis-demo.git
cd sentiment-analysis-demo
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Run the app:

```bash
python app.py
```

👉 This will **open your browser automatically** at `http://127.0.0.1:5000/` 🎨

---

## 🔗 Model Reference

We are using Hugging Face’s **DistilBERT** fine-tuned on SST-2:
👉 [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)

---

## 🎯 Features

✅ Clean & simple UI
✅ Real-time Sentiment Analysis (Positive / Negative)
✅ Powered by Hugging Face Transformers
✅ Lightweight but effective

---

## 🛠 Tech Stack

* ⚡ **Python**
* ⚡ **Flask**
* 🤗 **Hugging Face Transformers**
* 🌐 **HTML/CSS/JS** for frontend

---

## 🌍 Contribute

Want to improve this project? PRs are welcome 💜

