from transformers import pipeline, AutoTokenizer
import torch

model_name = 'facebook/bart-large-cnn'
tokenizer = AutoTokenizer.from_pretrained(model_name)
summarizer = pipeline("summarization", model=model_name)

max_tokens = 900

def summarize_text(text):
    text_chunks = split_text_into_chunks(text)
    all_summaries = []

    for chunk in text_chunks:
        try:
            summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
            all_summaries.append(summary[0]['summary_text'])
        except Exception as e:
            print(f"⚠️ Error summarizing chunk: {e}")
            continue
    return "\n\n".join(all_summaries)
    
def split_text_into_chunks(text,max_tokens=max_tokens):
    input_ids=tokenizer.encode(text, return_tensors="pt")[0]

    chunks = []
    for i in range(0, len(input_ids), max_tokens):
        chunk_ids = input_ids[i:i+max_tokens]
        chunk = tokenizer.decode(chunk_ids, skip_special_tokens=True)
        chunks.append(chunk)
    return chunks