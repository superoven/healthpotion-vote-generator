import arrow
import argparse
import random


from datetime import date, timedelta, datetime

NUM_OPTIONS = 6

def get_all_discussion_days():
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

def get_next_discussion_day():
    today = arrow.now().date()
    check_time = today + timedelta(days=20)
    for dt in get_all_discussion_days():
        if dt > check_time:
            return dt

def select_sample():
    inp_file = open("full_choice_list.txt", "r")
    lines = ['\n'.join(line.strip().rsplit(' ', 1)) for line in inp_file.readlines() if line]
    subset = random.sample(lines, NUM_OPTIONS)
    return subset

def print_command(args):
    hard_coded = False
    if hard_coded:
        inp_file = open("input.txt", "r")
        lines = [f"{line.strip()}" for line in inp_file.readlines() if len(line.strip()) > 0]
    else:
        lines = select_sample()

    # Randomize results
    random.shuffle(lines)
    concat_str = ", ".join(lines)

    disc_day = arrow.get(get_next_discussion_day())

    vote_title = f"Vote for the game to discuss on {disc_day.format('MMMM Do')}!"
    converted_date_str = disc_day.format("MM_YY") #"10_21" 
    # TODO: Make sure that the user has to provide an end date
    curr_datetime = arrow.now().datetime
    d = curr_datetime.date()

    # Day "3" is Thursday
    d += timedelta(days = (3 - d.weekday()) % 7)
    next_discussion_datetime_str = arrow.get(d).format("MM/DD/YYYY")

    # Calculate number of votes available depending on how big the list
    num_votes = int(len(lines) // 2.5)

    print(f"@everyone Let's vote on the game to discuss on {disc_day.format('MMMM DD')}!\n")
    print("You can vote on as many as you like, and the vote closes next Friday evening.\n")
    for i, line in enumerate(lines):
       print(f"{i + 1} - {line}")
    print(f"\nLooking forward to discussing {args.game_name} with you all on Thursday ({next_discussion_datetime_str} 7PM PST)!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some game name.')
    parser.add_argument('game_name', type=str, help='name of the game')
    args = parser.parse_args()
    print_command(args)
