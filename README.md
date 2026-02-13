Steam Specials Scraper

This project is a Python web scraper that extracts information about discounted games from the Steam Store’s "Specials" page (Top Sellers section). It collects key details such as game title, store link, release date, user review sentiment, number of reviews, original price, discounted price, discount percentage, and the calculated savings amount. The results are saved into an Excel file for easy analysis.

Description

Steam frequently runs sales and discounts on many popular games. This scraper automates the process of gathering current deals by programmatically navigating to the Steam Specials page and extracting data from the game listing containers.

It uses Playwright for browser automation to fully render the page content and pandas to structure and export the collected data. The script processes price strings, converts them into numeric values, calculates total savings, sorts the games by highest discount, and exports everything into an Excel spreadsheet.

The output is a neatly formatted Excel file (steam_specials.xlsx) containing:

Game Title

Store Link

Release Date

User Review Sentiment

Number of Reviews

Discount Percentage

Original Price

Discounted Price

Total Savings (calculated)

How It Works

Launches a Chromium browser session using Playwright

Navigates to the Steam Specials (Top Sellers) page

Waits for the content to fully load

Extracts game data using CSS selectors

Cleans and converts price values

Calculates savings for each game

Sorts results by discount percentage (descending)

Exports data into steam_specials.xlsx

Installation & Requirements

Prerequisites:

Python 3.7+

Playwright

pandas

openpyxl

Install dependencies:

pip install playwright pandas openpyxl

After installing Playwright, install the required browser binaries:

python -m playwright install

Usage

Clone the repository:

git clone https://github.com/MakarIKA-web/steam-py-parser.git

cd steam-py-parser

Run the script:

python steam-parser.py

After execution, the file steam_specials.xlsx will be created in the project directory.

Notes

The scraper relies on Steam’s current HTML structure. If Steam updates their website layout, CSS selectors may need adjustments.

You can enable headless mode in the script if you prefer background execution.

Loading delays may vary depending on network speed.

License

This project is open-source and available under the MIT License.

Contributions

Feel free to fork the repository and submit pull requests to improve or extend the functionality.

Contact

For questions or issues, please open an issue on the GitHub repository.

Happy gaming and happy scraping! 🎮
