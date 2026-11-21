def subsidy_separate(units, ration_card, member_above_80):
    if units <= 100:
        return "Subsidy"
    if 101 <= units <= 200 and ration_card:
        return "Partial subsidy"
    if units > 200 and member_above_80:
        return "Subsidy"
    return "No subsidy"

def subsidy_elif(units, ration_card, member_above_80):
    if units <= 100:
        return "Subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        return "No subsidy"
    elif units > 200 and member_above_80:
        return "Subsidy"
    else:
        return "No subsidy"
