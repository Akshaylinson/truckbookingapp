







 """
Run this once from the project root to download SD 1.5 inpainting.
Usage:  python download_sd_model.py

Requires:  pip install diffusers accelerate torch
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "models" / "stable-diffusion-inpainting"
CHECK = TARGET / "unet" / "config.json"

if CHECK.exists():
    print(f"[OK] Model already present at {TARGET}")
    sys.exit(0)

try:
    from diffusers import StableDiffusionInpaintPipeline
except ImportError:
    print("[error] diffusers not found. Run:  pip install diffusers accelerate torch")
    sys.exit(1)

print(f"[download] Target : {TARGET}")
print("[download] Source : stable-diffusion-v1-5/stable-diffusion-inpainting")
print("[download] Downloading model (~5 GB). This may take a while.\n")

TARGET.mkdir(parents=True, exist_ok=True)

try:
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        "stable-diffusion-v1-5/stable-diffusion-inpainting",
    )
    pipe.save_pretrained(str(TARGET))
    print(f"\n[done] Model saved to {TARGET}")
    print("[done] Restart the server — Stage 4 will now use real diffusion inference.")
except KeyboardInterrupt:
    print("\n[cancelled] Download cancelled.")
    sys.exit(1)
except Exception as exc:
    print(f"\n[error] Download failed: {exc}")
    sys.exit(1)




