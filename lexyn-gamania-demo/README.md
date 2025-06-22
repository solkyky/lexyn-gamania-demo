# Lexyn Context Guard · Gamania Demo

> **400 ms 內偵測並改寫遊戲對話毒性**

![demo](./demo.gif)

## Features
- `/analyze` REST API — JSON in/out
- Docker & GitHub CI — build verified on every push

## Quick Start
```bash
docker build -t lexyn-demo .
docker run -p 8000:8000 lexyn-demo
curl -X POST http://localhost:8000/analyze \
     -H "Content-Type: application/json" \
     -d '{"text":"Hello"}'
```

## Roadmap
- [ ] GPT-4o Integration
- [ ] LoRA Fine-tune (phi-2)
- [ ] RAG + FAISS
- [ ] AWS Lightsail Deployment