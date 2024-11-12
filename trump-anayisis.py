
from collections import Counter
import string
import matplotlib.pyplot as plt
import os

def analyze_words(file_path, num_words=10):
    # Verify if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at {file_path}")
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words
    words = text.split()
    
    # Common English stop words to exclude
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                 'of', 'with', 'by', 'from', 'up', 'about', 'into', 'over', 'after',
                 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                 'have', 'has', 'had', 'do', 'does', 'did',
                 'i', 'you', 'he', 'she', 'it', 'we', 'they',
                 'this', 'that', 'these', 'those',
                 'will', 'would', 'can', 'could', 'should', 'must',
                 'my', 'your', 'his', 'her', 'its', 'our', 'their'}
    
    # Filter out stop words
    filtered_words = [word for word in words if word not in stop_words]
    
    # Count frequencies
    counter = Counter(filtered_words)
    most_common_words = counter.most_common(num_words)
    
    # Create bar chart
    words, frequencies = zip(*most_common_words)
    plt.figure(figsize=(12, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title('Most Frequent Words in Text')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.tight_layout()
    
    # Calculate some basic statistics
    total_words = len(filtered_words)
    unique_words = len(set(filtered_words))
    
    return most_common_words, plt, total_words, unique_words

# Example usage
file_path = "E:/discurso_trump.txt"
try:
    frequencies, graph, total_words, unique_words = analyze_words(file_path)
    
    print("\nText Statistics:")
    print(f"Total words (excluding stop words): {total_words}")
    print(f"Unique words: {unique_words}")
    print("\nMost frequent words:")
    for word, freq in frequencies:
        print(f"{word}: {freq} times")
    
    graph.show()
except FileNotFoundError as e:
    print(f"Error: {e}")
