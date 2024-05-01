

w1 = float(input("First asset's weight: "))

var1 = float(input("First asset's variance: "))

w2 = float(input("Second asset's weight: "))

var2 = float(input("Second asset's variance: "))

covar = float(input("Enter covariance: "))

ans =  (w1 ** 2 * var1) + (w2 ** 2 * var2) + (2 * w1 * w2 * covar)

print(f"Your portfolio has a variance of: {ans}")