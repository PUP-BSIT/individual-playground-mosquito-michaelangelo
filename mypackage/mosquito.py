from beautiful_date import D, M

def display_choices():
    print("Enter your choice")
    print("1. date, month, year format")
    print("2. month, date, year format")
    print("3. year, month, date format")
    print("4. Exit")

def date_function():
    date_now = D.today()
    next_day = D.tomorrow()
    last_day = D.yesterday()

    while True:
        display_choices()

        choice = input("Enter your choice: ")

        dmy_format_today = f"{date_now.day}/{date_now.month}/{date_now.year}"
        dmy_format_tomorrow = f"{next_day.day}/{next_day.month}/{next_day.year}"
        dmy_format_yesterday = f"{last_day.day}/{last_day.month}/{last_day.year}"

        mdy_format_today = f"{date_now.month}/{date_now.day}/{date_now.year}"
        mdy_format_tomorrow = f"{next_day.month}/{next_day.day}/{next_day.year}"
        mdy_format_yesterday = f"{last_day.month}/{last_day.day}/{last_day.year}"

        ymd_format_today = f"{date_now.year}/{date_now.month}/{date_now.day}"
        ymd_format_tomorrow = f"{next_day.year}/{next_day.month}/{next_day.day}"
        ymd_format_yesterday = f"{last_day.year}/{last_day.month}/{last_day.day}"
        
        if choice == "1":
            print("\n")
            dmy_choice = input("Choose if today, tomorrow, yesterday: ").lower()
            
            if dmy_choice == "today":
                print("\n")
                print(f"This is the date today: {dmy_format_today}\n")
            elif dmy_choice == "tomorrow":
                print("\n")
                print(f"This is the date tomorrow: {dmy_format_tomorrow}\n")
            elif dmy_choice == "yesterday":
                print("\n")
                print(f"This is the date yesterday: {dmy_format_yesterday}\n")
            else: 
                print("\n")
                print("Inavlid choice!!!!")

        elif choice == "2":
            print("\n")
            mdy_choice = input("Choose if today, tomorrow, yesterday: ").lower()

            if mdy_choice == "today":
                print("\n")
                print(f"This is the date today: {mdy_format_today}\n") 
            elif mdy_choice == "tomorrow":
                print("\n")
                print(f"This is the date tomorrow: {mdy_format_tomorrow}\n")
            elif mdy_choice == "yesterday":
                print("\n")
                print(f"This is the date yesterday: {mdy_format_yesterday}\n")
            else: 
                print("\n")
                print("Invalid choice!!!")

        elif choice == "3":
            print("\n")
            ymd_choice = input("Choose if today, tomorrow, yesterday: ").lower()

            if ymd_choice == "today":
                print("\n")
                print(f"This is the date today: {ymd_format_today}\n") 
            elif ymd_choice == "tomorrow":
                print("\n")
                print(f"This is the date tomorrow: {ymd_format_tomorrow}\n")
            elif ymd_choice == "yesterday":
                print("\n")
                print(f"This is the date yesterday: {ymd_format_yesterday}\n")
            else: 
                print("\n")
                print("Invalid choice!!!")

        elif choice == "4":
            print("Exiting....")
            break
        else:
            print("\n")
            print("Choice is invalid!!!\n")