# 📮 India Post Barcode & Label Generator

A professional, Python-based application to generate official India Post tracking barcodes (UPU S10 standard) and print-ready PDF labels. 

This project is available in two versions: a **Standalone Windows Desktop App (.exe)** and a **Web Application (Streamlit)**.

## ✨ Features
* **Official Standard:** Generates high-density **Code 39** barcodes adhering to Universal Postal Union (UPU) S10 standards.
* **Smart Validation:** Automatically validates the 13-character alphanumeric format (e.g., `EA123456789IN`).
* **Dual Layout Modes:**
  * **Article Number:** Generates a compact 70x120 mm label with a high-resolution barcode, bold text, and a scannable QR code.
  * **Bag Number:** Generates a pre-printed bag layout format.
* **High Quality Export:** Exports labels as 300 DPI print-ready PDF files.

## 🛠️ Tech Stack
* **Language:** Python
* **Web UI:** Streamlit
* **Desktop UI:** Tkinter
* **Core Libraries:** `python-barcode`, `qrcode`, `Pillow (PIL)`
* **Packaging (Desktop):** PyInstaller

## 🚀 How to Run (Web Version)
If you want to run the web version locally:
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt