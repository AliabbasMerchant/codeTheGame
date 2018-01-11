import csv


class Player(object):
    players_list = []

    def __init__(self):
        with open('players_list.csv', 'r') as f:
            reader = csv.reader(f)
            self.players_list = list(reader)

    def return_dict(self, name_team_role):
        # name_team_role = resolve_name_team_role(name)
        player = {
            "name": name_team_role[0],  # str
            "team": name_team_role[1],  # str
            "role": name_team_role[2],  # str
            "matches": 0,
            "runs": 0,
            "fours": 0,
            "sixes": 0,
            "fifties": 0,
            "hundreds": 0,
            "wickets": 0,
            "four_w": 0,
            "five_w": 0,
            "maidens": 0,
            "field": 0,
            "balls_bowled": 0,
            "balls_batted": 0,
            "runs_conceded": 0,
            "duck": 0,
            "extras": 0,
            "points": 0.0,
            "economy": 0.0,  #dont add
            "strike": 0.0,  #dont add
            "average_runs": 0.0,  #dont add
            "average_wickets": 0.0,  #dont add
            "average_field": 0.0,  #dont add
        }
        return player

    # def resolve_name_team_role(self, name, team):
    #     name_team_role = [name, team, "undefined"]
    #     start = -1000
    #     end = 1000
    #     row_num = 0
    #     flag = 0
    #     for p in self.players_list:
    #         if p[0].strip().lower() == team.strip().lower():
    #             if start == -1000:
    #                 start = row_num
    #             end = row_num
    #             if p[2].strip().lower() == name.strip().lower():
    #                 name_team_role[0] = p[2]
    #                 name_team_role[1] = p[0]
    #                 name_team_role[2] = p[1]
    #                 flag = 1
    #                 break
    #         row_num += 1
    #     if flag == 0:
    #         for p in self.players_list[start: end+1]:
    #             if p[0].strip().lower() == team.strip().lower():
    #                 if p[3].strip().lower() == name.strip().lower():
    #                     name_team_role[0] = p[2]
    #                     name_team_role[1] = p[0]
    #                     name_team_role[2] = p[1]
    #                     flag = 1
    #                     break
    #                 if p[4].strip().lower() == name.strip().lower():
    #                     name_team_role[0] = p[2]
    #                     name_team_role[1] = p[0]
    #                     name_team_role[2] = p[1]
    #                     flag = 1
    #                     break
    #             row_num += 1
    #     return name_team_role

    def resolve_name_team_role(self, name, team):
        name_team_role = [name, team, "undefined"]
        for p in self.players_list:
            if p[0].strip().lower() == team.strip().lower():
                if p[2].strip().lower() == name.strip().lower():
                    name_team_role[0] = p[2]
                    name_team_role[1] = p[0]
                    name_team_role[2] = p[1]
                    return name_team_role
        for p in self.players_list:
            if p[0].strip().lower() == team.strip().lower():
                if p[3].strip().lower() == name.strip().lower():
                    name_team_role[0] = p[2]
                    name_team_role[1] = p[0]
                    name_team_role[2] = p[1]
                    return name_team_role
                if p[4].strip().lower() == name.strip().lower():
                    name_team_role[0] = p[2]
                    name_team_role[1] = p[0]
                    name_team_role[2] = p[1]
                    return name_team_role
        return name_team_role
