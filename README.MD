<h1 align="center">🛒 Wired Coupon Automation Tool 💸 </h1>

<p align="center">
    <img src="https://github.com/Prem-ium/Wired-Coupon-Scraper/blob/main/Assets/Coupon-Promo-Code-Web-Scraper-Banner.png?raw=true" alt="Wired Coupon Automation Tool Banner"/>
</p>

<p align="center">Selenium script to retrieve latest Wired Coupons & Promo Codes for various websites such as Walmart, DoorDash, EBay, & more.</p>

<p align="right"> 
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/></a>
</p>

## Demo
**Important Notice:** [`Gold Sponsors`](https://github.com/sponsors/Prem-ium) are entitled to special privileges, including exclusive features like Discord Bot support for this project. If you belong to the `Gold` tier sponsorship, please access the private repository for the Python script containing Discord support.

This is a Demo for this project's GitHub Gold Sponsor version (not the public version). 
<video src="https://github.com/user-attachments/assets/a09813a5-95ff-4057-a7de-ec23c832b8ee" controls="controls" style="max-width: 100%; height: auto;">
    Your browser does not support video tags.
</video>


## Environment Variables 
| Variable         | Required | Default | Description |
| ---------------- | -------- | ------- | ----------- |
| `RETAILERS` | No       | ["walmart"]    | A list of supported retailer coupon pages from Wired.com/coupons |
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
- No Arguments:
``` bash
    python main.py
```
- Pass RETAILERS as an argument. Seperate with a comma (```,```)
``` bash
    python main.py amazon,doordash
```

## Example Output
Output for running ```python main.py amazon```:

```Python
---------------------------------------------------------------------------
Welcome to Wired Coupon Scraper.

RETAILERS argument received.
Gathering coupon codes for: ['amazon']
--------------------------------------------------
codes.txt file already exists
----------------------------------------------------------------------
Retrieving AMAZON Promo Code Offers...

108 AMAZON Promo Codes/Coupons were found!
--------------------------------------------------
Take 40% Off select products from Kwfrhix - Amazon Promo Code:
        40MMS6OP
https://www.wired.com/coupons/get/94554598?popup=true

Appended Take 40% Off select products from Kwfrhix - Amazon Promo Code: - https://www.wired.com/coupons/get/94554598?popup=true
--------------------------------------------------
--------------------------------------------------
Enjoy 40% Off select JingLeXin products - Amazon Promo Code:
        40YPKL1X
https://www.wired.com/coupons/get/94554602?popup=true

Appended Enjoy 40% Off select JingLeXin products - Amazon Promo Code: - 40YPKL1X - https://www.wired.com/coupons/get/94554602?popup=true
--------------------------------------------------
*---Rest of Promo Codes---*
```

# Donations

If you appreciate my work and would like to show your support, there are two convenient ways to donate:

1. **GitHub Sponsors**
   - [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium)
   - This is the preferred donation method as it incurs no transaction fees & different tiers offer perks.
   [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

2. **Buy Me A Coffee**
   - [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)
   - [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)

Your generous donations will go a long way in helping me cover the expenses associated with developing new features and promoting the project to a wider audience. I extend my heartfelt gratitude to all those who have already contributed. Thank you for your support!


## License

This project uses the [MIT License.](https://choosealicense.com/licenses/mit/)

