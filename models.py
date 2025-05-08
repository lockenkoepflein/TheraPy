from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Lade Tokenizer und Modell von Hugging Face
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def generate_response(user_input, history=None):
    # Benutzer-Eingabe in Tokens umwandeln
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Bestehenden Verlauf anhängen, aber auf die letzten 1000 Tokens begrenzen
    if history is not None:
        # Kürze alten Verlauf (falls zu lang)
        if history.shape[-1] > 1000:
            history = history[:, -1000:]
        bot_input_ids = torch.cat([history, new_input_ids], dim=-1)
    else:
        bot_input_ids = new_input_ids

    # Antwort generieren mit Sampling-Strategie (für Abwechslung)
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )

    # Antwort aus den Tokens extrahieren
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    return response, chat_history_ids
