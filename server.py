import os
import json
import requests
from flask import Flask, request, Response, jsonify
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is not set. Add it to your .env file.")


@app.route("/api/ai-solve", methods=["POST"])
def ai_solve():
    body = request.get_json(silent=True) or {}
    messages = body.get("messages", [])
    max_tokens = body.get("max_tokens", 1500)
    temperature = body.get("temperature", 0.3)
    stream = body.get("stream", True)

    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": stream,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}",  # never sent to the browser
    }

    upstream = requests.post(GROQ_URL, headers=headers, json=payload, stream=stream)

    if not upstream.ok:
        try:
            err = upstream.json()
        except ValueError:
            err = {"error": {"message": upstream.text}}
        return jsonify(err), upstream.status_code

    if not stream:
        return jsonify(upstream.json())

    # Pipe the SSE stream straight through so the frontend's existing
    # streaming/parsing code in runAI() keeps working unchanged.
    def generate():
        for line in upstream.iter_lines(decode_unicode=True):
            if line is not None:
                yield line + "\n"

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    app.run(port=3000, debug=True)
