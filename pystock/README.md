

## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :
file name is: pystock

PyStock is a Python-based command-line application that allows users to fetch, analyze, and visualize stock market data for public companies using Yahoo Finance. It supports historical data retrieval, graphical visualization, and CSV export, all through simple CLI commands.
Language: Python

Interface: Command Line Interface (CLI)

Code Structure: Python modules & packages

Libraries: pandas, matplotlibو json, y.financem, argparse

Supporting Files: requirements.txt, README.md

## Example Project :  An online Grocery Store :

#### Overview : An online store that sells fruits to customers. This online store has 2 main users. The customer and the manager of the store . Each one of them should be able to do the following tasks for the store to function properly . 

### 1. Choose from stock list
You can pick one of these company:
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

### 2. Log in / Register
- New users can register with a username and password.
- Existing users can log in.

### 3. View Prices
- You can write two dates (start and end), and it shows:
  - Last closing price
  - Highest price
  - Lowest price
- If you don’t write dates, it shows prices for the last 5 days.
- The vertical label on the graph says "USD" instead of "Price".

### 4. Save Prices
- You can save the prices in a CSV file.
- You can choose the file name or let the program name it automatically based on dates.

### 5. Draw Graph
- You can choose to show a simple graph of the prices with labels for date (labelx) and RS(labely).

### 6. save data
- Everything you do (login, search, save, graph) is saved in `report_user.json`.
- You can see your history from the menu.


Argument	Description
symbol--> (Required) Stock symbol (e.g., AAPL, TSLA, GOOG)
--date_from	--> Start date (format: YYYY-MM-DD)
--date_to--> End date (format: YYYY-MM-DD)
--range	 like 5d, 1mo, 6mo, 1y
--graphed	Show graph of stock prices
-- save Data



#### Usage :
## Files
| File               | What it does                  |
|--------------------|-------------------------------|
| `main.py`          | The program logic and menus   |
| `login.py`         | Handles user login, register, and logs |
| `users.json`       | Stores users and passwords    |
| `report_user.json` | Saves your activity logs  with date     |
| `*.csv`            | Files where price (RS)are saved  |



## How to Install
Install required tools:
```bash
pip install yfinance matplotlib pandas


##  Start
Run the app: 
bash
python login.py


Then follow the instructions:

Main Menu:
1. Login
2. Register
3. Exit


After login:

Stock Menu:
1. Choose from stock list
2. View Activity Log
3. Logout
```

---

## Example
```
Activity Log for shahad:
- Logged in
- Searched AAPL from 2025-05-01 to 2025-06-01 — Last: 210.22, High: 220.33, Low: 200.10
- Saved data to AAPL_2025-05-01_to_2025-06-01.csv
- Viewed graph for AAPL
```
Username: shahad
Password: shad1234
Welcome, shahad

Stock Menu:
1. Logout
2. View Activity Log
3. Choose from stock list
>> 3

Choose a company:
...
>> 2
Selected: TSLA (Tesla Motors)
Use custom dates? (yes/no): yes
From date (YYYY-MM-DD): 2025-2-25
To date (YYYY-MM-DD): 2025-6-8
Getting data for TSLA...

Last price: 295.14
High: 367.71, Low: 214.25

Save this data?
1. Yes by default name
>> 1
Saved to TSLA_2025-2-25_to_2025-6-8.csv

Show graph? (yes/no): yes




## Notes
- All actions are saved per user.
- You use the keyboard for everything (fully CLI).
- The program checks for wrong input (like wrong dates or invalid symbols).
- It validates dates before making the API call.
- Code is organized into logical files (login, main, data files).


---

## API Reference
This project uses:
-  **Yahoo Finance API** *(via `yfinance`)* to fetch real-time and historical data like:
  - `Open`, `High`, `Low`, `Close`
  - It sends requests like:
    ```python
    yf.download("AAPL", start="2025-05-01", end="2025-06-01")
    ```


### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage. 

### NOTE: before submitting the final project, please do the following command:
`pip freeze > requirements.txt` to enable use to know & use the packages used in your project.
yfinance
matplotlib
pandas
