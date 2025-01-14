# Welcome everyone.

This is a custom data preparation tool for Bangla text. It consists of sentence-level tokenization, stopword removal, and word-stemming steps. 

Hopefully, this tool will help your model for better natural language understanding. 

## Installation
```bash
$ pip install git+https://github.com/avisheak/preparation
```

## Usage

```python
from preparation import prepare
input_text = """your input text"""
prepared_text = prepare(
    input_text       
)
```
