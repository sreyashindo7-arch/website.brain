# ⏰ Smart Alarm — website.brain

> **A cognitive alarm clock that forces you awake using AI-powered brain challenges.**

---

## 🧠 The Problem

Standard alarm clocks are trivially easy to dismiss. A single tap sends most people straight back to sleep — defeating the entire purpose. The average person snoozes their alarm **3–4 times** per morning, losing up to 30 minutes of productive time daily.

## 💡 Our Solution

**Smart Alarm** is a browser-based alarm clock that **won't let you go back to sleep**. When the alarm rings, you are presented with a **wake-up brain challenge** (powered by Google Gemini AI) that you *must* solve correctly before the alarm can be silenced. No task solved = no silence.

This forces a moment of genuine cognitive engagement at the exact moment you're tempted to doze off — effectively breaking the lazy-snooze cycle.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| ⏰ **Smart Alarm** | Set an alarm for any time; it rings precisely on schedule |
| 🧠 **Brain Challenge Gate** | Must solve a math/logic task to stop the alarm |
| 😴 **5-Minute Snooze** | Snooze is allowed, but the challenge returns when it ends |
| 🔊 **Web Audio Alarm** | Pulsing alarm sound generated via Web Audio API (no files needed) |
| 🤖 **Gemini AI Backend** | FastAPI + Google Gemini 2.0 Flash for AI-generated content |
| ☁️ **Vercel Deployed** | Production-ready serverless deployment |

---

## 🛠️ Tech Stack

### Frontend
- **Pure HTML / CSS / JavaScript** — zero frameworks, zero dependencies
- **Glassmorphism UI** with animated clock and responsive design
- **Web Audio API** for synthesized alarm sound

### Backend
- **Python + FastAPI** — lightweight, async-ready API server
- **Google Gemini 2.0 Flash** (`gemini-2.0-flash`) — AI model for generating challenge content
- **Jinja2 Templates** — server-side rendering
- **Vercel** — serverless deployment via `vercel.json`

---

## 🚀 How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn instant:app --reload
```

Then open `http://localhost:8000` in your browser.

For the standalone frontend (no server needed):
> Simply open `queerwell/website.brain.html` directly in any browser.

---

## 📁 Project Structure

```
├── instant.py              # FastAPI app with Gemini AI integration
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel serverless deployment config
├── queerwell/
│   ├── website.brain.html  # Main Smart Alarm frontend (self-contained)
│   ├── index.html          # Landing page
│   └── styles.css          # Stylesheet
└── llm2/
    ├── main.py             # Extended FastAPI + Gemini chat backend
    └── templates/
        └── index.html      # Chat UI template
```

---

## 🎯 Why This Matters

- **No app install needed** — runs in any browser
- **No internet required for the alarm** — core alarm is fully client-side
- **AI-ready architecture** — backend is wired to Gemini to serve dynamic, personalized challenges
- **Scalable** — the challenge difficulty can be tuned via Gemini prompts

---

## 👥 Team

| Name | GitHub |
|---|---|
| Sreyashin | [@sreyashindo7-arch](https://github.com/sreyashindo7-arch) |
| Aswathy | [@aswathyjay](https://github.com/aswathyjay) |

---

## 📌 Important Notes for Judges

- The **live frontend** works entirely offline in a browser — no server needed to demo the core alarm feature.
- The **Gemini AI integration** (`instant.py`) is deployed on Vercel and generates enthusiastic, dynamic content on each page load — demonstrating real LLM integration.
- The project was built with **accessibility and simplicity in mind** — any user can understand and use it immediately without onboarding.
- Future roadmap includes: voice-based challenges, Gemini-generated personalized puzzles, and streak tracking.
