# 📮 India Post Barcode & Label Generator

A professional, Python-based application to generate official India Post tracking barcodes (UPU S10 standard) and print-ready PDF labels. 

This project is available in two versions: a **Live Web Application** and a **Standalone Windows Desktop App (.exe)**.

---

## 🌐 Live Web Application
Aap bina kisi installation ke seedha browser se isko use kar sakte hain:  
👉 **[Click Here to Open Live Web App](https://indiapost-label-web.streamlit.app)** *(Apna Streamlit link yahan dal sakte hain)*

---

## 💻 Download Windows Desktop App (.exe)
Agar aapko apne computer par offline software chalana hai:
1. Is repository ke **[Releases](https://github.com/navdeepsahrawat645/indiapost-label-web/releases)** section mein jayiye.
2. Wahan se latest **`IndiaPost Barcode Generator.exe`** file download kar lijiye.
3. Isko direct Windows par run karein (Python install hone ki koi zarurat nahi hai).

---

## ✨ Features
* **Official Standard:** Generates high-density **Code 39** barcodes adhering to Universal Postal Union (UPU) S10 standards.
* **Strict Format Validation:** Automatically validates 13-character article numbers (`2 Letters + 9 Digits + 2 Letters`, e.g., `AY847874894IN`).
* **Fast Input Support:** Full **Enter key** support for instant label generation.
* **Dual Layout Modes:**
  * **Article Number:** Generates a compact 70x120 mm label with a high-resolution barcode, clear bold font (`arialbd.ttf`), and a scannable QR code.
  * **Bag Number:** Generates a pre-printed bag layout format.
* **High Quality Export:** Exports labels as 300 DPI print-ready PDF files.

## 🛠️ Tech Stack
* **Language:** Python
* **Web UI:** Streamlit
* **Desktop UI:** Tkinter
* **Core Libraries:** `python-barcode`, `qrcode`, `Pillow (PIL)`
* **Packaging (Desktop):** PyInstaller

---
**Version:** 2.0  
**Developed by:** Navdeep Singh SA D Dn © 2026