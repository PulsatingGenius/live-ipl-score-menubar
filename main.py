import requests
from bs4 import BeautifulSoup
import rumps

def get_live_scores():
   
    url = "https://www.cricbuzz.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    score_elements = soup.find_all("div", class_="cb-ovr-flo")

    team1 = score_elements[1].text.strip()  
    score1 = score_elements[2].text.strip() 
    team2 = score_elements[3].text.strip()  
    score2 = score_elements[4].text.strip()  
    match_status = score_elements[5].text.strip() 

    return team1, score1, team2, score2, match_status

class LiveCricketScoresApp(rumps.App):
    def __init__(self):
        super(LiveCricketScoresApp, self).__init__("Live Cricket Scores")
        self.menu = ["Refresh", rumps.separator]
        self.refresh_scores()  
        rumps.timer(30)(self.refresh_scores)  

    @rumps.clicked("Refresh")
    def refresh_scores(self, _=None):
        team1, score1, team2, score2, match_status = get_live_scores()
        self.title = f"{team1}: {score1} vs {team2}: {score2} ({match_status})"

if __name__ == '__main__':
    LiveCricketScoresApp().run()
