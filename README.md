# The-Blue-Alliance-API-Example
A very simple Python example of getting data from The Blue Alliance

`example.py` is a barebones Python script that provides a method for accessing [The Blue Alliance's API][tba-api-docs].

*Remember*: Change the X-TBA-App-Id header to match your team and your purpose. It has to follow the format `<team/person id>:<app description>:<version>`.

This code can get the team number and name of the teams in the PNW 2016, ranked in order:

```python
rankings = apiRequest("district/pnw/2016/rankings")

for team in rankings:
	# gets the team key and extracts the team number
	teamNumber = team["team_key"][3:]
	
	# looks up the team nickname in the BlueAlliance API
	teamName = getTeamName(teamNumber)
	
	# pads teamNumber so that it is 4 digits long
	while(len(teamNumber) < 4):
		teamNumber = " " + teamNumber
	
	print(teamNumber + " | " + teamName)
```

[tba-api-docs]: https://www.thebluealliance.com/apidocs