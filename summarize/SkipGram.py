from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import numpy as np
import skipthoughts
import nltk
import regex as re
import os

def skipgram(filename=None):
    model = skipthoughts.UniSkip()
    encoder = skipthoughts.Encoder(model)

    # load data
    filepath = os.path.join(os.getcwd(),'webapp','static','uploads')
    file = open(os.path.join(filepath,filename),'r')
    full_transcript = file.read()

    # cleaning data (removes brackets , special characters etc)
    full_transcript = re.sub(r'\[[0-9]*\]', ' ', full_transcript)
    full_transcript = re.sub(r'\s+', ' ', full_transcript)
    formatted_transcript_text = re.sub('[^a-zA-Z]', ' ', full_transcript )
    formatted_transcript_text = re.sub(r'\s+', ' ', formatted_transcript_text)

    sentence_list = nltk.tokenize.sent_tokenize(full_transcript)
    # encode data
    vectors = encoder.encode(sentence_list)

    # cluster data
    n_clusters = np.ceil(len(vectors)**0.5)
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(vectors)
    # print(kmeans.labels_)

    avg = []
    for j in range(n_clusters):
        idx = np.where(kmeans.labels_ == j)[0]
        avg.append(np.mean(idx))
    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, vectors)
    ordering = sorted(range(n_clusters), key=lambda k: avg[k])
    summary = ' '.join([sentence_list[closest[idx]] for idx in ordering])

    return summary