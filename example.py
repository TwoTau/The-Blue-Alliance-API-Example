from urllib import request
import json

BASE_URL = "https://www.thebluealliance.com/api/v2/"
HEADERS = {
    "X-TBA-App-Id": "frc2976:post-season-scouting:v01",
    "User-agent": "Mozilla/5.0"
}

def apiRequest(key):
    urlRequest = request.Request(BASE_URL + key, headers=HEADERS)
    response = request.urlopen(urlRequest)
    result = json.loads(response.read().decode("utf-8"))
    return result

def getTeamName(teamNumber):
    return apiRequest("team/frc" + str(teamNumber))["nickname"]

if __name__ == "__main__":
    # example to get the team number and name of the teams in PNW 2016, ranked
    rankings = apiRequest("district/pnw/2016/rankings")
    for team in rankings:
        teamNumber = team["team_key"][3:]
        teamName = getTeamName(teamNumber)
        while(len(teamNumber) < 4):
            teamNumber = " " + teamNumber
		
        print(teamNumber + " | " + teamName)