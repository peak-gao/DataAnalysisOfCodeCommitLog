import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
import loadData as ld

from wordcloud import WordCloud, STOPWORDS


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)

mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))

text =  ld.loadSummary()

stopwords = set(STOPWORDS)

wc = WordCloud(max_words=100, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(text)

default_colors = wc.to_array()
wc.to_file("a_new_hope.png")
plt.figure()
plt.title("Commit Word Cloud")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()
