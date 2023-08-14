<h1 align="center">🛒 Wired Coupon Automation Tool 💸 </h1>

<p align="center">Selenium script to retrieve latest Wired Coupons & Promo Codes for various websites such as Walmart, DoorDash, EBay, & more.</p>

<p align="right"> 
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/></a>
</p>

## Environment Variables 
| Variable         | Required | Default | Description |
| ---------------- | -------- | ------- | ----------- |
| `RETAILERS` | No       | None    | A list of supported retailer coupon pages from Wired.com/coupons |
| `APPRISE_ALERTS` | No       | None    | A comma-separated list of Apprise notification services. |
| `ALLOW_DUPLICATES` | No    | `False` | If set to `True`, the script will allow sending duplicate coupons to apprise alerts. |
| `KEEP_ALIVE` | No    | `False` | If set to `True`, the script will run Flask server to allow Keep Alive. |

## Installation
1. Clone the repository:
```bash
    git clone https://github.com/Prem-ium/Wired-Coupon-Scraper.git
    cd Wired-Coupon-Scraper
```
2. Install the required packages:
```bash
    pip install -r requirements.txt
```
3. Set up the environment variables.
4. Run the script:
``` bash
    python main.py
```


## Example Output

```Python
Created new codes.txt file

10 Walmart coupons were found!

-------------------------
Summer Sale: 50% Off sitewide + Extra $100 Modloft Discount Code:
	DESIGNDELIVERED	
Appended DESIGNDELIVERED to codes.txt
--------------------------------------------------
-------------------------
$20 off when you spend $50+ with Walmart coupon:
	TRIPLE20	
Appended TRIPLE20 to codes.txt
--------------------------------------------------
-------------------------
Walmart Promo Code 2023: 30% off:
	WOWFRESH	
Appended WOWFRESH to codes.txt
--------------------------------------------------
-------------------------
# Runs through all remaining coupons #
```


## Donations

I've been working on this project for a few months now, and I'm really happy with how it's turned out. 
If you would like to show your appreciation for my work, I have set up two methods of sending in a donation: 

<a href="https://github.com/sponsors/Prem-ium">Github Sponsors</a>, the ideal donation method, to make donations with no fees!
<a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA" alt="GitHub Sponsor" img width="25%">
</a>

Otherwise, <a href="https://www.buymeacoffee.com/prem.ium">Buy-Me-Coffee</a> can be used to place donations as well. 
<a href="https://www.buymeacoffee.com/prem.ium" target="_blank">
        <img src="https://raw.githubusercontent.com/Prem-ium/youtube-analytics-bot/main/output-examples/media/coffee-logo.png" alt="Buy Me A Coffee" img width="25%">
</a>

I extend my heartfelt gratitude to all those who have already contributed. 
Thank you for your support!

## License

[MIT](https://choosealicense.com/licenses/mit/)

