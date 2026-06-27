# 🐍 Python-Projekte

> **Beispielskripte und Projekte für KI, Automatisierung und Datenanalyse**

---

## 📂 Struktur

```
projects/python/
├── ai-chatbot/          # Ein einfacher KI-Chatbot
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── data-analysis/       # Datenanalysen mit Pandas & Matplotlib
│   ├── analyze.py
│   ├── data/
│   └── README.md
└── automation/          # Automatisierungsskripte
    ├── rename_files.py
    ├── backup_script.py
    └── README.md
```

---

## 🚀 Beispiel: Einfacher KI-Chatbot

### **📌 Beschreibung**
Ein einfacher Chatbot, der auf Benutzereingaben reagiert und grundlegende KI-Funktionen nutzt.

### **📦 Abhängigkeiten**
- Python 3.8+
- `transformers` (Hugging Face)
- `torch` (PyTorch)

### **✅ Installation**
```bash
cd projects/python/ai-chatbot
pip install -r requirements.txt
```

### **🏃‍♂️ Ausführung**
```bash
python main.py
```

---

## 📊 Beispiel: Datenanalyse

### **📌 Beschreibung**
Skripte zur Analyse von Daten mit **Pandas, NumPy und Matplotlib**.

### **📦 Abhängigkeiten**
- Python 3.8+
- `pandas`
- `numpy`
- `matplotlib`

### **✅ Installation**
```bash
cd projects/python/data-analysis
pip install -r requirements.txt
```

### **🏃‍♂️ Ausführung**
```bash
python analyze.py
```

---

## 🤖 Beispiel: Automatisierung

### **📌 Beschreibung**
Skripte zur Automatisierung von Aufgaben wie **Dateiverwaltung, Backups und Web-Scraping**.

### **📦 Abhängigkeiten**
- Python 3.8+
- `requests` (für HTTP-Anfragen)
- `beautifulsoup4` (für Web-Scraping)

### **✅ Installation**
```bash
cd projects/python/automation
pip install -r requirements.txt
```

---

## 📝 Hinweise
- **Virtual Environment**: Nutze `venv` oder `conda`, um Abhängigkeiten zu isolieren.
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows
  ```
- **Docker**: Für komplexere Projekte kannst du Docker verwenden. Siehe [Docker-Dokumentation](https://docs.docker.com/).

---

## 🔗 Nützliche Links
- [Python Dokumentation](https://docs.python.org/3/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Pandas Dokumentation](https://pandas.pydata.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
