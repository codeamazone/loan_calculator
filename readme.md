# Command Line Loan Calculator

I wrote this program as part of the Python Developer Path by JetBrains Academy (https://hyperskill.org).
It is operated from the command line and allows you to calculate monthly payments, the principal amount, or the number of months it takes to repay a loan.

There are two different types of payment: differentiated and annuity payment.

The program requires four parameters.

Possible parameters are:

- **--type** (always required), indicating the type of payment ("annuity" or "diff")
- **--payment**, specifying the monthly payment. This can only be provided for annuity payment, since the montly payments differ in differentiated payment
- **--principal**, referring to the loan principal
- **--periods**, referring to the number of months needed to repay the loan
- **--interest** (always required), denoting the interest rate. It is specified withour the %-sign

The calculator is able to calculate either the monthly payment, or the loan principal, or the periods, depending on which parameter you do not provide when starting it.

## Examples

### Calculating differentiated payments for a 10-month loan with a principal of 1,000000 at 10% interest

```
$ python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

Month 1: paid out 108334
Month 2: paid out 107500
Month 3: paid out 106667
Month 4: paid out 105834
Month 5: paid out 105000
Month 6: paid out 104167
Month 7: paid out 103334
Month 8: paid out 102500
Month 9: paid out 101667
Month 10: paid out 100834
Overpayment = 45837
```

### Calculating the annuity payment for a 120-month (10-year) loan with a principal amount of 1,000,000 at 12% interest

```
$ python creditcalc.py --type=annuity --principal=1000000 --periods=120 --interest=12

Your annuity payment = 14348!
Overpayment = 721760
```

### Calculating differentiated payments given a principal of 700,000 over 6 months at an interest rate of 9.7%

```
$ python creditcalc.py --type=diff --principal=700000 --periods=6 --interest=9.7

Month 1: paid out 122325
Month 2: paid out 121382
Month 3: paid out 120439
Month 4: paid out 119496
Month 5: paid out 118553
Month 6: paid out 117610
Overpayment = 19805
```

### Calculating the principal for a user paying 5,050 per month for 120 months (10 years) at 5.6% interest

```
$ python creditcalc.py --type=annuity --payment=5100 --periods=120 --interest=5.6

Your credit principal = 463207!
Overpayment = 142793

```
