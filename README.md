# UNIT-PROJECT-1



## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use your coding skills in Python accurately.
- Organize Your Code into modules & (or packages)
- Use git & Github to track changes in your code.

## Example Project :  An online Grocery Store :

#### Overview : An online store that sells fruits to customers. This online store has 2 main users. The customer and the manager of the store . Each one of them should be able to do the following tasks for the store to function properly . 

### 1. Choose from stock list
You can pick one of these company:
- AAPL → Apple
- TSLA → Tesla
- GOOG → Google
- MSFT → Microsoft
- AMZN → Amazon

### 2. Log in / Register
- New users can register with a username and password.
- Existing users can log in.

### 3. View Prices
- You can write two dates (start and end), and it shows:
  - Last closing price
  - Highest price
  - Lowest price
- If you don’t write dates, it shows prices for the last 5 days.
- The vertical label on the graph says "RS" instead of "Price".

### 4. Save Prices
- You can save the prices in a CSV file.
- You can choose the file name or let the program name it automatically based on dates.

### 5. Draw Graph
- You can choose to show a simple graph of the prices with labels for date (labelx) and RS(labely).

### 6. Logs
- Everything you do (login, search, save, graph) is saved in `report_user.json`.
- You can see your history from the menu.



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
pip install yfinance matplotlib
```

---

## How to Start
Run the app:
```bash
python main.py
```

Then follow the instructions:
```
Main Menu:
1. Login
2. Register
3. Exit
```

After login:
```
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

---

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
- All data is fetched live from the internet — no fake data.

### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage. 

### NOTE: before submitting the final project, please do the following command:
`pip freeze > requirements.txt` to enable use to know & use the packages used in your project.
