# ALTRON Build Roadmap

Build incrementally — like LEGO. Don't build everything at once.

1. **Brain** — core reasoning + model connection *(scaffolded)*
2. **GUI Chat** — basic interface to talk to the brain *(scaffolded)*
3. **Memory** — short-term, then long-term *(short-term scaffolded)*
4. **Tools** — files, terminal, browser, system control *(stubs)*
5. **Agents** — coding, research, computer agents *(stubs)*
6. **Voice** — speech in/out *(stubs)*
7. **Vision** — screen/image understanding *(stubs)*
8. **Automation** — workflows and scheduling *(stubs)*
9. **IoT** — optional hardware integration *(not started)*

## Phase 1 goal

```
User → GUI → AI Brain → Memory → Response
```

Get "Hello ALTRON" working end-to-end before adding anything else.
This skeleton already wires that loop together in `main.py` — fill in
`core/brain.py`'s `call_model()` with your provider of choice (OpenAI,
NVIDIA NIM, Hugging Face, or a local model) to bring it to life.
