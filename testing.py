from summarize.summary import get_text_summary
from summarize.TextRank import textRankSummary
from summarize.LexRank import lexRankSummary
# from summarize.SkipGram import skipgram

summary1= get_text_summary('test.txt')
summary3 = textRankSummary('test.txt')
summary4 = lexRankSummary('test.txt')
print(summary1)
print("-"*30)
print(summary3)
print("-"*30)
print(summary4)
print("-"*30)
# print(skipgram('test.txt'))