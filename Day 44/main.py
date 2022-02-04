import requests, smtplib, lxml
from bs4 import BeautifulSoup


def main():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    acc_lang = "en-US,en;q=0.9"

    headers = {
        "User-Agent": user_agent,
        "Accept-Language": acc_lang,
    }
    url = "https://www.amazon.in/Kindle-10th-Gen/dp/B07FQ4Q7MB/"

    res = requests.get(
        headers=headers,
        url=url,
    )

    soup = BeautifulSoup(res.text, "lxml")

    elem = soup.select_one(".a-price-whole").text
    title = soup.select_one("#productTitle").text

    pc = elem.replace(",", "")

    price = int(pc.replace(".", ""))

    print(price)

    EMAIL = "reaperfs144@gmail.com"
    PSSWORD = "7Pz4j56bGYWhsu"
    max_price = 8999

    msg = f"""
    Price Drop!!!
    Product: {title}
    Price: {price}
    Link: {url}
    """

    if price < max_price:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PSSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="fsaiyad990@gmail.com",
                msg=msg,
            )

    else:
        print("Price still high")


if __name__ == "__main__":
    main()
