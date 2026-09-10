import os 
import re
import urllib.parse

CLIENT_EMAIL = os.getenv("CLIENT_EMAIL", "")

KEYWORDS = (
  "gmail" , "email" , "e-mail" , "mail",
  "write an email" , "send an mail" , "draft an mail",
  "compose an mail" , "write mail" , "send mail" , "draft mail",
  "compose mail"
)
