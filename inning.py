import Player
import json
import csv
import re


class Inning(object):

    def __init__(self):
        self.data = {}
        self.name_of_file = ""

    def read_csv(self, file):
        ifile = open(file)
        self.csv = csv.reader(ifile)
        print("read csv")

    def allot_data(self):
        prev_bowler = ""
        dot_balls = 0
        row_num = 0
        for ball in self.csv:
            if row_num == 0:
                self.name_of_file = re.sub('\W+', ' ', ball[0] + " " + ball[1] + " " + ball[2]).strip()
                self.team_bat = ball[0].strip()
                self.team_bowl = ball[2].strip()
            elif row_num == 1:
                pass
            else:
                # ball_no= ball[0]
                outcome = re.sub('\W+', '', ball[1]).strip()
                bowler_name = re.sub('\W+', ' ', ball[3]).strip()
                batsman_name = re.sub('\W+', ' ', ball[4]).strip()
                fielder_name = ""
                try:
                    if ball[5]:
                        fielder_name = re.sub('\W+', ' ', ball[5]).strip()
                    else:
                        fielder_name = ""
                except Exception:
                    pass
                extra = False
                runs = 0
                wicket = False
                if outcome[0].isdigit():
                    runs = int(outcome[0])
                else:
                    wicket = True
                if len(outcome) > 1:
                    if outcome[1].isalpha():  # not needed
                        extra = True
                if wicket:
                    runs = 0  # not needed
                if extra:
                    runs = runs - 1

                if bowler_name:
                    player = Player.Player()
                    name_team_role = player.resolve_name_team_role(bowler_name, self.team_bowl)
                    if not name_team_role[0] in self.data:
                        self.data[name_team_role[0]] = player.return_dict(name_team_role)
                    self.data[name_team_role[0]]["matches"] = 1
                    self.data[name_team_role[0]]["balls_bowled"] += 1
                    self.data[name_team_role[0]]["runs_conceded"] += runs
                    if extra:
                        self.data[name_team_role[0]]["extras"] += 1
                        self.data[name_team_role[0]]["runs_conceded"] += 1  # the run of the extra
                    if wicket:
                        self.data[name_team_role[0]]["wickets"] += 1
                    if runs == 0:
                        dot_balls += 1
                    else:
                        dot_balls = 0
                    if dot_balls > 1:
                        if bowler_name.strip().lower() == prev_bowler.strip().lower():
                            pass
                        else:
                            dot_balls = 1
                    if dot_balls == 6:
                        self.data[name_team_role[0]]["maidens"] += 1
                        dot_balls = 0
                    prev_bowler = bowler_name

                if batsman_name:
                    player = Player.Player()
                    name_team_role = player.resolve_name_team_role(batsman_name, self.team_bat)
                    if not name_team_role[0] in self.data:
                        self.data[name_team_role[0]] = player.return_dict(name_team_role)
                    self.data[name_team_role[0]]["matches"] = 1
                    self.data[name_team_role[0]]["runs"] += runs
                    self.data[name_team_role[0]]["balls_batted"] += 1
                    if runs == 4:
                        self.data[name_team_role[0]]["fours"] += 1
                    if runs == 6:
                        self.data[name_team_role[0]]["sixes"] += 1

                if fielder_name:
                    player = Player.Player()
                    name_team_role = player.resolve_name_team_role(batsman_name, self.team_bat)
                    if not name_team_role[0] in self.data:
                        self.data[name_team_role[0]] = player.return_dict(name_team_role)
                    self.data[name_team_role[0]]["matches"] = 1
                    self.data[name_team_role[0]]["field"] += 1
            row_num += 1

    def save_to_json(self):
        file_name = self.name_of_file + "_data.json"
        print(file_name)
        for p in self.data:
            print("    " + self.data[p]["name"] + "  " + self.data[p]["team"])
        with open(file_name, "w") as outfile:
            json.dump(self.data, outfile, sort_keys=True, indent=4)
        self.data = {}
        return file_name

    def calculate_scores(self):
        run_score = 0.5
        four_score = 0.5
        six_score = 1
        fifty_score = 4
        hundred_score = 6
        duck_score = -2  # except bowler
        played_score = 2
        w_score = 10  # not excluding run out
        four_w_score = 4
        five_w_score = 8
        maiden_score = 4
        field_score = 5
        extras_score = -1

        economy_0_4 = 3
        economy_4_5 = 2
        economy_5_6 = 1
        economy_9_10 = -1
        economy_10_11 = -2
        economy_11_above = -3
        strike_60_70 = -1  # min 10 balls except bowlers
        strike_50_60 = -2  # min 10 balls except bowlers
        strike_0_50 = -3  # min 10 balls except bowlers

        points = 0
        for player in self.data:
            if float(self.data[player]["runs"]) == 0 and self.data[player]["team"] == self.team_bat:
                self.data[player]["duck"] = 1
            if float(self.data[player]["runs"]) >= 100.0:
                self.data[player]["hundreds"] = 1
            elif float(self.data[player]["runs"]) >= 50.0:
                self.data[player]["fifties"] = 1

            if self.data[player]["wickets"] >= 5:
                self.data[player]["five_w"] = 1
            if self.data[player]["wickets"] == 4:
                self.data[player]["four_w"] = 1
            if self.data[player]["balls_bowled"] > 0:
                self.data[player]["economy"] = 6 * (
                        self.data[player]["runs_conceded"] / self.data[player]["balls_bowled"])
            if self.data[player]["balls_batted"] >= 10:
                self.data[player]["strike"] = (self.data[player]["runs"] / self.data[player]["balls_batted"]) * 100
            else:
                self.data[player]["strike"] = 0.0

            points = float(self.data[player]["runs"]) * run_score
            points += float(self.data[player]["fours"]) * four_score
            points += float(self.data[player]["sixes"]) * six_score
            points += float(self.data[player]["fifties"]) * fifty_score
            points += float(self.data[player]["hundreds"]) * hundred_score
            points += played_score
            points += float(self.data[player]["wickets"]) * w_score
            points += float(self.data[player]["four_w"]) * four_w_score
            points += float(self.data[player]["five_w"]) * five_w_score
            points += float(self.data[player]["maidens"]) * maiden_score
            points += float(self.data[player]["extras"]) * extras_score
            points += float(self.data[player]["field"]) * field_score

            if self.data[player]["team"] == self.team_bowl:
                if float(self.data[player]["economy"]) < 4.0:
                    points += economy_0_4
                elif float(self.data[player]["economy"]) < 5.0:
                    points += economy_4_5
                elif float(self.data[player]["economy"]) < 6.0:
                    points += economy_5_6
                if self.data[player]["role"].strip().lower() == "BOWLER".strip().lower() or self.data[player][
                    "role"].strip().lower() == "ALL ROUNDER".strip().lower():
                    if float(self.data[player]["economy"]) >= 11.0:
                        points += economy_11_above
                    elif float(self.data[player]["economy"]) >= 10.0:
                        points += economy_10_11
                    elif float(self.data[player]["economy"]) >= 9.0:
                        points += economy_9_10

            if self.data[player]["role"].strip().lower() != "BOWLER".strip().lower():
                if self.data[player]["balls_batted"] >= 10:
                    if float(self.data[player]["strike"]) < 50:
                        points += strike_0_50
                    elif float(self.data[player]["strike"]) < 60:
                        points += strike_50_60
                    elif float(self.data[player]["strike"]) < 70:
                        points += strike_60_70
                points += float(self.data[player]["duck"]) * duck_score

            self.data[player]["points"] = points
