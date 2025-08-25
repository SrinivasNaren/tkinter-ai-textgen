import tkinter as tk
from transformers import pipeline


# Load Hugging Face sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# Function to analyze text
def analyze_sentiment():
    user_input = text_entry.get("1.0", tk.END).strip()
    if user_input:
        result = sentiment_pipeline(user_input)[0]
        sentiment_label = result['label']
        sentiment_score = round(result['score'], 3)
        output_label.config(
            text=f"Sentiment: {sentiment_label}\nConfidence: {sentiment_score}"
        )
    else:
        output_label.config(text="⚠️ Please enter some text to analyze.")

# GUI Window
root = tk.Tk()
root.title("AI Sentiment Analysis App")
root.geometry("450x350")
root.config(bg="#f0f0f0")

# Title
title = tk.Label(
    root, 
    text="Sentiment Analysis (AI + Hugging Face)", 
    font=("Arial", 14, "bold"), 
    bg="#f0f0f0"
)
title.pack(pady=10)

# Text Box
text_entry = tk.Text(root, height=6, width=50, font=("Arial", 12))
text_entry.pack(pady=10)

# Analyze Button
analyze_button = tk.Button(
    root, 
    text="Analyze Sentiment", 
    command=analyze_sentiment, 
    bg="#007acc", 
    fg="white", 
    font=("Arial", 12, "bold"),
    relief="raised",
    padx=10,
    pady=5
)
analyze_button.pack(pady=5)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
output_label.pack(pady=15)

# Run the app
root.mainloop()
