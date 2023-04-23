from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

import os

def textRankSummary(filename):
    filepath = os.path.join(os.getcwd(),'webapp','static','uploads')
    file = open(os.path.join(filepath,filename),'r')
    full_transcript = file.read()

    parser = PlaintextParser.from_string(full_transcript,Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document,8)
    summary = [str(sentence) for sentence in summary]
    summary = ' '.join(summary)
    return summary

# textRankSummary('test.txt')