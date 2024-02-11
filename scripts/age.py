from datetime import datetime
import pytz

def calculate_age_progress(dob, current_time):
    total_seconds_in_100_years = 100 * 365.25 * 24 * 60 * 60
    age_seconds = (current_time - dob).total_seconds()
    progress_percent = min(age_seconds / total_seconds_in_100_years * 100, 100)
    return progress_percent

def print_age_progress(progress_percent):
    progress_hashes = '#' * int(progress_percent // 10)
    remaining_hashes = '-' * (10 - len(progress_hashes))
    print(f'''[{progress_hashes}{remaining_hashes}] you've aged {progress_percent:.2f} yrs''')

if __name__ == "__main__":
    # Date of Birth in Asia/Kolkata timezone
    dob = datetime(2002, 9, 26, tzinfo=pytz.timezone('Asia/Kolkata'))

    # Current date and time in Asia/Kolkata timezone
    now_ist = datetime.now(pytz.timezone('Asia/Kolkata'))

    # Calculate age progress
    progress_percent = calculate_age_progress(dob, now_ist)

    # Print age progress
    print_age_progress(progress_percent)

