# Healthpotion Vote Generator

Simple script to automate making the votes for Healthpotion

## Setup

```bash
# Make a virtual environment for this repo
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Process

### On the Friday before a discussion
- Move the runner-up from the last vote into `backlog.txt`
- Remove all other choices from last vote from `full_choice_list.txt`
- Generate the vote post with:
```bash
python parse_healthpotion.py "<PREVIOUS_WINNER>"
```
- Try the post in a local discord post to yourself and touch it up if anything is not formatted correctly
- Post to the #voting-box
- Create a poll lasting a week with the names of all answers in order
- Add all results from the #game-suggestions for next time
