# from . import captions
import regex as re
import nltk
import os
import heapq

def get_text_summary(filename=None):
    if not filename:
        return "No File Was Provided"
    
    filepath = os.path.join(os.getcwd(),'webapp','static','uploads')
    file = open(os.path.join(filepath,filename),'r')
    full_transcript = file.read()

    # cleaning data (removes brackets , special characters etc)
    full_transcript = re.sub(r'\[[0-9]*\]', ' ', full_transcript)
    full_transcript = re.sub(r'\s+', ' ', full_transcript)
    formatted_transcript_text = re.sub('[^a-zA-Z]', ' ', full_transcript )
    formatted_transcript_text = re.sub(r'\s+', ' ', formatted_transcript_text)

    #converting text to sentences
    sentence_list = nltk.tokenize.sent_tokenize(full_transcript)

    #find weighted frequency of occurence
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    word_list = nltk.word_tokenize(formatted_transcript_text)
    for word in word_list:
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

    #calculate the sentence score
    sentence_scores ={}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' '))  < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    #getting summary
    summary_sentences = heapq.nlargest(10,sentence_scores,key=sentence_scores.get)
    summary1 = ' '.join(summary_sentences)

    #lexrank summary
    # lxr = LexRank(sentence_list, stopwords=STOPWORDS['en'])
    # summary2 = lxr.get_summary(sentence_list, summary_size=10, threshold=None, fast_power_method=True)
    # summary2 = ' '.join(summary2)


    return summary1

# testing
# summary1,summary2 = get_text_summary('test.txt')
# print(summary1)
# print('-'*30)
# print(summary2)