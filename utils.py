# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

def progress_bar(current, total):
    if total == 0:
        return "[⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡] 0%"
    percent = int((current / total) * 100)
    bar = "⬢" * (percent // 10) + "⬡" * (10 - percent // 10)
    return f"[{bar}] {percent}%"

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
