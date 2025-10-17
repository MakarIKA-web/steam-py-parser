from playwright.sync_api import sync_playwright
import pandas as pd
import re

def parse_price(price_str):
    if not price_str:
        return 0.0
    cleaned = price_str.replace('kr', '') \
                       .replace('€', '') \
                       .replace('£', '') \
                       .replace('$', '') \
                       .replace(',', '.') \
                       .replace(u'\xa0', '') \
                       .strip()
    cleaned = re.sub(r'[^0-9\.-]', '', cleaned)
    try:
        return float(cleaned)
    except:
        return 0.0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    ctx = browser.new_context()
    page = ctx.new_page()

    page.goto("https://store.steampowered.com/specials?flavor=contenthub_topsellers|")
    page.wait_for_timeout(7000)
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(3000)

    # Select game containers based on class that looks stable
    game_containers = page.query_selector_all("div._1_P15GG6AKyF_NMX2j4-Mu.Panel.Focusable")
    print(f"Found {len(game_containers)} games")

    games = []
    for game in game_containers:
        try:
            title_el = game.query_selector("div._2ekpT6PjwtcFaT4jLQehUK.StoreSaleWidgetTitle")
            title = title_el.inner_text().strip() if title_el else "N/A"

            link_el = game.query_selector("a.Focusable")
            link = link_el.get_attribute("href") if link_el else ""

            pub_date_el = game.query_selector("div._1qvTFgmehUzbdYM9cw0eS7")
            pub_date = pub_date_el.inner_text().strip() if pub_date_el else ""

            sentiment_el = game.query_selector("div._2nuoOi5kC2aUI12z85PneA")
            sentiment = sentiment_el.get_attribute("aria-label") if sentiment_el else ""

            count_el = game.query_selector("div._1wXL_MfRpdKQ3wZiNP5lrH")
            count = count_el.inner_text().strip() if count_el else ""

            disc_el = game.query_selector("div.cnkoFkzVCby40gJ0jGGS4")
            disc_str = disc_el.inner_text().strip() if disc_el else ""

            orig_el = game.query_selector("div._3fFFsvII7Y2KXNLDk_krOW")
            orig_str = orig_el.inner_text().strip() if orig_el else ""

            dpr_el = game.query_selector("div._3j4dI1yA7cRfCvK8h406OB")
            dpr_str = dpr_el.inner_text().strip() if dpr_el else ""

            orig_val = parse_price(orig_str)
            dpr_val = parse_price(dpr_str)
            savings = round(orig_val - dpr_val, 2)

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
            print(f"Error parsing game: {e}")
            continue

    games.sort(key=lambda g: g["Discount %"], reverse=True)

    df = pd.DataFrame(games)
    df.to_excel("steam_specials.xlsx", index=False)
    print("Done, wrote steam_specials.xlsx")

    browser.close()
