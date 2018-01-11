import json


class Consolidate(object):
    consolidate_data = {}

    def consolidate(self, list):
        for name in list:
            data = json.load(open(name))
            for player in data:  # player is the key
                print(data[player]["name"])
                if player in self.consolidate_data:
                    for key in data[player]:
                        if key in self.consolidate_data[player]:
                            try:
                                temp = float(self.consolidate_data[player][key])
                                temp2 = float(data[player][key])
                                self.consolidate_data[player][key] = (temp + temp2)
                            except Exception:
                                pass
                        else:
                            self.consolidate_data[player][key] = data[player][key]
                else:
                    self.consolidate_data[player] = data[player]

                try:
                    if self.consolidate_data[player]["balls_bowled"] > 0:
                        self.consolidate_data[player]["economy"] = 6 * (self.consolidate_data[player]["runs_conceded"] / self.consolidate_data[player]["balls_bowled"])
                except Exception:
                    pass
                try:
                    if self.consolidate_data[player]["balls_batted"] >= 10:
                        self.consolidate_data[player]["strike"] = (self.consolidate_data[player]["runs"] / self.consolidate_data[player]["balls_batted"]) * 100
                    else:
                        self.consolidate_data[player]["strike"] = 0.0
                except Exception:
                    pass
                try:
                    self.consolidate_data[player]["average_wickets"] = self.consolidate_data[player]["wickets"] / self.consolidate_data[player]["matches"]
                except Exception:
                    pass
                try:
                    self.consolidate_data[player]["average_field"] = self.consolidate_data[player]["field"] / self.consolidate_data[player]["matches"]
                except Exception:
                    pass
                try:
                    self.consolidate_data[player]["average_runs"] = self.consolidate_data[player]["runs"] / self.consolidate_data[player]["matches"]
                except Exception:
                    pass
                print(self.consolidate_data[player]["points"])

    def save_to_json(self):
        with open("consolidated_data.json", "w") as outfile:
            json.dump(self.consolidate_data, outfile, sort_keys=True, indent=4)