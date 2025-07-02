import json
import os
import yfinance as yf
import matplotlib.pyplot as plt

# ========= COMPANIES =========
#  list of companies the user can choose:
STOCK_LIST = {
    "AAPL": "Apple Inc",
    "TSLA": "Tesla Motors",
    "GOOG": "Google LLC",
    "MSFT": "Microsoft Corp",
    "AMZN": "Amazon Inc", 
    "META": "Meta Platforms Inc.", 
    "NVDA": "NVIDIA Corporation", 
    "NFLX": "Netflix Inc.", 
    "BABA": "Alibaba Group", 
    "INTC": "Intel Corporation", 
    "ORCL": "Oracle Corporation", 
    "ADBE": "Adobe Inc.", 
    "PYPL": "PayPal Holdings Inc.", 
    "IBM": "International Business Machines", 
    "CSCO": "Cisco Systems Inc.", 
    "PEP": "PepsiCo Inc.", 
    "KO": "Coca-Cola Company", 
    "WMT": "Walmart Inc.", 
    "DIS": "The Walt Disney Company", 
    "UBER": "Uber Technologies Inc " 
}

# ========= LOGGING SYSTEM =========
# File to store user activity logs
REPORT_FILE = "report_user.json"

def load_logs():
    if not os.path.exists(REPORT_FILE):
        return {}
    with open(REPORT_FILE, "r") as f:
        return json.load(f)

def save_logs(logs):
    with open(REPORT_FILE, "w") as f:
        json.dump(logs, f, indent=4)

def log_action(username, action):
    logs = load_logs()
    if username not in logs:
        logs[username] = []
    logs[username].append(action)
    save_logs(logs)

def show_user_logs(username):
    logs = load_logs()
    history = logs.get(username, [])
    print(f"\nActivity Log for {username}:")
    if not history:
        print("No previous records.")
    else:
        for entry in history:
            print(f"-- {entry}")

# ========= USER SYSTEM =========

# Load user accounts from users.json file
def load_users():
    if not os.path.exists("users.json"):
        return {}
    # Read
    with open("users.json", "r") as file:
        return json.load(file)
# Write
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

def register():
    users = load_users()
    username = input("New username: ").strip()
    if username in users:
        print("Username already exists.")
        return
    password = input("New password: ").strip()
    users[username] = password
    save_users(users)
    print("User registered.")

def login():
    users = load_users()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if username in users and users[username] == password:
        print(f"Welcome, {username}")
        log_action(username, "Logged in")
        return username
    else:
        print("Wrong username or password.")
        return None

# ========= STOCK FUNCTIONS =========

def display_stock_data(symbol, date_from=None, date_to=None, username=None, company_name=None):
    print(f"Getting data for {symbol}...")
    try:
           
    #    if symbol.isnumeric():
    #
    #        print("Invalid stock symbol. It should not be a number.")
     
    
    #       return

        if date_from and date_to:
            from datetime import datetime
            try:
                start = datetime.strptime(date_from, "%Y-%m-%d")
                end = datetime.strptime(date_to, "%Y-%m-%d")
                if start > end:
                    print("Start date cannot be after end date.")
                    return
            except:
                print("Invalid date format. Use YYYY-MM-DD.")
                return

            data = yf.download(symbol, start=date_from, end=date_to)
        else:
            data = yf.download(symbol, period="5d")

        if data.empty:
            print("No data found.")
            return

        try:
            last_price = float(data["Close"].iloc[-1])
            high = float(data["High"].max())
            low = float(data["Low"].min())

            print(f"Last price: {last_price:.2f}")
            print(f"High: {high:.2f}, Low: {low:.2f}")

            if username:
                if date_from and date_to:
                    log_action(username, f"Searched {symbol} ({company_name}) from {date_from} to {date_to} — Last: {last_price:.2f}, High: {high:.2f}, Low: {low:.2f}")
                else:
                    log_action(username, f"Searched {symbol} ({company_name}) (5d) — Last: {last_price:.2f}, High: {high:.2f}, Low: {low:.2f}")

        except Exception as e:
            print("Error reading prices:", e)
            return

        print("Save this data?")
        print("1. Yes by default name)")
        print("2. Yes by you can chose file name.csv)")
        print("3. No")
        choice = input(">> ").strip()

        if choice == "1":
            if date_from and date_to:
                filename = f"{symbol}_{date_from}_to_{date_to}.csv"
            else:
                filename = f"{symbol}_last5days.csv"
            data.to_csv(filename)

            print(f"Saved to {filename}")

            if username:

                log_action(username, f"Saved data to {filename}")


        elif choice == "2":
            filename = input("Enter filename: ").strip()
            if not filename.endswith(".csv"):
                filename += ".csv"
            data.to_csv(filename)
            print(f"Saved to {filename}")
            if username:
                log_action(username, f"Saved data to {filename}")
        else:
            print("Not saved.")

        show = input("Show graph? (yes/no): ").strip().lower()
      #  Ask if user wants to see a graph
        if show == "yes":
         #   Plot the closing prices
            data["Close"].plot(title=f"{symbol} Closing Prices")
            plt.xlabel("Date")
            plt.ylabel("RS")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            if username:
                log_action(username, f"Viewed graph for {symbol}")

    except Exception as e:
        print("Error:", e)

# ========= MAIN MENU =========1

def stock_menu(username):
    while True:
        print("\nStock Menu:")
        print("1. Logout")
        print("2. View Activity Log")
        print("3. Choose from stock list")
        choice = input(">> ").strip()

        if choice == "1":
            print("Logged out.")
            log_action(username, "Logged out")
            break

        elif choice == "2":
            show_user_logs(username)

        elif choice == "3":
            print("\nChoose a company:")
            # index, Synbol company, name company 
            for idx, (symbol, name) in enumerate(STOCK_LIST.items(), start=1):

                print(f"{idx}. {symbol} - {name}")
            selected = input(">> ").strip()

            try:
                #convert for chose the user input number 
                selected = int(selected)
                symbol = list(STOCK_LIST.keys())[selected - 1]
                company_name = STOCK_LIST[symbol]
                print(f"Selected: {symbol} ({company_name})")
                use_dates = input("Use custom dates? (yes/no): ").strip().lower()
                if use_dates == "yes":
                    date_from = input("From date (YYYY-MM-DD): ")
                    date_to = input("To date (YYYY-MM-DD): ")

                    #print the user after input date
                    display_stock_data(symbol, date_from, date_to, username, company_name)
                else:
                    display_stock_data(symbol, username=username, company_name=company_name)
            except:
                print("Invalid selection.")

        else:
            print("Invalid option.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input(">> ").strip()

        if choice == "1":
            user = login()
            if user:
                stock_menu(user)
        elif choice == "2":
            register()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Choose a valid option.")

if __name__ == "__main__":
    main()
