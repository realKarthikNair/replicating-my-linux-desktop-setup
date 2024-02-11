from datetime import datetime, timezone
import pytz

def get_year_progress():
    now_utc = datetime.now(timezone.utc)
    ist_timezone = pytz.timezone('Asia/Kolkata')
    now_ist = now_utc.astimezone(ist_timezone)
    year_start = datetime(now_ist.year, 1, 1, tzinfo=ist_timezone)
    year_end = datetime(now_ist.year + 1, 1, 1, tzinfo=ist_timezone)
    year_duration = year_end - year_start
    progress = (now_ist - year_start) / year_duration
    remaining = year_duration - (now_ist - year_start)

    progress_percent = round(progress * 100, 2)
    remaining_percent = round(remaining.total_seconds() / year_duration.total_seconds() * 100, 2)

    progress_hashes = '#' * (int(progress_percent) // 10)
    remaining_hashes = '-' * (10 - len(progress_hashes))
    print(f'''[{progress_hashes}{remaining_hashes}] {100-progress_percent:.2f}% of {now_ist.year} left''')

if __name__ == "__main__":
    get_year_progress()



