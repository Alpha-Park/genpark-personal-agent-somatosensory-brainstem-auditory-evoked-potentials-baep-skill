---
name: genpark-personal-agent-somatosensory-brainstem-auditory-evoked-potentials-baep-skill
description: Evaluates brainstem auditory evoked potentials (BAEP / ABR) wave I-V absolute latencies, interpeak intervals (I-III, III-V, I-V central auditory conduction time), and interaural wave V differences.
---

# Somatosensory Brainstem Auditory Evoked Potentials (BAEP / ABR) Skill

This skill computes electrophysiological brainstem auditory conduction metrics to detect retrocochlear lesions, acoustic neuroma, and brainstem demyelinating pathology.

## Core Capabilities
- Evaluates absolute latencies for Wave I, Wave III, and Wave V.
- Computes lower pontine ($IPL\text{ I-III}$, normal $\le 2.45\text{ ms}$), rostral pontomesencephalic ($IPL\text{ III-V}$, normal $\le 2.20\text{ ms}$), and Central Auditory Conduction Time ($CACT\text{ I-V}$, normal $\le 4.40\text{ ms}$).
- Calculates Interaural Latency Difference ($ILD \le 0.40\text{ ms}$) for vestibular schwannoma detection.
- Analyzes $V/I$ amplitude ratio (normal $\ge 0.50$).

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
