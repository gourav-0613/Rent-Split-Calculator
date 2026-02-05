
# clculating Electricity amount for month
def cal_electricity_bill(unit, charge):
    return float(unit*charge)

# calculate total expenses
def cal_total_expense(rent,food,electricity,waterbill,grocery,maintenance):
    return float(
    rent
    +food
    +electricity
    +waterbill
    +grocery
    +maintenance
    )



def main():
    while True:

        print("---------------------------------")
        print("-----### RENT CALCULATOR ###-----")
        print("---------------------------------")

        try:
        
            total_rent = float(input("Enter Total Rent:-"))
            total_food_order = float(input("Enter Total Money of Food order in Month:-"))
            electric_unit = float(input("Enter total unit of the month of meter:-"))
            charge_per_unit =  float(input("Enter charge for per unit of Elecricity:-"))
            water_bill = float(input("enter the amount of water bill:-"))
            total_grocery_amount = float(input("enter the amount of Grocery bill:-"))
            maintenance = float(input("Maintenance Amount:-"))


            number_of_people = int(input("How Many Number of People Have to contrie for the Rent:-"))
            if(number_of_people <= 0):

                raise ZeroDivisionError("Number of people must be greater than zero:-")
                
            
            total_electric_bill = cal_electricity_bill(
                electric_unit,
                charge_per_unit)


            total_expense = cal_total_expense(
                total_rent,
                total_food_order,
                total_electric_bill,
                water_bill,
                total_grocery_amount,
                maintenance
            )

            # calculate Per person rent by dividing total expense 
            share_per_person = total_expense / number_of_people
            print("-----------------------------------")
            print(f"Total Expense: {total_expense:.2f}")
            print(f"Total Rent for each Person for this  month is: {share_per_person:.2f}")
            print("-----------------------------------")
            break 

        except ValueError:
            print(" please enter only numeric values")
            print(" please start again:")


        except ZeroDivisionError as e:
            print(f" Error:{e}")

        except Exception as e:
            print(f" Unexpected error occured: {e}")

if __name__ == "__main__":
    main()