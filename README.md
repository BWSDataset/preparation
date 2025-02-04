# Welcome everyone.

This is a custom data preprocessing tool for Bangla text. It consists of sentence-level tokenization, stopword removal, unnecessary text removal, and word-stemming steps. 

Hopefully, this tool will help your model for better natural language understanding. 

## Installation
```bash
$ pip install git+https://github.com/bwsdataset/readiness
```

## Usage

```python
from preparation import prepare
input_text = """your input text"""
prepared_text = prepare(
    input_text,
    list=None # an optional list of strings which you want to remove from your text (default `None`)      
)
```
