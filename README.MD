<h1 align="center">🛒 Wired Coupon Automation Tool 💸</h1>

<p align="center">
    <img src="https://github.com/Prem-ium/Wired-Coupon-Scraper/blob/main/Assets/Coupon-Promo-Code-Web-Scraper-Banner.png?raw=true" alt="Wired Coupon Automation Tool Banner"/>
</p>

<p align="center">
    Selenium script to retrieve the latest Wired Coupons & Promo Codes for various websites such as Walmart, DoorDash, eBay, and more.
</p>

<p align="right"> 
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    <img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/>
    <a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="GitHub Sponsor"/>
    </a>
</p>

---

## 🚀 Demo  

### **Gold Sponsor Demo**  
Gold Sponsors get access to **exclusive features**, including Discord Bot integration for this project. If you're a `Gold` tier sponsor, please access the private repository containing the full script with Discord integration instead of this public version.  

**Demo Video:**  
<video src="https://github.com/user-attachments/assets/d369c9a9-7143-4d5f-9105-e6ae137b9c7d" controls style="max-width: 100%; height: auto;">
    Your browser does not support video playback.
    <a href="https://github.com/user-attachments/assets/d369c9a9-7143-4d5f-9105-e6ae137b9c7d">View the video here</a>.
</video>  

<details>
  <summary>Image Preview</summary>
  
  ![Discord Bot Demo](https://github.com/Prem-ium/Wired-Coupon-Scraper/blob/main/Assets/DiscordBot.png?raw=true)

</details>  

### **Public Version Demo**  
This is a demo of the **public** version of the project.  

🚨 **Note:** As of **4/3/25**, Wired has updated their website layout, breaking the current implementation. A **new version** is being developed for **GitHub Gold sponsors**, with a free public release planned at a later date.  

**Demo Video:**  
<video src="https://github.com/user-attachments/assets/9cc1370e-cf35-4ad3-8901-3e08c474212b" controls style="max-width: 100%; height: auto;">
    Your browser does not support video playback.
    <a href="https://github.com/user-attachments/assets/9cc1370e-cf35-4ad3-8901-3e08c474212b" download>Download the video here</a>.
</video>  

<details>
  <summary>Console Output Preview</summary>

```python
-------------------------------------------------------------
Welcome to Wired Coupon Scraper.

RETAILERS argument received.
Gathering coupon codes for: ['amazon']
--------------------------------------------------
codes.txt file already exists
--------------------------------------------------
Retrieving AMAZON Promo Code Offers...

108 AMAZON Promo Codes/Coupons were found!
--------------------------------------------------
Take 40% Off select products from Kwfrhix - Amazon Promo Code:
        40MMS6OP
https://www.wired.com/coupons/get/94554598?popup=true

Appended Take 40% Off select products from Kwfrhix - Amazon Promo Code: - https://www.wired.com/coupons/get/94554598?popup=true
--------------------------------------------------
Enjoy 40% Off select JingLeXin products - Amazon Promo Code:
        40YPKL1X
https://www.wired.com/coupons/get/94554602?popup=true

Appended Enjoy 40% Off select JingLeXin products - Amazon Promo Code: - 40YPKL1X - https://www.wired.com/coupons/get/94554602?popup=true
--------------------------------------------------
*---Rest of Promo Codes---*
```
</details>  

---

## ⚙️ Environment Variables  

The following environment variables can be configured to customize the script's behavior. All variables are **optional** and have default values:

| Variable           | Default               | Description |
|--------------------|-----------------------|-------------|
| `RETAILERS`        | `["walmart"]`         | A JSON-formatted list of supported retailers. Example: `["walmart", "amazon", "target"]`. |
| `APPRISE_ALERTS`   | None                  | A comma-separated list of Apprise notification service URLs for coupon alerts. Example: `discord://webhook_id/webhook_token,mailto://user:pass@smtp.example.com`. |
| `ALLOW_DUPLICATES` | `False`               | If `True`, duplicate coupons will be sent to Apprise alerts. |
| `KEEP_ALIVE`       | `False`               | If `True`, the script runs a Flask server for Keep-Alive functionality. |

---

## 📥 Installation  

1. **Clone the repository:**
```bash
git clone https://github.com/Prem-ium/Wired-Coupon-Scraper.git
cd Wired-Coupon-Scraper
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables.**  

4. **Run the script:**  
- Without arguments:
```bash
python main.py
```
- With retailer arguments (comma-separated):
```bash
python main.py amazon,doordash
```

---

## ❤️ Donations  

If you appreciate my work and want to support future development, consider donating:  

1. **GitHub Sponsors** *(Preferred – No transaction fees & includes perks!)*  
   - [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium)  
   - [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)  

2. **Buy Me A Coffee** *(Alternative donation method)*  
   - [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)  
   - [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)  

3. **Referral Links** *(Support without direct donations!)*  
   - Use my curated [Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md) for cashback, credit card bonuses, and brokerage rewards.  
   - [Explore Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md)  

Your support helps fund **new features**, **project improvements**, and **better automation tools**. Thank you! 🚀  

---

## Experiencing Issues? 🛠️  

Issues are disabled for the general public. As of **9/8/2024**, only **Silver/Gold tier sponsors** receive direct support. If you need assistance, please consider sponsoring me:  

[![Sponsor](https://img.shields.io/badge/sponsor-EA4AAA?style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/Prem-ium)  

---

## 📜 License  

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. See the `LICENSE` file for details.