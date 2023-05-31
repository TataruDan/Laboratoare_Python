# declaration of the list of dictionaries
mobile_operator = [
    {
        "subscription_name" : "Mountain",
        "month" : 4,
        "price_for_call" : 1.50,
        "internet_mobile_subscription" : 50,
        "auto_subscription" : True,
        "internet_packages" : ["77GB","50GB","60GB"],
    },
{
        "subscription_name" : "Cascada",
        "month" : 2,
        "price_for_call" : 4.50,
        "internet_mobile_subscription" : 50.99,
        "auto_subscription" : True,
        "internet_packages" : ["30GB","35GB","38GB"],
    },
{
        "subscription_name" : "Cosmos",
        "month" : 8,
        "price_for_call" : 2.50,
        "internet_mobile_subscription" : 140.50,
        "auto_subscription" : False,
        "internet_packages" : ["Unlimited","150GB","100GB"],
    },
{
        "subscription_name" : "Butterfly",
        "month" : 5,
        "price_for_call" : 3.33,
        "internet_mobile_subscription" : 99.20,
        "auto_subscription" : True,
        "internet_packages" : ["130GB","120GB","100GB"],
    },
{
        "subscription_name" : "Trend",
        "month" : 3,
        "price_for_call" : 4.20,
        "internet_mobile_subscription" : 77.50,
        "auto_subscription" : False,
        "internet_packages" : ["77GB","50GB","60GB"],
    },
]
# printing to the screen the information
print("Number of records ({}):".format(len(mobile_operator)))
# First dictionary
print("1.")
print("Subscription name : {}".format(mobile_operator[0]["subscription_name"]))
print("Months: {}".format(mobile_operator[0]["month"]))
print("Price for call: {} $".format(mobile_operator[0]["price_for_call"]))
print("Mobile internet subscription : {} $".format(mobile_operator[0]["internet_mobile_subscription"]))
print("Auto subscription: {}".format(mobile_operator[0]["auto_subscription"]))
print("Internet packages: {}".format(mobile_operator[0]["internet_packages"]))
# Second dictionary
print("\n2.")
print("Subscription name : {}".format(mobile_operator[1]["subscription_name"]))
print("Months: {}".format(mobile_operator[1]["month"]))
print("Price for call: {} $".format(mobile_operator[1]["price_for_call"]))
print("Mobile internet subscription : {} $".format(mobile_operator[1]["internet_mobile_subscription"]))
print("Auto subscription: {}".format(mobile_operator[1]["auto_subscription"]))
print("Internet packages: {}".format(mobile_operator[1]["internet_packages"]))
# Third dictionary
print("\n3.")
print("Subscription name : {}".format(mobile_operator[2]["subscription_name"]))
print("Months: {}".format(mobile_operator[2]["month"]))
print("Price for call: {} $".format(mobile_operator[2]["price_for_call"]))
print("Mobile internet subscription : {} $".format(mobile_operator[2]["internet_mobile_subscription"]))
print("Auto subscription: {}".format(mobile_operator[2]["auto_subscription"]))
print("Internet packages: {}".format(mobile_operator[2]["internet_packages"]))
# Fourth dictionary
print("\n4.")
print("Subscription name : {}".format(mobile_operator[3]["subscription_name"]))
print("Months: {}".format(mobile_operator[3]["month"]))
print("Price for call: {} $".format(mobile_operator[3]["price_for_call"]))
print("Mobile internet subscription : {} $".format(mobile_operator[3]["internet_mobile_subscription"]))
print("Auto subscription: {}".format(mobile_operator[3]["auto_subscription"]))
print("Internet packages: {}".format(mobile_operator[3]["internet_packages"]))
# Fifth dictionary
print("\n5.")
print("Subscription name : {}".format(mobile_operator[4]["subscription_name"]))
print("Months: {}".format(mobile_operator[4]["month"]))
print("Price for call: {} $".format(mobile_operator[4]["price_for_call"]))
print("Mobile internet subscription : {} $".format(mobile_operator[4]["internet_mobile_subscription"]))
print("Auto subscription: {}".format(mobile_operator[4]["auto_subscription"]))
print("Internet packages: {}".format(mobile_operator[4]["internet_packages"]))