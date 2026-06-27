# 🤖 Einfacher KI-Chatbot

> **Ein Chatbot mit Hugging Face Transformers und PyTorch**

---

## 📌 Beschreibung

Dieses Projekt demonstriert, wie man einen **einfachen KI-Chatbot** mit einem vorgefertigten **Sprachmodell von Hugging Face** erstellt. Der Chatbot nutzt das **`distilgpt2`-Modell**, ein kleines, aber leistungsfähiges Modell für Textgenerierung.

---

## ✅ Voraussetzungen

- **Python 3.8 oder höher**
- **Internetverbindung** (zum Herunterladen des Modells beim ersten Start)
- **Mindestens 2 GB RAM** (für das Modell)

---

## 📦 Installation

### **1. Virtual Environment erstellen (empfohlen)**
```bash
# Erstelle ein virtuelles Environment
python -m venv venv

# Aktiviere das Environment
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### **2. Abhängigkeiten installieren**
```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ Ausführung

### **Chatbot starten**
```bash
python main.py
```

### **Beispiel-Interaktion**
```
🤖 Willkommen zum einfachen KI-Chatbot!
💬 Tippe 'exit' oder 'quit', um das Programm zu beenden.

⏳ Lade KI-Modell... (Dies kann beim ersten Mal einige Sekunden dauern)
✅ Modell erfolgreich geladen!

👤 Du: Hallo!
🤖 Chatbot: Hallo! Wie kann ich dir heute helfen?

👤 Du: Was ist KI?
🤖 Chatbot: Künstliche Intelligenz (KI) ist ein Bereich der Informatik, der sich mit der Entwicklung von Systemen beschäftigt, die Aufgaben ausführen können, die normalerweise menschliche Intelligenz erfordern.

👤 Du: exit
👋 Auf Wiedersehen!
```

---

## 🛠️ Anpassungen

### **Modell ändern**
Du kannst das Modell in der `main.py`-Datei ändern. Hier sind einige Alternativen:

| **Modell** | **Beschreibung** | **Größe** | **Geschwindigkeit** |
|------------|----------------|-----------|---------------------|
| `distilbert/distilgpt2` | Kleines GPT-2-Modell | ~250 MB | ⭐⭐⭐⭐⭐ |
| `gpt2` | Standard GPT-2-Modell | ~500 MB | ⭐⭐⭐⭐ |
| `EleutherAI/gpt-neo-125M` | Größeres Modell | ~500 MB | ⭐⭐⭐ |
| `facebook/blenderbot-400M-distill` | Chatbot-spezifisches Modell | ~1.5 GB | ⭐⭐ |

**Beispiel:**
```python
# In main.py
chatbot = pipeline(
    "text-generation",
    model="gpt2",  # Modell ändern
    device=-1,
    max_length=100,
)
```

---

### **Parameter anpassen**
Du kannst die **Generierungsparameter** anpassen, um die Antworten zu beeinflussen:

| **Parameter** | **Beschreibung** | **Standardwert** | **Empfohlener Bereich** |
|---------------|----------------|------------------|-------------------------|
| `max_length` | Maximale Länge der generierten Antwort | `100` | `50-200` |
| `temperature` | Kreativität (niedrig = deterministisch, hoch = zufällig) | `0.7` | `0.1-1.0` |
| `top_k` | Anzahl der wahrscheinlichsten Tokens, die berücksichtigt werden | `50` | `10-100` |
| `top_p` | Wahrscheinlichkeitsschwelle für Token-Auswahl | `0.95` | `0.1-1.0` |

**Beispiel:**
```python
chatbot = pipeline(
    "text-generation",
    model="distilbert/distilgpt2",
    max_length=150,  # Längere Antworten
    temperature=0.9,  # Kreativere Antworten
)
```

---

## 💡 Tipps

### **GPU verwenden (für schnellere Ausführung)**
Falls du eine **NVIDIA-Grafikkarte** mit CUDA-Unterstützung hast, kannst du das Modell auf der GPU ausführen:

1. Installiere PyTorch mit CUDA:
   ```bash
   pip uninstall torch
   pip install torch --extra-index-url https://download.pytorch.org/whl/cu118
   ```

2. Ändere in `main.py` den `device`-Parameter:
   ```python
   chatbot = pipeline(
       "text-generation",
       model="distilbert/distilgpt2",
       device=0,  # 0 = erste GPU
   )
   ```

### **Modell lokal speichern**
Beim ersten Start wird das Modell **automatisch heruntergeladen**. Falls du es **offline verwenden** möchtest, kannst du es manuell speichern:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Modell und Tokenizer laden und speichern
model_name = "distilbert/distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Speichern
model.save_pretrained("./models/distilgpt2")
tokenizer.save_pretrained("./models/distilgpt2")
```

---

## ❌ Bekannte Einschränkungen

- **Lange Ladezeit beim ersten Start**: Das Modell wird beim ersten Mal **heruntergeladen** (ca. 250 MB).
- **Begrenzte Kontextlänge**: Das Modell kann nur **begrenzte Kontexte** verarbeiten (max. ~100 Tokens).
- **Kein Gedächtnis**: Der Chatbot hat **kein Gedächtnis** für vorherige Nachrichten (jeder Input wird unabhängig verarbeitet).
- **Qualität der Antworten**: Kleine Modelle wie `distilgpt2` können **unzusammenhängende oder unsinnige Antworten** generieren.

---

## 🔗 Nützliche Links

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) – Dokumentation
- [Hugging Face Model Hub](https://huggingface.co/models) – Modelle entdecken
- [PyTorch Dokumentation](https://pytorch.org/docs/stable/index.html) – PyTorch lernen
- [DistilGPT2 Modell](https://huggingface.co/distilbert/distilgpt2) – Modell-Details

---

## 📜 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Siehe [LICENSE](../../../LICENSE) für Details.
