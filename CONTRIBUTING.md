# Contributing to Audra Labs — Hackspire '26

Thank you for your interest in contributing to Audra Labs!

## Team

- **Nishant Kumar Sharma** — Team Lead & Backend Developer
- **Ankana Biswas** — UI/UX Designer
- **Anupam Kumari** — Frontend Developer

---

## Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/heygaurav1/Audra-Labs.git
   cd Audra-Labs
   ```

2. **Setup Python Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate       # On Windows
   source venv/bin/activate    # On macOS/Linux
   pip install -r requirements.txt
   ```

3. **Run Locally**
   ```bash
   python app.py
   ```

4. **Code Quality**
   Ensure Python syntax is valid:
   ```bash
   python -m py_compile backend/api.py app.py
   ```

---

## Areas for Contribution

- [ ] Additional multi-spectral forensic filters (e.g. PRNU camera fingerprinting)
- [ ] Real-time video deepfake stream analysis
- [ ] Extended C2PA manifest signing and certificate validation
- [ ] Export to PDF report format

---

## License

MIT License — see [LICENSE](LICENSE) for details.
