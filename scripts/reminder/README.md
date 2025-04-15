# Question Review Planner

A CLI tool to help you plan and track your algorithm problem review schedule.

## Installation

### Dependencies

This script works best with the `python-dotenv` library installed:

```bash
pip install python-dotenv
```

If the library is not installed, the script will fall back to a built-in .env parser with a recommendation to install the library.

## Usage

The script supports the following commands:

### 1. Push Questions

Add questions to your review list:

```bash
./reminder.py push 123.twoSum.py 456.reverseLinkedList.py
```

This will add the specified questions to your review list with an initial state of 0.

### 2. Pull Questions for Review

Find all questions that should be reviewed today:

```bash
./reminder.py pull
```

This will display a list of questions due for review, including their current state.

### 3. Mark Questions as Done

Mark questions as reviewed and update their next review date:

```bash
./reminder.py done 123.twoSum.py
```

The next review date will be calculated based on the question's current state:
- State 0: Review after 2 days
- State 1: Review after 4 days
- State 2: Review after 9 days
- State 3: Review after 21 days
- State 4: Review after 38 days
- State 5: No more reviews needed

### 4. Update Question State

Update the familiarity state of questions:

```bash
./reminder.py state 2 123.twoSum.py 456.reverseLinkedList.py
```

This updates the specified questions to state 2.

## States

The states represent your familiarity with the question:
- 0: Least familiar (review every 2 days)
- 1: Somewhat familiar (review every 4 days)
- 2: Moderately familiar (review every 9 days)
- 3: Quite familiar (review every 21 days)
- 4: Very familiar (review every 38 days)
- 5: Completely mastered (no more reviews needed)

## Data Storage

All question data is stored in a JSON file. The location of this file can be configured in three ways:

1. **Default path**: `C:\Users\Boris\Documents\10_MyGithub\ts-algo-prac\scripts\reminder\data.json`

2. **Using .env file**: Create or edit the `.env` file in the same directory as the script:
   ```
   DATA_FILE=C:\path\to\your\data.json
   ```
   
   The script uses the `python-dotenv` library to parse the .env file (if installed), which provides better handling of various .env formats.

3. **Command line argument**:
   ```bash
   ./reminder.py --data-file C:\path\to\your\data.json push 123.twoSum.py
   ```

Priority order: Command line argument > .env file > Default path

## Soft Links

When using soft links to run the script from different locations, the data file path will be correctly loaded from the `.env` file rather than trying to determine it based on the script location. 