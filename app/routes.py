from flask import Flask, render_template, request
from models import generate_response

app = Flask(__name__)

chat_history_ids = None
conversation = []

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history_ids, conversation

    if request.method == "POST":
        user_input = request.form["user_input"]
        
        # Generiere Antwort und aktualisiere den Verlauf
        response, chat_history_ids = generate_response(user_input, chat_history_ids)
        
        # Speichere Verlauf für Anzeige im HTML
        conversation.append(("You", user_input))
        conversation.append(("TheraPy", response))

    return render_template("index.html", conversation=conversation)
