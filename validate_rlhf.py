
"""
RLHF Preference Data Validator
Checks JSONL files for standard RLHF pairwise ranking schema.
"""

import json
import argparse
import sys

REQUIRED_FIELDS = ["id", "prompt", "response_a", "response_b", "chosen", "rationale"]

def load_jsonl(path):
    records = []
    errors = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                errors.append(f"Line {i}: Invalid JSON — {e}")
    return records, errors

def validate_records(records):
    errors = []
    for i, rec in enumerate(records, start=1):
  
        for field in REQUIRED_FIELDS:
            if field not in rec:
                errors.append(f"Line {i}: Missing field '{field}'")
                continue
        
   
        if "chosen" in rec and rec["chosen"].upper() not in ["A", "B"]:
            errors.append(f"Line {i}: 'chosen' must be 'A' or 'B', got '{rec['chosen']}'")
            
     
        if "response_a" in rec and "response_b" in rec:
            if rec["response_a"].strip() == rec["response_b"].strip():
                errors.append(f"Line {i}: response_a and response_b are identical")
                
    
        if "rationale" in rec and len(rec["rationale"].strip()) < 10:
            errors.append(f"Line {i}: Rationale too short (must explain the choice)")
            
    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate RLHF Preference JSONL.")
    parser.add_argument("--input", required=True, help="Path to preferences.jsonl")
    args = parser.parse_args()

    records, json_errors = load_jsonl(args.input)
    val_errors = validate_records(records)
    all_errors = json_errors + val_errors

    print("=== RLHF Dataset Validation Report ===")
    print(f"Total pairs evaluated: {len(records)}")
    print(f"Valid pairs: {len(records) - len(val_errors)}")
    print(f"Errors found: {len(all_errors)}")
    print()
    
    for e in all_errors:
        print(f"[ERROR] {e}")
        
    if not all_errors:
        print("✅ Dataset is ready for RLHF training pipeline.")

if __name__ == "__main__":
    main()
