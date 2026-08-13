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