# AI-Assisted RISC-V Specification Parameter Extractor

Independent prototype for extracting architectural parameters from short RISC-V specification excerpts into structured YAML.

> Note: This is an independent prototype built from a public-style RISC-V parameter extraction coding challenge. It focuses on structured LLM output, evidence tracking, and validation.

## Problem

RISC-V specification text contains architectural properties such as implementation-specific cache parameters, fixed CSR encoding widths, and bit-field meanings. The goal is to extract those properties into a machine-readable YAML format without hallucinating values that are not present in the supplied text.

## Approach

The extraction workflow uses an LLM prompt with strict rules:

- use only the supplied excerpt,
- include exact source evidence for every parameter,
- distinguish fixed architectural constants from implementation-specific choices,
- mark missing referenced information as unknown instead of guessing,
- output structured YAML.

## Files

- `source.txt` — input RISC-V snippets used for extraction.
- `prompt.md` — final extraction prompt.
- `riscv_challenge_results.yaml` — extracted YAML results.
- `validate_results.py` — lightweight validator for schema/evidence checks.

## Extracted Parameters

The prototype extracts six parameters:

1. `cache_capacity`
2. `cache_organization`
3. `cache_block_size`
4. `csr_address_width`
5. `csr_read_write_access_encoding`
6. `csr_lowest_accessible_privilege_encoding`

The CSR privilege-level mapping is intentionally marked as unknown because the supplied snippet references Table 1 but does not include it.

## Validation

Install dependency:

```bash
python3 -m pip install pyyaml
```

Run:

```bash
python3 validate_results.py source.txt riscv_challenge_results.yaml
```

Expected output:

```text
PASS: validated 6 parameters
```

The validator checks:

- valid YAML parsing,
- required fields,
- unique parameter names,
- valid confidence values,
- exact evidence strings present in the source text.

## Limitations

This is a small prototype tested on two RISC-V excerpts. The validator checks structure and evidence presence, but it does not prove semantic correctness. A stronger version could use JSON Schema, larger evaluation sets, table ingestion, and human-in-the-loop review.
