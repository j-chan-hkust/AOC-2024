import requests
import time
import pyperclip
import webbrowser
from bs4 import BeautifulSoup
from datetime import datetime
import os
import pytz

# Configuration
AOC_YEAR = 2024
BASE_URL = "https://adventofcode.com"
KAGI_ASSISTANT_URL = "https://kagi.com/assistant"
BOILERPLATE_PATH = "boilerplate.py"
CHECK_INTERVAL = 1  # Check every second
MINIMUM_PROMPT_LENGTH = 100

def get_advent_prompt(day):
    """Fetch the prompt for a specific day."""
    url = f"{BASE_URL}/{AOC_YEAR}/day/{day}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('article', class_='day-desc')
            if articles:
                return '\n\n'.join(article.get_text().strip() for article in articles)
        return None
    except Exception as e:
        print(f"Error fetching prompt: {e}")
        return None

def read_boilerplate():
    """Read the boilerplate code from file."""
    try:
        if os.path.exists(BOILERPLATE_PATH):
            with open(BOILERPLATE_PATH, 'r') as file:
                return file.read()
        print(f"Warning: Boilerplate file not found at {BOILERPLATE_PATH}")
        return ""
    except Exception as e:
        print(f"Error reading boilerplate: {e}")
        return ""

def combine_prompt_and_boilerplate(day, prompt, boilerplate):
    """Combine prompt and boilerplate into final format."""
    return f"""Here's a competitive programming problem. Provide only the solution code with minimal comments. No explanations needed.

Problem (AoC {AOC_YEAR} Day {day}):
{prompt}

Template:
{boilerplate}

Provide only the solution code."""

def is_valid_prompt(prompt):
    """Validate if the prompt seems legitimate."""
    return prompt and len(prompt) >= MINIMUM_PROMPT_LENGTH

def wait_until_midnight_est():
    """Wait until midnight EST."""
    est = pytz.timezone('US/Eastern')
    while True:
        now = datetime.now(est)
        if now.hour == 0 and now.minute == 0:
            return
        seconds_until_midnight = ((24 - now.hour - 1) * 3600 +
                                (60 - now.minute - 1) * 60 +
                                (60 - now.second))
        if seconds_until_midnight > 60:
            print(f"Waiting for midnight EST... ({seconds_until_midnight//3600}h {(seconds_until_midnight%3600)//60}m)")
            time.sleep(60)
        else:
            print(f"Almost midnight... ({seconds_until_midnight}s)")
            time.sleep(1)

def main():
    # Get day and year
    current_day = datetime.now().day
    day = input(f"Enter day number (press Enter for current day {current_day}): ").strip()
    day = int(day) if day else current_day

    global AOC_YEAR
    year = input(f"Enter year (press Enter for {AOC_YEAR}): ").strip()
    if year:
        AOC_YEAR = int(year)

    print(f"Starting prompt monitor for Year {AOC_YEAR} Day {day}...")
    print("Waiting for midnight EST...")

    wait_until_midnight_est()
    print("It's midnight! Starting rapid checks...")

    while True:
        prompt = get_advent_prompt(day)

        if is_valid_prompt(prompt):
            print("Found valid prompt!")
            boilerplate = read_boilerplate()
            final_text = combine_prompt_and_boilerplate(day, prompt, boilerplate)
            pyperclip.copy(final_text)
            print("Copied prompt to clipboard!")
            webbrowser.open(KAGI_ASSISTANT_URL)
            print("Opened Kagi Assistant!")
            break

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
