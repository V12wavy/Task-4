import pandas as pd

df = pd.read_csv("Task4a_data.csv")


def convert_gbp_to_usd(amount_local):
    """ Takes in amount in GBP and returns amount in USD """
    rate = df["GBP - USD"][0]
    amount_usd = amount_local * rate
    return round(amount_usd, 2)


# Add function below to convert USD to GBP
def convert_usd_to_gbp(amount_local):
    rate = df["USD - GBP"][0]
    amount_gbp = amount_local * rate
    return round(amount_gbp, 2)


amount = float(input("Enter amount in GBP: "))
print(convert_usd_to_gbp(amount))

amount = float(input("Enter amount in USD: "))
print(convert_gbp_to_usd(amount))

# convert gbp=jpy
def convert_gbp_jpy(amount_local):
    rate = df["GBP- JPY"][0]
    amount = amount_local * rate
    return round(amount, 2)
