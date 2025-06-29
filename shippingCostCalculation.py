# Shipping Cost Calculation

## Input Package Weight and Shipping RateAdd commentMore actions
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate Shipping Cost
shippingCost = weight * rate

## Display the Result
print(f"Shipping Cost: {shippingCost} USD")
