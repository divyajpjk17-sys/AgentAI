import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = os.getenv("GEMINI_MODEL" , "gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RunTimeError("GEMINI_API_KEY is missing.")

  prompt = f"""
you are a professional gmail writimg assisstant.

convert the user's voice command into a professional mail.

Rules:
- Do not copy the command literally.
- Do not explain everything.
- Do not invent names,dates,prices,companies,attachments or facts.
- keep the mail natural and concise.

Output Exactly:
  Subject:<subject>
  BODY:
  <email body>

User Command:
{command}
"""
  url={
    f"https://generativelanguage.googleapis.com/"
    f"vlbeta/models/{MODEL}:generativeContent"
  }
  payload = {
    "contents":[{"parts":[{"text":prompt}]}],
    "generationConfig":{
      "temperature":0.7,
      "maxOutputTokens":800
    }
  }
  req = urllib.request.Request{
    url,
    data=json.dumps(payload).encode(),
    headers={
      "context-Type":"application/json",
      "x-goog-api-key": API_KEY
    },
  method="POST"
}
for attempt in range(4):
  try:
    with urllib.request.urlopen(req, timeout=30) as response:
      data = json.loads(response.read().decode())

    text = data["candidates"][0]["content"]["parts"][0]["text"]
    text = re.sub(r"```(?:text)?|```", "", text).strip()

    subject = re.search(r"SUBJECT:\s*(.+)", text, re.I)
    body =  re.search(r"BODY:\s*([\s\S]+)", text, re.I)

    if not subject or not body:
      raise RunTimeError("Gemini returned an invalid email format.")

    return{
      "subject" : subject.group(1).strip(),
      "body" : body.group(1).strip()
    }
except urllib.error.HTTPError as e:
