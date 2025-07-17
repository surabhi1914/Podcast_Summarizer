from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# def split_text_into_segments(text, max_words=100):
#     words = text.split()
#     segments = []
#     for i in range(0, len(words), max_words):
#         segment = ' '.join(words[i:i + max_words])
#         segments.append(segment)
#     return segments

def cluster_segments(segments, num_clusters=5):
    embeddings = model.encode(segments)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(embeddings)
    
    clustered={}

    for idx, label in enumerate(kmeans.labels_):
        clustered.setdefault(label, []).append((idx,segments[idx]))
    return clustered

def generate_chapters(text, num_chapters=5):
    segments=[seg['text'] for seg in text]
    clustered=cluster_segments(segments,num_clusters=num_chapters)

    chapters=[]
    for label in sorted(clustered.keys()):
        segment_indices = [idx for idx, _ in clustered[label]]
        title_idx = min(segment_indices)
        title_text = clustered[label][0][1].split('.')[0]
        timestamp = title_idx*60
        time_str = format_timestamp(timestamp)
        chapters.append((title_idx, f"{time_str} - {title_text}"))

    chapters.sort(key=lambda x:x[0])

    chapters = [chapter for _, chapter in chapters]
    return chapters

def format_timestamp(seconds):
    minutes = seconds // 60
    sec=seconds % 60 
    return f"{int(minutes):02d}:{int(sec):02d}"
    


