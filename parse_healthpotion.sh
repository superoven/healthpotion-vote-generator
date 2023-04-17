#!/bin/bash -eo pipefail

NUM_OPTIONS=5

if ! which shuf > /dev/null; then
  echo "The 'shuf' command is not installed. To install it:"
  if [ "$(uname)" == "Darwin" ]; then
    echo "  Install Homebrew (https://brew.sh/), then run:"
    echo "  brew install coreutils"
  elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    echo "  Run one of the following commands:"
    echo "  sudo apt-get install coreutils  # For Ubuntu and Debian-based systems"
    echo "  sudo yum install coreutils     # For CentOS and Red Hat-based systems"
    echo "  sudo pacman -S coreutils       # For Arch Linux"
  else
    echo "  Unsupported platform: $(uname)"
  fi
fi

# function get_all_discussion_days {
#     target_year=$(date +'%Y')
#     if [ $(date +'%m') -eq 12 ]; then
#         target_year=$((target_year + 1))
#     fi
#     curr_datetime=$(date -d "${target_year}-01-01")
#     echo "curr_datetime: ${curr_datetime}"
#     year=$(echo "${curr_datetime}" | cut -d'-' -f1)
#     weekday=$(echo "${curr_datetime}" | awk '{print strftime("%w", $0)}')
#     d=$(echo "${curr_datetime}" | cut -d' ' -f1)

#     d=$(date -d "${d} +$(( (3 - ${weekday}) % 7 )) days")
#     ret=()
#     curr_count=0
#     curr_month=$(date -d "${d}" +'%m')
#     while [ $(date -d "${d}" +'%Y') -eq "${year}" ]; do
#         if [ $(date -d "${d}" +'%m') -eq "${curr_month}" ]; then
#             curr_count=$((curr_count+1))
#         fi
#         d=$(date -d "${d} +7 days")
#         if [ "${curr_count}" -eq 2 ]; then
#             ret+=("${d}")
#             curr_count=0
#             curr_month=$((curr_month+1))
#         fi
#     done
#     printf '%s\n' "${ret[@]}"
# }

# function get_next_discussion_day {
#     today=$(date +'%Y-%m-%d')
#     check_time=$(date -d "${today} +20 days" +'%Y-%m-%d')
#     for dt in $(get_all_discussion_days); do
#         if [ "${dt}" \> "${check_time}" ]; then
#             echo "${dt}"
#             break
#         fi
#     done
# }

function select_sample {
    #echo "hello"
    lines=()
    while IFS= read -r line; do
        # lines+=("$line")
        lines+=("$(echo "${line}" | awk '{print substr($0, 0, length($0)-1)}')")
    done < "full_choice_list.txt"
    
    # subset=$(echo "${lines[@]}" | tr ' ' '\n' | shuf -n "${NUM_OPTIONS}" | tr '\n' ' ')
    subset=$(echo "${lines[@]}" | shuf -n "${NUM_OPTIONS}")
    printf '%s\n' "${subset}"
}

function print_command {
    echo "hello"
    lines=($(select_sample))
    echo "lines: ${lines[@]}"
    # disc_day=$(date -d "$(get_next_discussion_day)" +'%B %d')
    # curr_datetime=$(date +'%Y-%m-%d %H:%M:%S')
    # d=$(echo "${curr_datetime}" | cut -d' ' -f1)

    # d=$(date -d "${d} +$(( (3 - $(date -d "${d}" +'%w')) % 7 )) days")
    # next_discussion_datetime_str=$(date -d "${d}" +'%m/%d/%Y')

    # num_votes=$(( $(echo "${lines[@]}" | wc -w) / 2 + 1 ))

    # printf '@everyone Let'"'"'s vote on the game to discuss on %s!\n\n' "${disc_day}"
    # printf 'You have %s votes to use, and the vote closes this Friday evening.\n\n' "${num_votes}"
    # i=1
    # for line in "${lines[@]}"; do
    #     printf '%s - %s\n' "${i}" "${line}"
    #     i=$((i+1))
    # done
    # printf '\nLooking forward to discussing %s with you all on Thursday (%s 7PM PST)!\n' "${1}" "${next_discussion_datetime_str}"
}

print_command "${1}"
