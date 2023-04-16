# DoorDash Coupon Scraper

## Introduction

The DoorDash Coupon Scraper is a Python script that scrapes DoorDash coupons from the [Wired Coupons](https://www.wired.com/coupons) website. The coupons are displayed in the console and can also be sent as notifications using Apprise.

[Possibile future expansion of my other DoorDash Repository, which tries promo codes for specific accounts/orders.](https://github.com/Prem-ium/DoorDash-PromoCodes)

## Example Output

```Python
Thanks for using DoorDash Coupon Scraper!
Created by: @Prem-ium (https://www.github.com/Prem-ium)

----------------------------------------------------------------------
codes.txt file already exists

76 DoorDash coupons were found!


--------------------------------------------------
Code US25SAVU2Q23 found in cache
Code US25SAVU2Q23 for Exclusive DoorDash promo code: 25% off orders over $15 + free delivery already exists in cache, skipping
--------------------------------------------------
DoorDash promo code: 50% off any $20 order + free delivery:
	XC66F45	
Appended XC66F45 to codes.txt
Updated today

----------------------------------------------------------------------
--------------------------------------------------
DoorDash coupon code: Spend $20, get $10 off + free delivery:
	RPD4JM7	
Appended RPD4JM7 to codes.txt
Updated today

----------------------------------------------------------------------
--------------------------------------------------
DoorDash discount code: 30% off any size order + free delivery:
	HUNGRYDEAL	
Appended HUNGRYDEAL to codes.txt
Updated today

----------------------------------------------------------------------
--------------------------------------------------
```

## Installation

1. Clone the repository:

```bash
    git clone https://github.com/Prem-ium/DoorDash-Coupon-Scraper.git
    cd coupon-scraper
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


## Environment Variables

| Variable         | Required | Default | Description |
| ---------------- | -------- | ------- | ----------- |
| `APPRISE_ALERTS` | No       | None    | A comma-separated list of Apprise notification services. |
| `ALLOW_DUPLICATES` | No    | `False` | If set to `True`, the script will allow sending duplicate coupons to apprise alerts. |

