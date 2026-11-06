# RLHF Preference Dataset Template & Validator

A standardized schema and validation script for Reinforcement Learning from Human Feedback (RLHF) data. Built to ensure annotation teams deliver high-quality pairwise ranking data for LLM alignment.

**Built by:** Ibegbunam Emmanuel — AI Training Specialist | Multilingual RLHF & Red-Teaming

## Why this exists
Frontier models are aligned using human preferences. If the data format is wrong, the model learns the wrong things. This toolkit provides a strict JSONL schema and a Python validator to catch errors (like identical responses, missing rationales, or malformed IDs) before the data enters the training pipeline.

## What it does
- **Schema Validation:** Ensures every record has required RLHF fields (`prompt`, `response_a`, `response_b`, `chosen`, `rationale`).
- **Logic Check:** Prevents errors like `response_a` being identical to `response_b`.
- **Rationale Check:** Ensures the annotator actually explained *why* they chose a response.
- **Format Check:** Verifies that `chosen` is strictly `"A"` or `"B"`.

## Quick Start

```bash
python validate_rlhf.py --input sample_data/preferences.jsonl
