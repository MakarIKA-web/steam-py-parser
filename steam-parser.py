# Importing the necessary libraries
from playwright.sync_api import sync_playwright  # Playwright for web scraping
import pandas as pd  # Pandas for working with data and exporting to Excel
import re  # Regular expressions for cleaning and parsing strings

# Function to parse price values from the string
def parse_price(price_str):
    if not price_str:  # If the price string is empty or None, return 0.0
        return 0.0
    # Clean the price string by removing unwanted characters
    cleaned = price_str.replace('kr', '') \
                        .replace('€', '') \
                        .replace('£', '') \
                        .replace('$', '') \
                        .replace(',', '.') \
                        .replace(u'\xa0', '') \
                        .strip()
    cleaned = re.sub(r'[^0-9.-]', '', cleaned)
    try:
        # Attempt to convert the cleaned price string to a float
        return float(cleaned)
    except:  # If conversion fails, return 0.0
        return 0.0

# Begin scraping using Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Launch the browser in non-headless mode (visible)
    ctx = browser.new_context()  # Create a new browser context (tab)
    page = ctx.new_page()  # Open a new page/tab in the context

    # Navigate to the Steam specials page
    page.goto("https://store.steampowered.com/specials?flavor=contenthub_topsellers|")
    page.wait_for_timeout(7000)  # Wait for 7 seconds to ensure the page is fully loaded
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")  # Scroll to the bottom of the page to load more games
    page.wait_for_timeout(3000)  # Wait for an additional 3 seconds to ensure all content is loaded

    # Select game containers on the page (each game is wrapped in a div with a specific class)
    game_containers = page.query_selector_all("div._1_P15GG6AKyF_NMX2j4-Mu.Panel.Focusable")
    print(f"Found {len(game_containers)} games")  # Print the number of games found on the page

    games = []  # Initialize an empty list to store game data

    # Loop through each game container and extract relevant details
    for game in game_containers:
        try:
            # Extract the game title using its CSS class
            title_el = game.query_selector("div._2ekpT6PjwtcFaT4jLQehUK.StoreSaleWidgetTitle")
            title = title_el.inner_text().strip() if title_el else "N/A"  # Get the title or "N/A" if not found

            # Extract the game link (URL)
            link_el = game.query_selector("a.Focusable")
            link = link_el.get_attribute("href") if link_el else ""  # Get the href attribute or empty string if not found

            # Extract the publication date (if available)
            pub_date_el = game.query_selector("div._1qvTFgmehUzbdYM9cw0eS7")
            pub_date = pub_date_el.inner_text().strip() if pub_date_el else ""  # Get the publication date or empty string

            # Extract the sentiment rating (e.g., good/bad) from the aria-label attribute
            sentiment_el = game.query_selector("div._2nuoOi5kC2aUI12z85PneA")
            sentiment = sentiment_el.get_attribute("aria-label") if sentiment_el else ""  # Get the sentiment or empty string

            # Extract the review count
            count_el = game.query_selector("div._1wXL_MfRpdKQ3wZiNP5lrH")
            count = count_el.inner_text().strip() if count_el else ""  # Get the review count or empty string

            # Extract the discount information (e.g., "50% off")
            disc_el = game.query_selector("div.cnkoFkzVCby40gJ0jGGS4")
            disc_str = disc_el.inner_text().strip() if disc_el else ""  # Get the discount string or empty string

            # Extract the original price of the game
            orig_el = game.query_selector("div._3fFFsvII7Y2KXNLDk_krOW")
            orig_str = orig_el.inner_text().strip() if orig_el else ""  # Get the original price or empty string

            # Extract the discounted price
            dpr_el = game.query_selector("div._3j4dI1yA7cRfCvK8h406OB")
            dpr_str = dpr_el.inner_text().strip() if dpr_el else ""  # Get the discounted price or empty string

            # Parse the original and discounted prices using the parse_price function
            orig_val = parse_price(orig_str)  # Convert original price string to float
            dpr_val = parse_price(dpr_str)  # Convert discount price string to float
            savings = round(orig_val - dpr_val, 2)  # Calculate the savings (difference between original and discounted prices)

            # Append the extracted data for this game to the list
            games.append({
                "Title": title,
                "Link": link,
                "Pub Date": pub_date,
                "Sentiment": sentiment,
                "Review Count": count,
                "Discount %": disc_str,
                "Original Price": orig_str,
                "Discount Price": dpr_str,
                "Savings": savings
            })
        except Exception as e:
            # If there is any error while parsing this particular game, print the error and continue to the next game
            print(f"Error parsing game: {e}")
            continue

    # Sort the list of games by the "Discount %" field in descending order
    games.sort(key=lambda g: g["Discount %"], reverse=True)

    # Create a pandas DataFrame from the list of games
    df = pd.DataFrame(games)
    
    # Write the DataFrame to an Excel file (without including the index column)
    df.to_excel("steam_specials.xlsx", index=False)
    print("Done, wrote steam_specials.xlsx")  # Indicate that the file has been written successfully

    browser.close()  # Close the browser after the scraping is done
