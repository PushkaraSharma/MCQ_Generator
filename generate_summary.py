from summarizer import TransformerSummarizer

def Summary(text):
    model=TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
    result = model(text, min_length=60, max_length=500, ratio=0.4)
    summary = "".join(result)
    return summary
