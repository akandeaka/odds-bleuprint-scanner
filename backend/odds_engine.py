def interpret_odds(odds, season_stage, league_type):
    if odds == 1.14:
        return "Under 1.5 HT → goals in 2nd half"
    elif odds == 1.19 and season_stage == "start":
        return "H/A win + Over 2.5 FT"
    elif odds in [1.22, 1.26, 1.28]:
        return "Straight win H/A"
    elif odds == 1.25:
        return "Trap odd → avoid"
    elif odds in [1.30, 1.36] and season_stage == "start":
        return "Straight win H/A"
    elif odds == 1.30:
        if league_type == "popular":
            return "1X + Under 3.5"
        elif league_type == "lower_league":
            return "Straight win H"
    elif 1.40 <= odds <= 1.44:
        return "1X + Under 4.5"
    elif odds in [1.50, 1.57]:
        return "Straight win H"
    elif odds == 1.53:
        return "X2 + Under 3.5 FT"
    elif odds in [1.57, 1.61]:
        return "Straight win H/A"
    elif odds in [1.72, 1.80]:
        return "Straight win H (big teams)"
    elif odds == 1.90:
        return "FTX, XHT, or 1X + Under 3.5 FT"
    elif odds in [2.00, 2.10]:
        return "Straight win H or 1X + Under 3.5"
    elif odds == 3.00:
        return "FTX, XHT, Under 3.5 FT, or DC + NG HT"
    elif odds in [3.25, 3.29]:
        return "FTX, XHT, Under 3.5 goals"
    elif odds == 3.39:
        return "BTTS or Over 2.5 FT"
    elif odds == 3.60 and season_stage == "start":
        return "Over 0.5 HT + Over 3.5 FT"
    else:
        return None
