import subprocess

def fill_contribution_chart(start_date, end_date):
    # Generate a list of dates between the start and end dates
    dates = [start_date + datetime.timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    
    # Iterate over the dates and create empty commits
    for date in dates:
        # Set the GIT_AUTHOR_DATE and GIT_COMMITTER_DATE environment variables
        env = {
            'GIT_AUTHOR_DATE': date.strftime('%Y-%m-%d 12:00:00'),
            'GIT_COMMITTER_DATE': date.strftime('%Y-%m-%d 12:00:00')
        }
        
        # Create an empty commit
        subprocess.call('path/to/git commit --allow-empty -m "Auto-commit" --quiet', env=env, shell=True)

# Usage example
import datetime

# Set the desired start and end dates
start_date = datetime.date(2023, 2, 5)
end_date = datetime.date(2023, 6, 25)

# Fill the contribution chart
fill_contribution_chart(start_date, end_date)
