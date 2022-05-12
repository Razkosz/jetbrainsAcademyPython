import math
import argparse

parser = argparse.ArgumentParser(description="Loan Calculator. You can calculate annuity or differentiate loan payment")

# parameters definition
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

# list of used parameters: 0 type, 1 loan, 2 monthly payment, 3 months, 4 monthly interest rate
p = [args.type,
     float(args.principal) if args.principal is not None else None,
     float(args.payment) if args.payment is not None else None,
     int(args.periods) if args.periods is not None else None,
     float(args.interest) / 100 / 12 if args.interest is not None else None]
# print(p)

# check if there are exactly 4 parameters
countNone = 0
for x in p:
    if x is None:
        countNone += 1
if countNone != 1:
    print("Incorrect parameters")
# choosing between calc types
elif args.type == "diff":
    # differentiate calc
    if not args.payment:
        overall_payment = 0
        for m in range(p[3]):
            payment = math.ceil((p[1] / p[3]) + p[4] * (p[1] - ((p[1] * m) / p[3])))
            overall_payment += payment
            print("Month {}: payment is {}".format(m + 1, payment))
        print("Overpayment = {}".format(int(overall_payment - p[1])))
    else:
        print("Incorrect parameters")
elif args.type == "annuity":
    if not args.periods:
        loan = p[1]
        m_pay = p[2]
        i_rate = p[4]
        months = math.ceil(math.log(m_pay / (m_pay - i_rate * loan), 1 + i_rate))
        years = math.floor(months / 12)
        month = months % 12
        op = int(m_pay * months - loan)
        if years == 0:
            print("It will take {m}{m_pl} to repay this loan".format(m=month,
                                                                     m_pl=" month" if month == 1 else " months"))
        elif month == 0:
            print("It will take {y}{y_pl} to repay this loan".format(y=years,
                                                                     y_pl=" year" if years == 1 else " years"))
        else:
            print("It will take {y}{y_pl}{m}{m_pl} to repay this loan".format(y=years,
                                                                              y_pl=(" year " if years == 1 else " years "),
                                                                              m=month,
                                                                              m_pl=(" month" if month == 1 else " months")))
        print(f"Overpayment = {op}")
    # calc annuity payment
    elif not args.payment:
        loan = p[1]
        months = p[3]
        i_rate = p[4]
        payment = math.ceil(loan * ((i_rate * math.pow((1 + i_rate), months)) / (math.pow((1 + i_rate), months) - 1)))
        op = int(payment * months - loan)
        print(f"Your annuity payment = {payment}")
        print(f"Overpayment = {op}")
    # calc loan principal
    elif not args.principal:
        payment = p[2]
        months = p[3]
        i_rate = p[4]
        loan = math.ceil(payment / ((i_rate * math.pow(1 + i_rate, months)) / (math.pow(1 + i_rate, months) - 1)))
        op = int(payment * months - loan)
        print(f"Your loan principal = {loan}!")
        print(f"Overpayment = {op}")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
