import re

def detect_discord_emote():
    discord_text_example = "<a:Blune:797546918058131456> Hello, <How are you :> <a:Blune:7459367204>"
    match = re.findall(r"<\w?:\w+:\d+>", discord_text_example)

    return match

if __name__ == "__main__":
    print(detect_discord_emote())