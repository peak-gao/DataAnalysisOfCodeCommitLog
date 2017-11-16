"""
create word cloud based on commit summary
"""
from os import path
import random
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import loadData as ld

dirname = path.dirname(__file__)

mask = np.array(Image.open(path.join(dirname, "resources/stormtrooper_mask.png")))

text = ld.loadSummaries()

stopwords = set(STOPWORDS)

# wc = WordCloud(
#     max_words=1000, mask=mask, stopwords=stopwords, margin=10,
#     random_state=1).generate(text)

wc = WordCloud(background_color="white", stopwords=stopwords, margin=10,
    random_state=1).generate(text)

default_colors = wc.to_array()
plt.figure()
plt.title("Commit Word Cloud")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()
