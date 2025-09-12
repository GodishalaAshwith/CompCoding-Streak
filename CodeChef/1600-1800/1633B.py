for _ in range(int(input())):
    teams_goals = {}
    team_points = {}
    for _ in range(12):
        match_info = input().split()
        team_home = match_info[0]
        goals_home = int(match_info[1])
        goals_away = int(match_info[3])
        team_away = match_info[4]

        # Updating home team stats
        if team_home in teams_goals:
            teams_goals[team_home] += (goals_home - goals_away)
        else:
            teams_goals[team_home] = goals_home - goals_away

        if team_home in team_points:
            if goals_home > goals_away:
                team_points[team_home] += 3
            elif goals_home == goals_away:
                team_points[team_home] += 1
        else:
            if goals_home > goals_away:
                team_points[team_home] = 3
            elif goals_home == goals_away:
                team_points[team_home] = 1
            else:
                team_points[team_home] = 0

        # Updating away team stats
        if team_away in teams_goals:
            teams_goals[team_away] += (goals_away - goals_home)
        else:
            teams_goals[team_away] = goals_away - goals_home

        if team_away in team_points:
            if goals_away > goals_home:
                team_points[team_away] += 3
            elif goals_home == goals_away:
                team_points[team_away] += 1
        else:
            if goals_away > goals_home:
                team_points[team_away] = 3
            elif goals_home == goals_away:
                team_points[team_away] = 1
            else:
                team_points[team_away] = 0

    for _ in range(2):
        first_winner = max(team_points, key=lambda team: (team_points[team], teams_goals[team]))
        print(first_winner, end=' ')
        del team_points[first_winner]
    print()