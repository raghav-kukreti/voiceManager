import requests as _req

def main_reader(url, n=5):
    from bs4 import BeautifulSoup as bs
    response = _req.get(url)
    if not response.ok:
        return False
    page = response.content
    soup = bs(page, "lxml")
    final_value = "\n".join([x.text for x in soup.findAll("textarea") if len(x.text.split()) > 1])
    return final_value

print(main_reader('http://localhost:5000'))
