# Changelog

All notable changes to cat-survey will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-05-11

### Changed
- **Canonical import name normalized to `catsurvey`** (no separator), matching
  the rest of the cat-* family. The previous name `cat_survey` continues to
  work as a backward-compatible alias; both forms resolve to the same module
  object. Existing code does not need to change.
- **Source directory** renamed from `src/cat_survey/` to `src/catsurvey/`.
  Alias ships as `src/cat_survey/__init__.py`.
- **Internal imports** of `cat_stack` rewritten to `catstack`. Now requires
  `cat-stack>=1.0.19`.

---

## [0.1.0] - Initial release

- Survey response classification, extraction, exploration, and summarization
  via the cat-stack engine.
