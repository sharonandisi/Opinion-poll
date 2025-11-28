#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

NOTEBOOK="${1:-gatundu_poll_analysis.ipynb}"
SYNTH_FILE="${SYNTHETIC_FILE:-synthetic_responses.csv}"
OUTPUT_DIR="${OUTPUT_DIR:-build}"
KERNEL_NAME="${KERNEL_NAME:-python3}"

if [[ ! -f "$SYNTH_FILE" ]]; then
  echo "Synthetic dataset not found at $SYNTH_FILE. Generating..."
  python generate_synthetic_responses.py
fi

cp "$SYNTH_FILE" responses.csv
mkdir -p "$OUTPUT_DIR"

BASENAME="$(basename "${NOTEBOOK%.ipynb}")"
EXEC_NOTEBOOK="$OUTPUT_DIR/${BASENAME}_executed.ipynb"
HTML_REPORT="$OUTPUT_DIR/${BASENAME}.html"

echo "Executing $NOTEBOOK..."
jupyter nbconvert \
  --to notebook \
  --execute "$NOTEBOOK" \
  --output "${BASENAME}_executed.ipynb" \
  --output-dir "$OUTPUT_DIR" \
  --ExecutePreprocessor.timeout=600 \
  --ExecutePreprocessor.kernel_name="$KERNEL_NAME"

echo "Exporting HTML snapshot..."
jupyter nbconvert \
  --to html "$EXEC_NOTEBOOK" \
  --output "${BASENAME}.html" \
  --output-dir "$OUTPUT_DIR"

echo "Finished. Outputs stored in $OUTPUT_DIR/"

