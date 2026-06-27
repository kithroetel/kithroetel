#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 Einfacher KI-Chatbot mit Hugging Face Transformers

Dieses Skript demonstriert, wie man einen einfachen Chatbot mit einem
vorgefertigten Sprachmodell von Hugging Face erstellt.

Anforderungen:
- Python 3.8+
- transformers (Hugging Face)
- torch (PyTorch)

Installation:
    pip install transformers torch

Verwendung:
    python main.py
"""

from transformers import pipeline
import warnings

# Ignoriere Warnungen von Hugging Face
warnings.filterwarnings("ignore")


def main():
    print("🤖 Willkommen zum einfachen KI-Chatbot!")
    print("💬 Tippe 'exit' oder 'quit', um das Programm zu beenden.\n")

    # Lade das Sprachmodell (kleines Modell für schnelle Ausführung)
    print("⏳ Lade KI-Modell... (Dies kann beim ersten Mal einige Sekunden dauern)")
    try:
        # Verwende ein kleines, schnelles Modell für die Demonstration
        chatbot = pipeline(
            "text-generation",
            model="distilbert/distilgpt2",  # Kleines GPT-2-Modell
            device=-1,  # CPU verwenden (für GPU: device=0)
            max_length=100,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
        )
        print("✅ Modell erfolgreich geladen!\n")
    except Exception as e:
        print(f"❌ Fehler beim Laden des Modells: {e}")
        print("💡 Tipp: Stelle sicher, dass du eine Internetverbindung hast und die Abhängigkeiten installiert sind.")
        return

    # Chat-Schleife
    while True:
        user_input = input("👤 Du: ").strip()

        if user_input.lower() in ["exit", "quit", "beenden"]:
            print("👋 Auf Wiedersehen!")
            break

        if not user_input:
            print("⚠️  Bitte gib eine Nachricht ein.")
            continue

        # Generiere die Antwort des Chatbots
        try:
            # Formatierung für das Modell
            prompt = f"<s>[USER] {user_input} [/USER] [ASSISTANT]"
            
            # Generiere die Antwort
            response = chatbot(
                prompt,
                max_length=100,
                num_return_sequences=1,
                pad_token_id=50256,  # GPT-2's EOS-Token
            )

            # Extrahiere die Antwort und bereinige sie
            bot_response = response[0]["generated_text"]
            
            # Entferne den Prompt aus der Antwort
            if prompt in bot_response:
                bot_response = bot_response.replace(prompt, "")
            
            # Entferne spezielle Tokens
            bot_response = bot_response.replace("</s>", "").strip()
            
            print(f"🤖 Chatbot: {bot_response}")
        except Exception as e:
            print(f"❌ Fehler bei der Generierung der Antwort: {e}")


if __name__ == "__main__":
    main()
