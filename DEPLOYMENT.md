# Audra Labs — Deployment Guide (Hackspire '26)

This document provides complete instructions for deploying Audra Labs across different environments.

## Deployment Options at a Glance

| Target | Complexity | Python Needed? | Best For |
| :--- | :--- | :--- | :--- |
| **Vercel** | ⭐ (1-Click) | Serverless | Instant live demo with full Python API & static HTML |
| **Docker / Compose** | ⭐ (1 Command) | Automated | Local testing, self-hosting, and cloud containers |
| **Render / Railway** | ⭐ (1-Click) | Automated | Dedicated cloud container with persistent Gunicorn |
| **GitHub Pages / Netlify** | ⭐ (Zero Config) | No (Pure Static) | Pure browser deployment via Canvas Forensic Fallback |
| **Linux VPS / Cloud VM** | ⭐⭐ (Manual) | Python 3.9+ | Nginx + Gunicorn + Systemd production architecture |

---

## 1. Deploying to Vercel (Recommended)

1. Push your repository to GitHub.
2. Visit [vercel.com](https://vercel.com) and click **Add New &rarr; Project**.
3. Import your repository.
4. (Optional) Set `ANTHROPIC_API_KEY` in **Environment Variables**.
5. Click **Deploy**. Vercel will automatically configure both the Python serverless API (`backend/api.py`) and static frontend (`index.html`) using `vercel.json`.

---

## 2. Deploying with Docker

### Single Command (Docker Compose)
```bash
docker compose up -d
```
Your app will be live at `http://localhost:5000`.

### Manual Docker Build
```bash
docker build -t audra-labs .
docker run -p 5000:5000 -e ANTHROPIC_API_KEY=your_key_here audra-labs
```

---

## 3. Deploying to Render

1. Create a New **Web Service** on [render.com](https://render.com).
2. Connect your GitHub repository.
3. Render will detect `render.yaml` automatically, or you can specify:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT backend.api:app`
4. Deploy!

---

## 4. Deploying to Railway

1. Install Railway CLI or connect via GitHub:
   ```bash
   npm i -g @railway/cli
   railway up
   ```
2. Railway reads the included `Procfile`:
   ```
   web: gunicorn -w 4 -b 0.0.0.0:${PORT:-5000} backend.api:app
   ```

---

## 5. Pure Static Hosting (GitHub Pages / Cloudflare Pages)

Because Audra Labs includes an integrated **Client-Side Canvas Forensic Engine**, you can deploy the repository directly as a static site:
1. Enable **GitHub Pages** under repository **Settings &rarr; Pages**.
2. Set source to the `main` branch root `/`.
3. Save! The app will run full Error Level Analysis and heuristic audits directly in the user's browser without requiring a backend server.

---

## Environment Variables Reference

| Variable | Required | Default | Description |
| :--- | :--- | :--- | :--- |
| `PORT` | No | `5000` | Port for Flask/Gunicorn |
| `ANTHROPIC_API_KEY` | No | `None` | Anthropic Claude API key. If omitted, local heuristics run |
| `ANTHROPIC_MODEL` | No | `claude-3-5-sonnet-20241022` | Claude model name |
| `FLASK_ENV` | No | `production` | Flask environment |
| `DEBUG` | No | `False` | Debug mode |

---

## Team

- **Nishant Kumar Sharma** — Team Lead & Backend Developer
- **Ankana Biswas** — UI/UX Designer
- **Anupam Kumari** — Frontend Developer
