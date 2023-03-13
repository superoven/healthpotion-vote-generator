import arrow
import random

from datetime import date, timedelta, datetime
from googlesearch import search

# import datetime
# import pytz

# utc=pytz.UTC

NUM_OPTIONS = 5

def get_steam_url(name_str):
    # domains = ["store.steampowered.com", "itch.io"]
    # for i in search(f"{name_str} game", tld="steampowered.com"):
    # for domain in domains:
    # TODO: Do this in parallel
    for i in search(f"{name_str} game steam -steamunlocked"):
        return i
    return ""

def get_all_discussion_days():
    # TODO: choose the next year if current month is December
    target_year = arrow.now().year + 1 if arrow.now().month == 12 else arrow.now().year
    curr_datetime = datetime(target_year, 1, 1)
    year = curr_datetime.year
    weekday = curr_datetime.weekday()
    d = curr_datetime.date()

    # Day "3" is Thursday
    d += timedelta(days = (3 - weekday) % 7)
    ret = []
    curr_count = 0
    curr_month = d.month
    while d.year == year:
        if d.month == curr_month:
            curr_count += 1
        d += timedelta(days = 7)
        if curr_count == 2:
            ret.append(d)
            curr_count = 0
            curr_month += 1
    return ret

# TODO: Use this and fix this lol
def get_next_discussion_day():
    today = arrow.now().date()
    check_time = today + timedelta(days=20)
    for dt in get_all_discussion_days():
        if dt > check_time:
            return dt

def select_sample():
    inp_file = open("full_choice_list.txt", "r")
    lines = [f"{line.strip()}" for line in inp_file.readlines() if line]
    subset = random.sample(lines, NUM_OPTIONS)
    # for line in subset:
    #     print(line)
    return subset

def print_command():
    hard_coded = False
    if hard_coded:
        inp_file = open("input.txt", "r")
        lines = [f"{line.strip()}" for line in inp_file.readlines() if len(line.strip()) > 0]
    else:
        lines = select_sample()

    # Don't use
    # TODO: Do this in parallel
    # lines = [f"{line.strip().title()} <{get_steam_url(line)}>" for line in inp_file.readlines() if len(line.strip()) > 0]

    # Randomize results
    random.shuffle(lines)
    concat_str = ", ".join(lines)

    disc_day = arrow.get(get_next_discussion_day())

    vote_title = f"Vote for the game to discuss on {disc_day.format('MMMM Do')}!"
    converted_date_str = disc_day.format("MM_YY") #"10_21" 
    # TODO: Make sure that the user has to provide an end date
    curr_datetime = arrow.now().datetime
    d = curr_datetime.date()

    # Day "4" is Friday
    # d += timedelta(days = (4 - d.weekday()) % 7)
    # expire_datetime_str = arrow.get(d).format("DD.MM.YYYY")

    # Day "3" is Thursday
    d += timedelta(days = (3 - d.weekday()) % 7)
    next_discussion_datetime_str = arrow.get(d).format("MM/DD/YYYY")

    # Calculate number of votes available depending on how big the list
    num_votes = int(len(lines) // 2.5)

    #cmd_str = f'pm!cmd -q "{vote_title}" -l "{converted_date_str}" -a -o "{concat_str}" -mc "{num_votes}" -h -d "{expire_datetime_str} 5pm PST"'
    print(f"@everyone Let's vote on the game to discuss on {disc_day.format('MMMM DD')}!\n")
    print("You have two votes to use, and the vote closes this Friday evening.\n")
    for i, line in enumerate(lines):
       print(f"{i + 1} - {line}")
    previous_game = "Half-Life 2"
    print(f"\nLooking forward to discussing {previous_game} with you all on Thursday ({next_discussion_datetime_str} 7PM PST)!")
    # print(cmd_str)

if __name__ == "__main__":
    # TODO: Argparse the expiry date_string
    # print(get_all_discussion_days())
    # print(get_next_discussion_day())
    # select_sample()
    print_command()
    # print("----\nRemember to save to input.txt with hardcoded and to set the expire_datetime_str properly!")
    # print(" - Check whether or not the date for the vote is also correct")
