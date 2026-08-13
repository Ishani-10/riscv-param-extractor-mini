# Extraction Prompt

This file contains the final prompt used for the RISC-V architectural parameter extraction prototype.

## Final Prompt

You are extracting architectural parameters from a supplied RISC-V ISA specification excerpt.

Return only valid YAML with this structure:

```yaml
parameters:
  - name: string
    description: string
    type: string
    constraints: list
    source:
      section: string
      evidence: string
    confidence: high|medium|low
```

## Extraction Rules

1. Extract a parameter only when the excerpt identifies a property, field, encoding, implementation choice, or required architectural value.
2. Preserve the distinction between implementation-specific, implementation-defined, optional, may/might/should, and shall.
3. Mark fixed encoding widths and meanings as fixed by the standard.
4. For every item, include a short exact evidence span from the excerpt.
5. Do not use outside knowledge. If a table or definition is missing, record that it is unavailable instead of inventing its contents.
6. Keep numeric values with their units.
7. Separate each parameter from its constraints.
8. Omit unsupported properties rather than hallucinating them.
9. Use snake_case names and descriptive types.
10. Verify that every result has evidence in the supplied excerpt.

## Input Format

Paste the specification excerpt after this line:

```text
Input excerpt:
<<<PASTE EXCERPT HERE>>>
```

## Hallucination Controls

The prompt was designed to reduce unsupported extraction by requiring:

- exact evidence from the supplied text,
- no external knowledge,
- explicit representation of missing information,
- distinction between fixed ISA properties and implementation-specific choices,
- structured YAML output,
- manual and script-based validation after generation.

## Notes

This prompt was used to extract architectural parameters from two RISC-V privileged specification snippets involving cache block properties and CSR address encoding.
