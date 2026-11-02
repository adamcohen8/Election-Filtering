from pathlib import Path
import urllib.request
p=Path(__file__).resolve().parent/'sources/psu-generic.png'
with urllib.request.urlopen('https://democracy.psu.edu/wp-content/uploads/sites/14/2026/10/MOTN1.png',timeout=30) as r:p.write_bytes(r.read())
