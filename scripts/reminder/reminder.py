#!/usr/bin/env python3
import argparse
import json
import os
import re
import datetime
from datetime import timedelta

# Define the JSON file path
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# Define state to days mapping
STATE_TO_DAYS = {
    0: 2,
    1: 4,
    2: 9,
    3: 21,
    4: 38,
    5: float('inf')  # No need to review again
}

def load_data():
    """Load the data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"questions": {}}
    return {"questions": {}}

def save_data(data):
    """Save the data to the JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def parse_question_name(name):
    """Parse the question name to extract the number."""
    match = re.search(r'(\d+)', name)
    if match:
        return match.group(1)
    return None

def push_questions(args):
    """Add questions to the review list."""
    data = load_data()
    
    for question_name in args.questions:
        question_id = parse_question_name(question_name)
        if not question_id:
            print(f"Invalid question format: {question_name}")
            continue
        
        # Default state is 0 (least familiar)
        if question_id not in data["questions"]:
            today = datetime.date.today()
            # Set review day to 2 days from today for new questions
            next_review = today + timedelta(days=2)
            data["questions"][question_id] = {
                "name": question_name,
                "state": 0,
                "reviewDay": next_review.strftime("%Y-%m-%d")
            }
            print(f"Added: {question_name}, first review: {next_review.strftime('%Y-%m-%d')}")
        else:
            print(f"Question already exists: {question_name}")
    
    save_data(data)

def pull_questions(args):
    """Find questions that need to be reviewed."""
    data = load_data()
    today = datetime.date.today()
    
    needs_review = []
    for question_id, question_data in data["questions"].items():
        review_date = datetime.datetime.strptime(question_data["reviewDay"], "%Y-%m-%d").date()
        if review_date <= today:
            needs_review.append((question_data["name"], question_data["state"]))
    
    if not needs_review:
        print("No questions need review today.")
        return
    
    # Sort by name
    needs_review.sort()
    
    # Print formatted output
    for name, state in needs_review:
        print(f"{name:<30} state: {state}")

def mark_done(args):
    """Mark questions as reviewed and update their next review date."""
    data = load_data()
    today = datetime.date.today()
    
    for question_name in args.questions:
        question_id = parse_question_name(question_name)
        if not question_id or question_id not in data["questions"]:
            print(f"Question not found: {question_name}")
            continue
        
        question = data["questions"][question_id]
        state = question["state"]
        
        # Calculate next review date
        if state < 5:
            days = STATE_TO_DAYS[state]
            next_review = today + timedelta(days=days)
            question["reviewDay"] = next_review.strftime("%Y-%m-%d")
            print(f"Updated: {question_name}, next review: {next_review.strftime('%Y-%m-%d')}")
        else:
            print(f"No more reviews needed for: {question_name}")
    
    save_data(data)

def update_state(args):
    """Update the state of a question."""
    data = load_data()
    
    for question_name in args.questions:
        question_id = parse_question_name(question_name)
        if not question_id or question_id not in data["questions"]:
            print(f"Question not found: {question_name}")
            continue
        
        question = data["questions"][question_id]
        old_state = question["state"]
        new_state = args.state
        
        if old_state == new_state:
            print(f"State unchanged for: {question_name}")
            continue
        
        question["state"] = new_state
        print(f"Updated: {question_name}, state: {old_state} -> {new_state}")
    
    save_data(data)

def main():
    parser = argparse.ArgumentParser(description='Question Review Planner')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # push command
    push_parser = subparsers.add_parser('push', help='Add questions to review list')
    push_parser.add_argument('questions', nargs='+', help='Question names (e.g., 123.twoSum.py)')
    push_parser.set_defaults(func=push_questions)
    
    # pull command
    pull_parser = subparsers.add_parser('pull', help='Find questions to review today')
    pull_parser.set_defaults(func=pull_questions)
    
    # done command
    done_parser = subparsers.add_parser('done', help='Mark questions as reviewed')
    done_parser.add_argument('questions', nargs='+', help='Question names (e.g., 123.twoSum.py)')
    done_parser.set_defaults(func=mark_done)
    
    # state command (additional utility)
    state_parser = subparsers.add_parser('state', help='Update question state')
    state_parser.add_argument('state', type=int, choices=range(6), help='New state (0-5)')
    state_parser.add_argument('questions', nargs='+', help='Question names (e.g., 123.twoSum.py)')
    state_parser.set_defaults(func=update_state)
    
    args = parser.parse_args()
    
    if not hasattr(args, 'func'):
        parser.print_help()
        return
    
    args.func(args)

if __name__ == '__main__':
    main()
