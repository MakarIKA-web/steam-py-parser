Steam Specials Scraper

This project is a web scraper that extracts information about discounted games from the Steam store's "Specials" page (top sellers). It collects key details such as game title, release date, user review sentiment, number of reviews, original and discounted prices, and the savings amount. The results are saved into an Excel file for easy analysis.

Description

Steam frequently runs sales and discounts on many popular games. This scraper automates the process of gathering current deals by programmatically navigating to the Steam Specials page and extracting data from the game listing containers. It uses Playwright for browser automation to render the page fully and then parses the game information using CSS selectors.

The output is a neatly formatted Excel file (steam_specials.xlsx) containing:

- Game Title
- Store Link
- Release Date
- User Review Sentiment
- Number of Reviews
- Discount Percentage
- Original Price
- Discounted Price
- Total Savings (calculated)

This tool can help gamers and analysts quickly identify the best deals on Steam without manually browsing the website.

---

How it works

1. The script launches a Chromium browser session in non-headless mode (you can switch this to headless if preferred).
2. It navigates to the Steam Specials page filtered by top sellers.
3. Waits for the page content to load fully, including a scroll to the bottom to load more games.
4. It selects all the game containers from the page using CSS selectors.
5. Extracts relevant data such as game title, prices, discount, review ratings, and links.
6. Cleans and converts price strings into numerical values.
7. Calculates the savings for each game.
8. Sorts the games by discount percentage in descending order.
9. Exports the collected data into an Excel spreadsheet.

---

Installation & Requirements

Prerequisites

- Python 3.7+
- Playwright (https://playwright.dev/python/)
- pandas
- openpyxl (for Excel support)

Installing dependencies

You can install the required Python packages using pip:

pip install playwright pandas openpyxl

After installing Playwright, you need to install the browser binaries:

python -m playwright install

---

Usage

1. Clone this repository or download the script.

2. Run the Python script:

python steam_specials_scraper.py

3. The script will open a Chromium browser window, navigate to Steam's specials page, and scrape the data.

4. After completion, an steam_specials.xlsx file will be created in the same directory.

---

Notes

- The script uses a fixed CSS selector for Steam's page structure. If Steam updates their website design, selectors might need adjustments.
- You can set headless=True in browser.launch() for silent background scraping.
- The script waits for some fixed timeouts; these may need tuning depending on your network speed.

---

License

This project is open-source and available under the MIT License.

---

Contributions

Feel free to fork this repository and submit pull requests if you want to improve or extend the functionality.

---

Contact

For questions or issues, please open an issue on the GitHub repository.

---

Happy gaming and happy scraping! 🎮✨
