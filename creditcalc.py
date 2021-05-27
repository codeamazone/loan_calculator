"""
STAGE 2
print('Enter the credit principal:')
principal = int(input())
print('''What do you want to calculate?
type "m" - for the number of months,
type "p" - for the monthly payment:''')
selection = input()
if selection == 'm':
    print('Enter the monthly payment:')
    installment = int(input())
    no_of_months = principal // installment + (principal % installment > 0)
    print(f'It takes {no_of_months} months to repay the credit' if no_of_months > 1 else f'It takes {no_of_months} month to repay the credit')
elif selection == 'p':
    print('Enter the count of months:')
    months = int(input())
    installment = principal // months + (principal % months > 0)
    if principal % months == 0:
        print(f'Your monthly payment = {int(installment)}')
    elif principal % months > 0:
        last_payment = principal - (months - 1) * installment
        print(f'Your monthly payment = {installment} with last monthly payment = {last_payment}.')

STAGE 3
import math

import sys


def calculate_differentiated_payment(x, y, z):
    payments = []
    for m in range(1, y + 1):
        diff_payment = x / y + z * (x - (x * (m - 1)) / y)
        payments.append(math.ceil(diff_payment))
    for j in range(len(payments)):
        print(f'Month {j + 1}: paid out {payments[j]}')
    print(f'Overpayment = {sum(payments) - x}')


def calculate_n(x, y, z):
    no_of_payments = math.ceil(math.log((y / (y - z * x)), (z + 1)))
    years = no_of_payments // 12
    months = no_of_payments % 12
    if years < 1:
        print(
            f'You need {months} months to repay this credit!' if months > 1 else f'You need 1 month to repay this credit!')
    elif years == 1:
        if months == 0:
            print(f'You need 1 year to repay this credit!')
        elif months == 1:
            print(f'You need 1 year and one month to repay this credit!')
        elif months > 1:
            print(f'You need 1 year and {months} months to repay this credit!')
    elif years > 1:
        if months == 0:
            print(f'You need {years} years to repay this credit!')
        elif months == 1:
            print(f'You need {years} years and one month to repay this credit!')
        elif months > 1:
            print(
                f'You need {years} years and {months} months to repay this credit!')


def calculate_annuity(x, y, z):
    annuity = math.ceil(
        x * (z * math.pow((1 + z), y)) / (math.pow((1 + z), y) - 1))
    print(f'Your annuity payment = {annuity}!')


def calculate_credit_principal(x, y, z):
    principal = (x / ((z * math.pow((1 + z), y)) / (math.pow((1 + z), y) - 1)))
    print(f'Your credit principal = {int(principal)}!')


print('''What do you want to calculate?
type "n" - for the number of months,
type "a" - for the annuity monthly payment,
type "p" for the credit principal:''')
selection = input()
if selection == 'n':
    print('Enter the credit principal:')
    p = int(input())
    print('Enter the monthly payment:')
    a = float(input())
    print('Enter the credit interest:')
    credit_interest = float(input())
    i = credit_interest / (12 * 100)
    calculate_n(p, a, i)
elif selection == 'a':
    print('Enter the credit principal:')
    p = int(input())
    print('Enter the number of periods:')
    n = int(input())
    print('Enter the credit interest:')
    credit_interest = float(input())
    i = credit_interest / (12 * 100)
    calculate_annuity(p, n, i)
elif selection == 'p':
    print('Enter the monthly payment:')
    a = float(input())
    print('Enter the count of periods:')
    n = int(input())
    print('Enter the credit interest:')
    credit_interest = float(input())
    i = credit_interest / (12 * 100)
    calculate_credit_principal(a, n, i)"""

# STAGE 4
import math
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str, help='type')
parser.add_argument('--principal', type=int, help='principal')
parser.add_argument('--payment', type=float, help='payment')
parser.add_argument('--periods', type=int, help='periods')
parser.add_argument('--interest', type=float, help='interest')
args = parser.parse_args()

# different types of errors
len_error = len(sys.argv) != 5
no_type = args.type is None
type_error = args.type not in {'annuity', 'diff'}
diff_error = args.type == 'diff' and args.payment is not None
no_interest = args.interest is None
neg_principal = args.principal is not None and args.principal < 0
neg_payment = args.payment is not None and args.payment < 0
neg_periods = args.periods is not None and args.periods < 0
neg_interest = args.interest is not None and args.interest < 0
neg_error = neg_principal or neg_payment or neg_periods or neg_interest


def calculate_differentiated_payment(x, y, z):
    payments = []
    for m in range(1, y + 1):
        diff_payment = x / y + z * (x - (x * (m - 1)) / y)
        payments.append(math.ceil(diff_payment))
    for j in range(len(payments)):
        print(f'Month {j + 1}: paid out {payments[j]}')
    print(f'Overpayment = {sum(payments) - x}')


def calculate_annuity(x, y, z):
    annuity = math.ceil(x * (z * math.pow((1 + z), y)) / (math.pow((1 + z), y) - 1))
    overpayment = annuity * y - x
    print(f'Your annuity payment = {annuity}!\nOverpayment = {overpayment}')


def calculate_credit_principal(x, y, z):
    principal = (x / ((z * math.pow((1 + z), y)) / (math.pow((1 + z), y) - 1)))
    overpayment = math.ceil(x * y - principal)
    print(f'Your credit principal = {int(principal)}!\nOverpayment = {overpayment}')


def calculate_n(x, y, z):
    no_of_payments = math.ceil(math.log((y / (y - z * x)), (z + 1)))
    overpayment = math.ceil(no_of_payments * y - x)
    years = no_of_payments // 12
    months = no_of_payments % 12
    if years < 1:
        print(f'You need {months} months to repay this credit!' if months > 1 else f'You need 1 month to repay this credit!')
    elif years == 1:
        if months == 0:
            print(f'You need 1 year to repay this credit!')
        elif months == 1:
            print(f'You need 1 year and one month to repay this credit!')
        elif months > 1:
            print(f'You need 1 year and {months} months to repay this credit!')
    elif years > 1:
        if months == 0:
            print(f'You need {years} years to repay this credit!')
        elif months == 1:
            print(f'You need {years} years and one month to repay this credit!')
        elif months > 1:
            print(
                f'You need {years} years and {months} months to repay this credit!')
    print(f'Overpayment = {overpayment}')


if len_error or no_type or type_error or diff_error or no_interest or neg_error:
    print('Incorrect parameters')
elif args.type == 'diff':
    p = args.principal
    n = args.periods
    i = args.interest / (12 * 100)
    calculate_differentiated_payment(p, n, i)
elif args.type == 'annuity':
    if args.payment is None:
        p = args.principal
        n = args.periods
        i = args.interest / (12 * 100)
        calculate_annuity(p, n, i)
    elif args.principal is None:
        a = args.payment
        n = args.periods
        i = args.interest / (12 * 100)
        calculate_credit_principal(a, n, i)
    elif args.periods is None:
        p = args.principal
        a = args.payment
        i = args.interest / (12 * 100)
        calculate_n(p, a, i)
