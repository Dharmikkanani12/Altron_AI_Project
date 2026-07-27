# ALTRON AI

A personal AI assistant project ("build my own JARVIS"), built incrementally.

See `NOTES/ALTRON_ROADMAP.md` for the build order and `ALTRON_MASTER_NOTES.md`
(in the parent project folder) for full architecture notes.

## Quick start

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Status

Phase 1 skeleton — brain, GUI chat loop, and short-term memory wired together.
Everything else (agents, voice, vision, automation, IoT) is stubbed out with
clear TODOs so you can build it piece by piece.

## Project layout

```
ALTRON_AI/
├── main.py              Entry point
├── core/                Brain, config, planner
├── memory/               Short/long-term memory + RAG
├── agents/               Coding / research / computer agents
├── tools/                 Files, terminal, browser, system control
├── gui/                   Chat interface
├── voice/                 Speech-to-text / text-to-speech
├── vision/                 Screen/camera/OCR
├── automation/            Workflows and scheduling
└── database/               Local persistent storage
```
