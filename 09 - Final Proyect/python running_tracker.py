# Running Tracker App
import math

def print_welcome():
    print("Welcome to the Running Tracker App!")
    print("You can enter your run data and view your progress over time.")
    print("Type 'exit' at any time to stop the program.\n")

def get_run_input():
    date = input("Enter the date of the run (YYYY-MM-DD): ")
    if date.lower() == 'exit':
        return None
    distance = input("Enter the distance run (in km): ")
    if distance.lower() == 'exit':
        return None
    time = input("Enter the time of the run (in minutes): ")
    if time.lower() == 'exit':
        return None
    
    try:
        return {
            'date': date,
            'distance': float(distance),
            'time': float(time)
        }
    except ValueError:
        print("Invalid input. Please enter numerical values for distance and time.")
        return None

def format_pace(pace):
    minutes = int(pace)
    seconds = int(round((pace - minutes) * 60))
    return f"{minutes}:{seconds:02d}"

def print_all_runs(run_data):
    if not run_data:
        print("No runs recorded yet.\n")
        return

    print("\nYour Runs:")
    print("{:<12} {:<10} {:<10} {:<10}".format("Date", "Distance", "Time", "Pace"))
    print("-" * 44)
    total_distance = 0
    total_time = 0

    for run in run_data:
        pace = run['time'] / run['distance'] if run['distance'] != 0 else 0
        formatted_pace = format_pace(pace)
        print("{:<12} {:<10.2f} {:<10.2f} {:<10}".format(run['date'], run['distance'], run['time'], formatted_pace))
        total_distance += run['distance']
        total_time += run['time']

    avg_pace = total_time / total_distance if total_distance != 0 else 0
    formatted_avg_pace = format_pace(avg_pace)
    print("\nTotal Distance: {:.2f} km".format(total_distance))
    print("Total Time: {:.2f} minutes".format(total_time))
    print("Average Pace: {} min/km\n".format(formatted_avg_pace))

def main():
    run_data = []
    print_welcome()

    while True:
        print("Choose an option:")
        print("1. Enter a new run")
        print("2. View run summary")
        print("3. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            run = get_run_input()
            if run:
                run_data.append(run)
        elif choice == '2':
            print_all_runs(run_data)
        elif choice == '3' or choice.lower() == 'exit':
            print("Thanks for using the Running Tracker App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == '__main__':
    main()
