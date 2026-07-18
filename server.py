import os
import sys
import json
import socket
import requests
from flask import Flask, request, Response, jsonify
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# Configuration from environment variables
PORT = int(os.environ.get("PORT", 3000))
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"


def validate_startup():
    """Validate all required dependencies and configurations before startup."""
    
    # Check GROQ_API_KEY
    if not GROQ_API_KEY:
        print("❌ ERROR: GROQ_API_KEY not set in .env file")
        print("📋 Setup: cp .env.example .env && add your GROQ_API_KEY")
        sys.exit(1)
    
    # Check port availability
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("127.0.0.1", PORT))
    sock.close()
    
    if result == 0:
        print(f"❌ ERROR: Port {PORT} is already in use")
        print(f"💡 Solution: Change PORT in .env or kill the process using port {PORT}")
        sys.exit(1)
    
    print("✅ All validations passed!")
    print(f"🚀 Starting server on port {PORT} (debug={DEBUG})")


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
    validate_startup()
    app.run(port=PORT, debug=DEBUG)
