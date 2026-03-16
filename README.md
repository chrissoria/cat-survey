# cat-survey

Survey response classification powered by LLMs. A thin, survey-specific wrapper around [cat-stack](https://github.com/chrissoria/cat-stack).

`cat-survey` adds survey-specific prompt framing ("A respondent was asked: ...") on top of the domain-agnostic `cat-stack` engine — giving LLMs the context that responses come from a survey instrument.

## Installation

```bash
pip install cat-survey
```

With optional extras:

```bash
pip install "cat-survey[pdf]"         # PDF survey processing
pip install "cat-survey[embeddings]"  # Embedding-based similarity scoring
```

## Quick Start

### Classify survey responses

```python
import cat_survey

results = cat_survey.classify(
    input_data=["I feel great about the program", "It was a waste of time"],
    categories=["Positive", "Negative", "Neutral"],
    survey_question="How do you feel about the new wellness program?",
    api_key="sk-...",
)
```

### Discover categories from open-ended responses

```python
result = cat_survey.extract(
    input_data=responses,
    api_key="sk-...",
    survey_question="What changes would you suggest for the workplace?",
)
print(result["top_categories"])
```

### Summarize responses

```python
summaries = cat_survey.summarize(
    input_data=responses,
    api_key="sk-...",
    description="Open-ended feedback from employee satisfaction survey",
)
```

## How It Works

`cat-survey` is a thin wrapper that:

1. Takes your `survey_question` parameter
2. Injects survey-specific framing: *"A respondent was asked: '{survey_question}'."*
3. Delegates to `cat-stack` for all LLM communication, classification logic, batch processing, and ensemble methods

All `cat-stack` parameters (multi-model ensemble, batch mode, chain-of-thought, etc.) are passed through via `**kwargs`.

## API

| Function | Description |
|----------|-------------|
| `classify()` | Classify responses into predefined categories |
| `extract()` | Discover and normalize categories from responses |
| `explore()` | Raw category extraction (no deduplication) |
| `summarize()` | Summarize responses (pass-through to cat-stack) |

## Ecosystem

| Package | Role |
|---------|------|
| [cat-stack](https://github.com/chrissoria/cat-stack) | Domain-agnostic LLM classification engine |
| **cat-survey** | Survey-specific wrapper (this package) |
| [cat-cog](https://github.com/chrissoria/cat-cog) | Cognitive assessment scoring (CERAD) |

## License

GPL-3.0-or-later
