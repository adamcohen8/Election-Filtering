from pathlib import Path
import urllib.request
p=Path(__file__).resolve().parent/'sources/onpoint-oct28.xlsx'
url='https://docs.google.com/spreadsheets/d/1Zxj6w6DziLGJ6LOaw5aHMw6MdHHjHmKiQCiBoT9TgIQ/export?format=xlsx'
with urllib.request.urlopen(url,timeout=40) as r:p.write_bytes(r.read())
