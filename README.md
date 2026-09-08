# AI Engineer Assessment — Q&A Chatbot

A small FastAPI service with a single endpoint, `POST /ask`. It takes a natural-language
question, decides whether it is about **superheroes**, a **local text dataset**, or **both**,
pulls information from the right source(s), and uses a hosted LLM to compose a clear answer.
Every response also reports **which sources** the information came from.

- **Superhero data** comes from the [Superhero API](https://superheroapi.com/).
- **Dataset data** comes from a small local text file (`app/data/dataset.txt`) covering topics
  like FastAPI, Docker, ETL, and Airflow.
- **Answer generation** uses a real hosted LLM — **Google Gemini** (default) or **NVIDIA NIM**.

---

## 1. Setup

Requires **Python 3.12+**.

```bash
# clone, then from the project root:
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Configure your keys

Copy the example env file and paste in your own keys:

```bash
cp .env.example .env
```

Then edit `.env`:

| Variable | What it is | Where to get it |
|---|---|---|
| `SUPERHERO_API_TOKEN` | Superhero API access token | Sign in with GitHub at [superheroapi.com](https://superheroapi.com/) |
| `LLM_PROVIDER` | `gemini` or `nvidia` | — |
| `LLM_API_KEY` | API key for the chosen provider | Gemini: [aistudio.google.com/apikey](https://aistudio.google.com/apikey) · NVIDIA: [build.nvidia.com](https://build.nvidia.com/) |
| `LLM_MODEL` | Model id for the chosen provider | e.g. `gemini-3.6-flash` for Gemini |

> To switch between providers, just change `LLM_PROVIDER`, `LLM_API_KEY`, and `LLM_MODEL`.
> No code changes needed.

## 3. Run

```bash
uvicorn app.main:app --reload
```

The API is now at `http://127.0.0.1:8000`. Interactive docs (Swagger UI) are at
`http://127.0.0.1:8000/docs` — the easiest way to try `/ask` from a browser.

## 4. Call `/ask`

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Tell me about Batman and FastAPI"}'
```

Example response:

```json
{
  "question": "Tell me about Batman and FastAPI",
  "answer": "Batman (Bruce Wayne) is a good-aligned superhero known for high intelligence. FastAPI is a modern Python web framework for building APIs, based on type hints...",
  "sources": ["superhero_api", "dataset", "llm"]
}
```

`sources` tells you where the answer came from — `superhero_api`, `dataset`, or both,
plus `llm` for the model that composed the final text.

---

## Notes & design decisions

- **Routing** is keyword-based (a curated list of superhero names and dataset topics). It is
  simple and fast; the tradeoff is that it only recognizes known terms and defaults to the
  dataset otherwise.
- **Provider abstraction** — both LLMs sit behind a common `LLMProvider` interface selected by
  a factory, so adding a provider means adding one class.
- **Graceful failure** — Superhero API and LLM errors (timeouts, rate limits, outages) are caught
  and mapped to friendly messages instead of crashing the endpoint. Free-tier LLM keys have low
  daily quotas, so a `429` returns a "temporarily unavailable" message rather than an error.

## Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/ask` | Ask a question (`{"question": "..."}`) |
| `GET` | `/health` | Health check |
