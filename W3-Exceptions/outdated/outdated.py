from datetime import datetime

while True:
    user_input = input("Date: ").strip()

    try:
        date = datetime.strptime(user_input, "%m/%d/%Y")
    except ValueError:
        try:
            date = datetime.strptime(user_input, "%B %d, %Y")
        #Invalid input, ask again
        except ValueError:
            continue

    # Format date as YYYY-MM-DD
    formatted_date = date.strftime("%Y-%m-%d")
    print(formatted_date)
    break