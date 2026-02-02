def recommend_leave(burnout_score):
    if burnout_score > 0.7:
        return "Strongly recommend leave"
    elif burnout_score > 0.4:
        return "Suggest short break"
    return "No leave required"
