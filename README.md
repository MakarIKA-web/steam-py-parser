# 🎮 Steam Specials Scraper

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/github/license/MakarIKA-web/steam-py-parser)

A Python web scraper that collects discounted game data from Steam's
**Specials (Top Sellers)** page and exports it into a structured Excel
file.

Built using **Playwright** for browser automation and **pandas** for
data processing.

------------------------------------------------------------------------

## 📌 Overview

Steam frequently runs sales on popular games. This project automates the
process of gathering current discounts by:

-   Opening Steam's Specials page
-   Extracting game information
-   Cleaning and formatting price data
-   Calculating savings
-   Exporting results into an Excel spreadsheet

The final output is a ready-to-use `steam_specials.xlsx` file for easy
analysis.

------------------------------------------------------------------------

## 📊 Data Collected

For each discounted game, the scraper collects:

-   Game Title\
-   Store Link\
-   Release Date\
-   User Review Sentiment\
-   Number of Reviews\
-   Discount Percentage\
-   Original Price\
-   Discounted Price\
-   Total Savings (calculated)

Games are automatically sorted by highest discount.

------------------------------------------------------------------------

## ⚙️ How It Works

1.  Launches a Chromium browser session using Playwright\
2.  Navigates to Steam's Specials (Top Sellers) page\
3.  Scrolls to load all visible games\
4.  Extracts data using CSS selectors\
5.  Cleans and converts price strings into numeric values\
6.  Calculates savings\
7.  Sorts results by discount\
8.  Exports everything to Excel

------------------------------------------------------------------------

## 🧰 Installation

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/MakarIKA-web/steam-py-parser.git
cd steam-py-parser
```

### 2️⃣ (Optional but Recommended) Create a Virtual Environment

**Linux/macOS**

``` bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**

``` bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

``` bash
pip install playwright pandas openpyxl
```

### 4️⃣ Install Playwright Browsers

``` bash
python -m playwright install
```

------------------------------------------------------------------------

## 🚀 Usage

Run the script:

``` bash
python steam-parser.py
```

After execution, you will find:

    steam_specials.xlsx

in the project directory.

------------------------------------------------------------------------

## 🕶 Running in Headless Mode

If you prefer running without opening a visible browser window, modify:

``` python
browser = playwright.chromium.launch(headless=True)
```

------------------------------------------------------------------------

## 📂 Project Structure

    steam-py-parser/
    │
    ├── steam-parser.py
    ├── README.md
    └── steam_specials.xlsx (generated)

------------------------------------------------------------------------

## ⚠️ Notes & Limitations

-   The scraper depends on Steam's current HTML structure.\
    If Steam updates their layout, CSS selectors may need adjustments.
-   Fixed timeouts are used; slower networks may require tuning.
-   Excessive automated scraping may violate Steam's Terms of Service.\
    Use responsibly.

------------------------------------------------------------------------

## 📈 Example Output

  Game Title     Discount   Original Price   Sale Price   Savings
  -------------- ---------- ---------------- ------------ ---------
  Example Game   -75%       \$59.99          \$14.99      \$45.00

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome!

1.  Fork the repository\
2.  Create a new branch\
3.  Make your changes\
4.  Submit a Pull Request

Please ensure your code is clean and well-documented.

------------------------------------------------------------------------

## 📜 License

This project is licensed under the MIT License.

------------------------------------------------------------------------

## 💬 Contact

If you encounter issues or have feature suggestions, please open an
issue on the GitHub repository.

------------------------------------------------------------------------

Happy gaming and happy scraping! 🎮✨
