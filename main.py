import rumps
import requests
from bs4 import BeautifulSoup

def fetch_live_score():
    url = "https://www.cricbuzz.com/live-cricket-scores/89745/kkr-vs-dc-16th-match-indian-premier-league-2024"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    match_status = soup.find("div", class_="cb-col cb-col-100 cb-min-stts cb-text-complete").text.strip()
    score_div = soup.find('div', class_='cb-col cb-col-100 cb-col-scores')
    score_text = score_div.find('div', class_='cb-col cb-col-67 cb-scrs-wrp').text.strip() if score_div else "Score div not found on the page."
    return match_status, score_text

class LiveScoreApp(rumps.App):
    def __init__(self):
        super(LiveScoreApp, self).__init__("")  # No title
        self.menu = []
        self.update_scores()

    def update_scores(self):
        try:
            match_status, score_text = fetch_live_score()
            self.title = f"{match_status} - {score_text}"
            self.menu.clear()
        except Exception as e:
            print("Error fetching scores:", e)
            self.title = "Error fetching scores"

if __name__ == "__main__":
    LiveScoreApp().run()
