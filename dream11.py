import json

class dream11(object):
    batsmen = []
    bowlers = []
    all_rounders = []
    wicket_keepers = []
    bowl = 4
    bat = 4
    all = 2
    wicket = 1

    def read(self):
        self.data = json.load(open("consolidated_data.json"))
        for player in self.data:  # player is the key
            if self.data[player]["role"] == "BATSMAN":
                self.batsmen = self.merge(self.data[player] , self.batsmen, self.bat)
            if self.data[player]["role"] == "WICKET KEEPER":
                self.wicket_keepers = self.merge(self.data[player], self.wicket_keepers, self.wicket)
            if self.data[player]["role"] == "BOWLER":
                self.bowlers = self.merge(self.data[player] , self.bowlers, self.bowl)
            if self.data[player]["role"] == "ALL ROUNDER":
                self.all_rounders = self.merge(self.data[player], self.all_rounders, self.all)
        self.save_to_json()

    def merge(self, player, List, no):
        List.append(player)
        List.sort(key=lambda x: x["points"], reverse = True)
        return List[0:no]

    def save_to_json(self):
        team = self.join()
        with open("dream11.json", "w") as outfile:
            json.dump(team, outfile, sort_keys=True, indent=4)

    def join(self):
        team = {}
        self.bowlers.sort(key=lambda x: x["points"], reverse=True)
        self.bowlers = self.bowlers[0:self.bowl]
        self.batsmen.sort(key=lambda x: x["points"], reverse=True)
        self.batsmen = self.batsmen[0:self.bat]
        self.wicket_keepers.sort(key=lambda x: x["points"], reverse=True)
        self.wicket_keepers = self.wicket_keepers[0:self.wicket]
        self.all_rounders.sort(key=lambda x: x["points"], reverse=True)
        self.all_rounders = self.all_rounders[0:self.all]

        for player in self.bowlers:
            team[player["name"]] = player
        for player in self.batsmen:
            team[player["name"]] = player
        for player in self.wicket_keepers:
            team[player["name"]] = player
        for player in self.all_rounders:
            team[player["name"]] = player
        return team
