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

<video src="https://github.com/user-attachments/assets/d369c9a9-7143-4d5f-9105-e6ae137b9c7d" controls="controls" style="max-width: 100%; height: auto;">
    Your browser does not support video tags.
https://github.com/user-attachments/assets/d369c9a9-7143-4d5f-9105-e6ae137b9c7d
</video>

<details>
  <summary>Image Preview (If the video does not work)</summary>

![Discord Bot Demo](https://github.com/Prem-ium/Wired-Coupon-Scraper/blob/main/Assets/DiscordBot.png?raw=true)

</details>

This is a Demo for the public version:
<video src="https://github.com/user-attachments/assets/9cc1370e-cf35-4ad3-8901-3e08c474212b" controls="controls" style="max-width: 100%; height: auto;">
    Your browser does not support video tags.
</video>
<details>
  <summary>Console Output Preview (If the video does not work)</summary>
Output for running `python main.py amazon`


```python
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
</details>



## Environment Variables

The following environment variables can be configured to customize the behavior of the script. All variables are optional and have default values as shown below:

| Variable           | Default               | Description                                                                                                                                                  |
|--------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RETAILERS`        | `["walmart"]`         | A JSON-formatted list of supported retailer coupon pages from Wired.com/coupons. Example: `["walmart", "amazon", "target"]`.                                                                         |
| `APPRISE_ALERTS`   | None                  | A comma-separated list of Apprise notification service URLs to which coupon alerts will be sent. Example: `discord://webhook_id/webhook_token,mailto://user:pass@smtp.example.com`.                   |
| `ALLOW_DUPLICATES` | `False`               | If set to `True`, the script will allow sending duplicate coupons to Apprise alerts. Use this option if you want to be notified about the same coupon multiple times.                                |
| `KEEP_ALIVE`       | `False`               | If set to `True`, the script will run a Flask server to allow Keep-Alive functionality. This can be useful for deployments that need to keep the script running continuously.                        |

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

## Experiencing Issues? 🛠️
As of 9/8/2024, I have disabled the `Issues` privilege for the general public. For direct support on any bugs or issues, please consider sponsoring me as a GitHub Sponsor under the `Silver` or `Gold` tier. 
[![Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white)](https://github.com/sponsors/Prem-ium)

# Donations

If you appreciate my work and would like to show your support, there are two convenient ways to donate:

1. **GitHub Sponsors**
   - [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium)
   - This is the preferred donation method as it incurs no transaction fees & different tiers offer perks.
   [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

2. **Buy Me A Coffee**
   - [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)
   - [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)

3. **Referral Links**  
    - If you're unable to make a monetary donation, you can still support my work by using my curated [Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md). Earn bonuses and rewards while contributing to my projects at the same time.  
    - [Explore Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md)  

Your generous donations will go a long way in helping me cover the expenses associated with developing new features and promoting the project to a wider audience. I extend my heartfelt gratitude to all those who have already contributed. Thank you for your support!


## License

This project uses the [MIT License.](https://choosealicense.com/licenses/mit/)

