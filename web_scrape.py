import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kaster en exception hvis responsen er en 4xx eller 5xx feilkode.

        soup = BeautifulSoup(response.text, 'html.parser')

        # Fjern alle <script>, <style>, og <link> tags
        for script in soup(["script", "style", "link"]):
            script.extract()  # fjerner taggen fra soup

        text = soup.get_text()

        cleaned_text = text.replace('\n', ' ')


        return str(cleaned_text)

    except requests.RequestException as e:
        return f"Feil ved henting av nettside: {e}"

