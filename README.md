# Hi, I'm Yuto Maruyama 👋

**AI agent engineer** at Illinois Institute of Technology. I take a messy real-world problem, sit with the people who have it, and ship an LLM agent that does the work: running a physical vending machine, scheduling meetings over LINE, underwriting real estate, turning PDFs into house-format reports, and predicting where people go next.

🌐 [Portfolio](https://yuto-portfolio.onrender.com/) · 🇯🇵 / 🇺🇸 Japanese & English

---

### How I build

- **End to end:** hardware, webhooks, databases, frontends, deployment. Whatever the problem needs, not just the model call.
- **Human in the loop by default:** agents draft, people approve, wherever a mistake costs money or trust.
- **Integrate with what people already use:** LINE, Slack/Discord, Google Calendar, Excel and PowerPoint.
- **Evaluate, don't eyeball:** generate → evaluate → refine loops and tests around the LLM parts.

---

### ⭐ Featured projects

| Project | What it does | Stack |
|---|---|---|
| 🤖 **[Claudius: AI Vending Machine](https://github.com/yuto-49/agentic-machine)** | A real vending machine run by a Claude agent. A Raspberry Pi controls the hardware, an iPad PWA is the POS, and the agent handles inventory, pricing, and customer chat over Slack/Discord. | Python · FastAPI · Claude · RPi · PWA |
| 📅 **[LINE Scheduling Agent](https://github.com/yuto-49/line-scheduling-agent)** | Reads Japanese LINE messages, checks Google Calendar, proposes slots, and drafts replies the owner approves before anything is sent. | TypeScript · Hono · Drizzle · pg-boss · Claude |
| 📄 **[Doc Agent](https://github.com/yuto-49/doc-agent)** | Turns a source PDF into an Excel workbook or PowerPoint deck that matches a "golden" example, with a scored evaluate-and-patch loop. Runs on any OpenAI-compatible LLM, including local models. | Python · Docling · openpyxl · python-pptx · Ollama |
| 🏢 **[Real Estate Agentic Platform](https://github.com/yuto-49/real-estate-agent)** | Investor analytics for Tokyo workforce housing: deterministic underwriting and stress tests, market-signal pipelines, and a parallel Claude analyst council. | FastAPI · React · Claude · Postgres · Redis |
| 🦷 **[Dental Agent](https://github.com/yuto-49/dental-agent)** | Patient education platform with a doctor dashboard plus a LINE patient agent that answers only from the clinic's published material (RAG over pgvector, in progress). | FastAPI · Next.js · pgvector · LINE · RAG |
| 🧭 **[JEPA Location World Model](https://github.com/yuto-49/jepa-location-world-model)** | Self-supervised JEPA that predicts where someone goes next by learning representations of check-in trajectories, not raw locations. | PyTorch · Transformers · TypeScript service |

<details>
<summary>More work</summary>

- **[Focus Goal App](https://github.com/yuto-49/focus-goal-app)**: mobile goal tracker with an AI coach, location/photo check-ins and accountability friends (Expo · Supabase · Claude)
- **[ConnectAI](https://github.com/yuto-49/connect-ai)**: LinkedIn-style social platform with real-time DMs and a streaming AI chat tab (Socket.io · SSE · Claude)
- **[yuto-portfolio](https://github.com/yuto-49/yuto-portfolio)**: my portfolio site with AI career guidance

</details>

---

### 🛠️ What I work with

**Agents & LLMs:** Anthropic Claude API (tool use, streaming, RAG), OpenAI-compatible / local LLMs, multi-agent orchestration, human-in-the-loop design, evaluation loops
**Backend:** Python · FastAPI · SQLAlchemy 2.0 (async) · Pydantic v2 · TypeScript · Node · Hono · Postgres · Redis · Docker
**Frontend & Mobile:** React · Next.js · Vite · React Native / Expo · Swift
**ML:** PyTorch (JEPA / Transformers) · Jupyter · data pipelines
**Integrations:** LINE Messaging API + LIFF · Google Calendar · Slack / Discord · Supabase · Raspberry Pi GPIO
