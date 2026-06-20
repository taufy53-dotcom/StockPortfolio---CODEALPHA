# Stock Portfolio Tracker

## Description

Stock Portfolio Tracker is a simple Python project that helps users calculate the total value of their stock investments.

The program uses a predefined dictionary of stock prices and allows users to enter stock names and quantities. It then calculates the investment value for each stock and displays the total portfolio value. Users can also save the result to a text file.

## Features

* Displays available stock prices
* Accepts stock names and quantities
* Calculates investment value for each stock
* Calculates total portfolio value
* Handles invalid stock names
* Saves portfolio value to a text file (optional)

## Technologies Used

* Python

## Concepts Used

* Dictionaries
* Loops
* Conditional Statements
* User Input and Output
* Arithmetic Operations
* File Handling

## Stock Prices

| Stock | Price ($) |
| ----- | --------- |
| AAPL  | 180       |
| TSLA  | 250       |
| GOOGL | 150       |
| MSFT  | 420       |

## How to Run

1. Save the code as `stockportfolio.py`
2. Open a terminal in the project folder.
3. Run:

```bash
python3 stockportfolio.py
```

## Sample Output

```text
Available Stocks:
AAPL: $180
TSLA: $250
GOOGL: $150
MSFT: $420

How many stocks do you own? 2

Enter stock name: AAPL
Enter quantity: 5
AAPL Investment = $900

Enter stock name: TSLA
Enter quantity: 2
TSLA Investment = $500

Total Portfolio Value = $1400

Save result to file? yes

Result saved in portfolio.txt
```

## Output File

If the user chooses to save the result, a file named `portfolio.txt` is created.

Example:

```text
Total Portfolio Value = $1400
```

## Project Structure

```text
StockPortfolio/
│
├── stockportfolio.py
├── README.md
├── flowchart.txt
└── portfolio.txt
```

## Author

Taufique

