# ALTRON AI — Master Notes

A personal AI assistant project ("build my own JARVIS"). This document consolidates the vision, architecture, folder structure, and build roadmap into one reference.

---

## 1. Vision

ALTRON is a personal AI assistant that should be able to:

- Talk with the user
- Understand commands
- Remember information (short-term and long-term)
- Write and debug code
- Control the user's PC
- Analyze images / see the screen
- Automate repetitive tasks

---

## 2. Architecture Overview

```
User
  │
  ▼
GUI
  │
  ▼
AI Brain
  │
  ▼
Memory
  │
  ▼
Response
```

### Core Intelligence Layers

- **Brain** — understands requests, plans steps, produces solutions
- **Memory** — short-term (current conversation) + long-term (persistent facts/projects)
- **Agents** — specialized workers (coding, research, computer control)
- **Tools** — files, terminal, browser, system control
- **GUI** — chat interface
- **Voice** — speech-to-text / text-to-speech
- **Vision** — screen reading, OCR, image analysis
- **Automation** — workflows and scheduled tasks
- **IoT (optional)** — connect to real-world devices (Arduino, Raspberry Pi, sensors)

---

## 3. Component Details

### 3.1 AI Brain
Central reasoning engine. Flow: understand request → plan steps → give solution.
Needs a connected model backend — OpenAI, NVIDIA models, Hugging Face, or a local model.

**Files:** `core/brain.py`, `core/config.py`, `core/planner.py`

### 3.2 Memory
- **Short-term memory** — holds context for the current conversation only (temporary).
- **Long-term memory** — stores durable facts (e.g. active projects, preferences) that persist across sessions and can be recalled later ("continue my project").
- **RAG knowledge** — ALTRON can ingest documents (PDFs, manuals, code docs) and answer questions grounded in them.

**Files:** `memory/memory.py`, `memory/vector_memory.py`, `memory/rag.py`

### 3.3 Agent System
Rather than one monolithic AI, ALTRON delegates to specialized agents:

| Agent | Job |
|---|---|
| Coding Agent | Write code, debug, explain, scaffold projects |
| Research Agent | Find information, summarize, compare, report |
| Computer Agent | Control mouse/keyboard/files/apps/browser |
| Testing Agent | Run and validate tests |

**Files:** `agents/agent.py`, `agents/coding_agent.py`, `agents/research_agent.py`, `agents/computer_agent.py`

### 3.4 Tools
Low-level capabilities agents call into: file I/O, terminal execution, browser control, system control.

**Files:** `tools/files.py`, `tools/terminal.py`, `tools/browser.py`, `tools/system_control.py`

### 3.5 GUI
The chat-based face of ALTRON — simple input/output window.

**Files:** `gui/app.py`

### 3.6 Voice
Speech in, speech out.
Flow: your voice → speech recognition → AI brain → voice response.

**Files:** `voice/speech_to_text.py`, `voice/text_to_speech.py`

### 3.7 Vision
Screen reading, image analysis, OCR — e.g. spotting an error in a screenshot and pointing to the line number.

**Files:** `vision/camera.py`, `vision/screen.py`, `vision/ocr.py`

### 3.8 Automation
Repeated work handled automatically — e.g. an 8:00 AM routine that checks email, summarizes it, and builds a daily plan.

**Files:** `automation/workflow.py`, `automation/scheduler.py`

### 3.9 IoT (Optional / Future)
Connect ALTRON to physical devices — e.g. a temperature sensor reading triggers ALTRON to turn on a fan.

---

## 4. Folder Structure

```
ALTRON_AI/
│
├── README.md
├── NOTES/
│   └── ALTRON_ROADMAP.md
│
├── requirements.txt
├── main.py
│
├── core/
│   ├── brain.py
│   ├── config.py
│   └── planner.py
│
├── memory/
│   ├── memory.py
│   ├── vector_memory.py
│   └── rag.py
│
├── agents/
│   ├── agent.py
│   ├── coding_agent.py
│   ├── research_agent.py
│   └── computer_agent.py
│
├── tools/
│   ├── files.py
│   ├── terminal.py
│   ├── browser.py
│   └── system_control.py
│
├── gui/
│   └── app.py
│
├── voice/
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── vision/
│   ├── camera.py
│   ├── screen.py
│   └── ocr.py
│
├── automation/
│   ├── workflow.py
│   └── scheduler.py
│
└── database/
    └── memory.db
```

**Recommended project-level layout** (to survive even if chat history is lost):

```
ALTRON_AI_Project/
├── README.md
├── ALTRON_MASTER_NOTES.md   ← this file
├── source_code/
├── documentation/
└── backups/
```

---

## 5. Build Roadmap

Build incrementally, like LEGO — don't try to build everything at once.

1. **Brain** — core reasoning + model connection
2. **GUI Chat** — basic interface to talk to the brain
3. **Memory** — short-term, then long-term
4. **Tools** — files, terminal, browser, system control
5. **Agents** — coding, research, computer agents
6. **Voice** — speech in/out
7. **Vision** — screen/image understanding
8. **Automation** — workflows and scheduling
9. **IoT** — optional hardware integration

### Phase 1 Goal (first working version)

```
User → GUI → AI Brain → Memory → Response
```

Just get "Hello ALTRON" working end-to-end before adding anything else.

---

## 6. Future Features (Parking Lot)

- Multi-agent orchestration / hand-off between agents
- Local model support for offline operation
- Expanded IoT device library
- Richer RAG pipeline (multi-document, citations)
- Cross-device sync for memory/database
