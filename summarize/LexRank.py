from lexrank import LexRank, STOPWORDS
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import os

def lexRankSummary(filename):
    filepath = os.path.join(os.getcwd(),'webapp','static','uploads')
    file = open(os.path.join(filepath,filename),'r')
    full_transcript = file.read()

    token = Tokenizer("english")
    sentences = token.to_sentences(full_transcript)

    # parser = PlaintextParser.from_string(full_transcript,Tokenizer("english"))
    summarizer = LexRank(sentences, stopwords=STOPWORDS['en'])
    summary = summarizer.get_summary(sentences, summary_size=10, threshold=None, fast_power_method=True)
    summary = ' '.join(summary)
    return summary

# lexRankSummary('test.txt')