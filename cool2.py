import os
import webbrowser
import requests

url = "https://jtoh.fandom.com/api.php"
headers = {"User-Agent": "MyJToHBot/1.0"}

john = input("search for what?")
params = {
    "action": "parse",
    "page": john,
    "prop": "text", 
    "format": "json",
}

r = requests.get(url, params=params, headers=headers)
data = r.json()


html_content = data["parse"]["text"]["*"]


full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <base href="https://jtoh.fandom.com/">
    <title>{data["parse"]["title"]}</title>
</head>
<body>
    {html_content}
</body>
</html>
"""

file_path = os.path.abspath("jtoh_page.html")
with open(file_path, "w", encoding="utf-8") as f:
  f.write(full_html)

webbrowser.open(f"file://{file_path}")