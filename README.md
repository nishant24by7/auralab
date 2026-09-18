# Audra Labs — Forensic Image Authenticity Analyzer

**Detect. Verify. Protect.**  
*Official Submission for **Hackspire '26***

An enterprise-grade forensic image authenticity analyzer powered by Claude Vision AI, physical Error Level Analysis (ELA), 2D Fourier (FFT) noise decomposition, and cryptographic C2PA provenance verification. Uncover synthetic deepfakes, pixel splicing, steganographic payloads, and cyber threats in under 2 seconds.

---

## 🚀 Key Features for Hackspire '26

- ⚡ **1-Click Judge Demo Presets**: Test synthetic deepfake faces, authentic DSLR photos, spliced contracts, and steganography payloads with a single click.
- 🔥 **Error Level Analysis (ELA) Heatmap**: Re-compresses images to compute pixel-wise compression error delta and visualizes anomalous regions.
- 🔬 **Interactive 10x Forensic Loupe**: Hover magnifying glass tool to inspect suspicious pixel blocks and high-frequency noise grids up close.
- 🌡️ **Multi-Layer Vision Switcher**: Toggle between ELA delta, Thermal blood-flow simulation, High-pass noise residual, and Original image layers.
- 📷 **Live Optical Capture (Webcam)**: Audit real-time camera snapshots directly from the browser to verify hardware sensor provenance.
- 🛡️ **Steganography & Malware Scanner**: LSB bitstream entropy audit and EOF trailing binary payload detector to uncover covert malware channels.
- 📜 **Cryptographic Certificate of Authenticity**: Generates tamper-evident forensic certificates complete with SHA-256 checksums and Hackspire '26 seals.
- 🌐 **Zero-Friction Hybrid Architecture**: Runs with full Python Flask backend + Claude Vision API when configured, or auto-switches to an in-browser HTML5 Canvas forensic engine when offline or statically hosted. Never fails for judges.

---

## 👥 The Team

- **Nishant Kumar Sharma** — Team Lead & Backend Developer
- **Ankana Biswas** — UI/UX Designer
- **Anupam Kumari** — Frontend Developer

---

## 🛠️ Tech Stack

### Frontend
- HTML5 Canvas & Web Crypto API (`crypto.subtle` for SHA-256)
- Vanilla CSS with Cyber-Forensic HUD aesthetic & Dark/Light mode
- Space Grotesk, JetBrains Mono, and Rajdhani typography
- Interactive 10x forensic magnification loupe
- Standalone zero-dependency runtime

### Backend
- **Python 3.9+ / 3.11** with Flask & Gunicorn
- **Pillow (PIL)** for Error Level Analysis & thermal colorization
- **NumPy** for 2D Fast Fourier Transform (FFT) spectral decomposition
- **Anthropic Claude 3.5 Sonnet / Vision** for multi-modal cognitive reasoning
- **Deterministic Heuristic Engine** for instant zero-config judging

### Deployment & Cloud
- **Vercel** (Serverless Python functions & Edge static delivery)
- **Docker & Docker Compose** (Containerized single-command execution)
- **Render / Railway / Heroku** (`render.yaml` & `Procfile` ready)
- **Static Hosting** (GitHub Pages / Cloudflare Pages / Netlify via canvas fallback)

---

## ⚡ Quick Start

### Option 1: Instant Python Runner (Zero Setup)
```bash
# 1. Clone the repository
git clone https://github.com/heygaurav1/Audra-Labs.git
cd Audra-Labs

# 2. Run directly with Python (Dependencies auto-fallback if not installed)
python app.py
```
Open **`http://localhost:5000`** in your browser.

### Option 2: Full Local Environment
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On macOS/Linux

# Install requirements
pip install -r requirements.txt

# (Optional) Add your Anthropic API Key in .env
cp .env.example .env

# Run app
python app.py
```

### Option 3: Docker (1-Command Run)
```bash
# Run with Docker Compose
docker compose up

# Or build manually
docker build -t audra-labs .
docker run -p 5000:5000 audra-labs
```

### Option 4: Pure Static / No Python
You can also directly double-click **`index.html`** or serve it with any web server (`npx serve .`):
Audra Labs includes a built-in **Client-Side Canvas Forensic Engine** that executes Error Level Analysis and heuristic audits directly in the browser!

---

## ☁️ Easy Deployment

### Deploy to Vercel (1-Click)
1. Push repository to GitHub.
2. Import project into [vercel.com](https://vercel.com).
3. (Optional) Add `ANTHROPIC_API_KEY` in Project Settings &rarr; Environment Variables.
4. Click **Deploy**. Vercel automatically deploys both `index.html` and `backend/api.py`.

### Deploy to Render
1. Create a New **Web Service** on [render.com](https://render.com).
2. Connect your repository. Render automatically reads `render.yaml`.
3. Set start command to `gunicorn -w 4 -b 0.0.0.0:$PORT backend.api:app`.

### Deploy to Railway / Heroku
The included `Procfile` is pre-configured:
```
web: gunicorn -w 4 -b 0.0.0.0:${PORT:-5000} backend.api:app
```

---

## 🔬 API Endpoints

### `GET /api/health`
Returns system status, active forensic engines, and team metadata.

### `GET /api/engines`
Lists all 12 forensic detection engines with descriptions.

### `POST /api/analyze`
Submits image for complete forensic pipeline analysis.
```json
{
  "image": "<base64_encoded_image>",
  "mimeType": "image/jpeg",
  "fileName": "sample.jpg"
}
```

**Response Format:**
```json
{
  "verdict": "AUTHENTIC | TAMPERED | SUSPICIOUS",
  "confidence": 98,
  "fraud_risk_score": 12,
  "ai_generation_score": 14,
  "metadata_integrity": 95,
  "noise_pattern_anomaly": 12,
  "steganography_risk": 8,
  "biological_anomaly": 6,
  "physics_consistency_issues": 10,
  "heatmap": "data:image/png;base64,...",
  "threat_indicators": ["..."],
  "why_fake_proof": "...",
  "engine_results": [...],
  "forensic_features": {
    "sha256": "3a7bd3e236...",
    "width": 1920,
    "height": 1080,
    "format": "JPEG",
    "compression_ela_score": "14%"
  }
}
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Built with ❤️ for Hackspire '26**  
*Audra Labs — Detect. Verify. Protect.*
