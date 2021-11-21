import arrow
import random

from datetime import date, timedelta, datetime
from googlesearch import search

# import datetime
# import pytz

# utc=pytz.UTC


def get_steam_url(name_str):
    domains = ["store.steampowered.com", "itch.io"]
    # for i in search(f"{name_str} game", tld="steampowered.com"):
    for domain in domains:
        for i in search(f"{name_str} game download"):
            return i
    return ""

def get_all_discussion_days():
    curr_datetime = datetime(arrow.now().year, 1, 1)
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

def get_next_discussion_day():
    today = arrow.now().date()
    check_time = today + timedelta(days=3)
    for dt in get_all_discussion_days():
        if dt > check_time:
            return dt

def print_command():
    # TODO: Do this in parallel
    inp_file = open("example_input.txt", "r")
    lines = [f"{line.strip().title()} <{get_steam_url(line)}>" for line in inp_file.readlines() if len(line.strip()) > 0]

    print("--- Results: ---\n")
    for line in lines:
       print(f"{line}")

    # Randomize results
    random.shuffle(lines)
    concat_str = ", ".join(lines)

    disc_day = arrow.get(get_next_discussion_day())

    vote_title = f"Vote for the game to discuss on {disc_day.format('MMMM Do')}!"
    converted_date_str = disc_day.format("MM_YY")#"10_21" 
    # TODO: Make sure that the user has to provide an end date
    expire_datetime_str = "23.11.2021"
    cmd_str = f'pm!cmd -q "{vote_title}" -l "{converted_date_str}" -a -o "{concat_str}" -mc "3" -h -d "{expire_datetime_str} 5pm PST"'
    print()
    print(cmd_str)

if __name__ == "__main__":
    # print(get_all_discussion_days())
    print_command()
