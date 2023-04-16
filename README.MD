# DoorDash Coupon Scraper

## Introduction

<img src="https://raw.githubusercontent.com/Prem-ium/DoorDash-Coupon-Scraper/master/output-examples/Output.png" width="500">

The DoorDash Coupon Scraper is a Python script that scrapes DoorDash coupons from the [Wired Coupons](https://www.wired.com/coupons) website. The coupons are displayed in the console and can also be sent as notifications using Apprise.

[Possibile future expansion of my other DoorDash Repository, which tries promo codes for specific accounts/orders.](https://github.com/Prem-ium/DoorDash-PromoCodes)

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

