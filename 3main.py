import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import string
import nltk

#  Downloading stopwords 
nltk.download('stopwords')
from nltk.corpus import stopwords

# input text
text = """
Data science is an interdisciplinary field that uses scientific methods, processes, algorithms,
and systems to extract knowledge and insights from structured and unstructured data.
It applies techniques from many fields including statistics, computer science, and machine learning.
Data scientists use data to understand trends, build predictive models, and support decision-making.
The demand for data professionals is growing rapidly as organizations increasingly rely on data
to drive innovation and strategy. Effective data analysis helps businesses understand customer
behavior, optimize operations, and uncover new opportunities.
"""

# cleaning text
clean_text = text.lower()
clean_text = clean_text.translate(str.maketrans('', '', string.punctuation))

# removing stopwords
stop_words = set(stopwords.words('english'))
words = clean_text.split()
filtered_words = [word for word in words if word not in stop_words]

#  counting word frequency
word_counts = Counter(filtered_words)

#  Showing top 10 words
print("\n🔹 Top 10 Most Frequent Words:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")

#  Generating and saveing word cloud (no display beacause weak memory)
wordcloud = WordCloud(
    width=600, height=300,
    background_color='white',
    colormap='plasma'
).generate_from_frequencies(word_counts)

#  Saving wordcloud image instead of showing it
wordcloud.to_file("wordcloud_output.png")
print("\n✅ WordCloud saved as 'wordcloud_output.png' in the current folder.")