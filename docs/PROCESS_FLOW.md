# Real-Time Fraud Detection ML Platform: process flows

## Domain request

Endpoint: `POST /score`. Stages summarize [src/rtfraud/score.py](../src/rtfraud/score.py). This is in-process Python, not a hosted model or production apply.

```mermaid
flowchart TD
  A["POST /score"] --> B{"Valid input?"}
  B -->|"No"| E["HTTP 422"]
  B -->|"Yes: Required numeric features present"| C["Domain function in score.py"]
  C --> O["linear score; hold if total >= 0; no charge"]
  O --> X["No production side effect"]
```

See [INTERVIEW_QA.md](../INTERVIEW_QA.md) for fixture walkthroughs and [PROJECT_ARCHITECTURE.md](../PROJECT_ARCHITECTURE.md) for the component map.
