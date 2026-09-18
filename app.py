"""
Audra Labs — Forensic Image Authenticity Analyzer
Hackspire '26 Root Application Runner

Usage:
  python app.py
"""

import os
import sys

# Ensure backend module is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.api import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "False").lower() in ["true", "1", "yes"]
    print("\n" + "=" * 65)
    print("  AUDRA LABS — Forensic Image Authenticity Analyzer")
    print("  Hackspire '26 Edition")
    print("  Team: Nishant Kumar Sharma, Ankana Biswas, Anupam Kumari")
    print(f"  Live at: http://localhost:{port}")
    print("=" * 65 + "\n")
    app.run(host="0.0.0.0", port=port, debug=debug)
