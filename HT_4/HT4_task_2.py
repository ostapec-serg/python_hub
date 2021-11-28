#Write the function <bank>, which works according to the following logic:
#the user makes a deposit of <a> units for a period of <years> years at <percents> interest
#(each year the deposit amount increases by this percentage, this money is added to the deposit
#amount and in next year they also accrue interest). The <percents> parameter is optional and has
#a default value of <10> (10%).
#The function must print and return the amount that will be on the account.

def bank(income, depo_years, per=10):
    sum_of_percent = []
    for _ in range(1, depo_years+1):
        perc = income / 100 * round(per, )
        sum_of_percent.append(perc)
        kapusta = income + perc
        income = round(kapusta, 2)
    return income, round(sum(sum_of_percent), 2)

money = float(input("Enter the investment amount:\n"))
deposit_years = int(input("Enter the number of years for which you want to invest:\n"))
percent_per_year = float(input("Enter interest rate: \n"))
final = bank(money, deposit_years, percent_per_year)


print(f"For {deposit_years} years you have USD {final[0]} on your bank account\n"
      f"Investment amount USD {money} \n"
      f"Calculated interest for {deposit_years} years USD {final[1]}")
