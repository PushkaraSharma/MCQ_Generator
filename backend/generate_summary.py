from summarizer import Summarizer

def Summary(text):
    model = Summarizer()
    result = model(text, min_length=60,max_length=500,ratio=0.4)
    summary = "".join(result)
    print(summary)
    return summary