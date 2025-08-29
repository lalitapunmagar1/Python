def convert_to_24_hour(time_str):
    """Converts time from 12-hour format (e.g., '2 PM') to 24-hour format."""
    time_str = time_str.strip().upper()
    if "AM" in time_str or "PM" in time_str:
        time, period = time_str.split()
        time = int(time)
        if period == "PM" and time != 12:
            time += 12
        if period == "AM" and time == 12:
            time = 0
    else:
        time = int(time_str)
    return time
def simple_decision_making(time, is_weekday, is_sunny):
    if 6 <= time < 8 and is_weekday == "yes":
        return "Time to go to work."
   
    if 12 <= time <= 13:
        return "Time for lunch."
    
    if 21 <= time <=22:
        return "Time to go to bed."
    
    if is_weekday == "no" and is_sunny == "yes":
        return "Go for a walk."
  
    return "No specific action for this time."
def main():
    try:
        time_str = input("Enter the current time:")
        time = convert_to_24_hour(time_str)
        if time < 0 or time > 23:
            raise ValueError("Time must be between 0 and 23.")
        is_weekday = input("Is it a weekday? (yes/no): ")
        is_sunny = input("Is the weather sunny? (yes/no): ")
        if is_weekday not in ['yes', 'no'] or is_sunny not in ['yes', 'no']:
            raise ValueError("Input for 'is_weekday' and 'is_sunny' must be 'yes' or 'no'.")
        decision = simple_decision_making(time, is_weekday, is_sunny)
        print(decision)
    except ValueError as e:
        print(f"Error: {e}")
main()
