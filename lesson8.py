# Hi dear Maria!

# Problem 1:
class Date:

    @classmethod
    def date_converter(cls, string_date):
        date_int_list = string_date.split("-")
        for i in range(len(date_int_list)):
            date_int_list[i] = int(date_int_list[i])

        return date_int_list

    @staticmethod
    def date_validator(date_int_list):
        if date_int_list[0] < 1 or date_int_list[0] > 31:
            return "Entered date: " + str(date_int_list) + ". Day cannot be less then 1 or grater than 31!\n"
        elif date_int_list[1] < 1 or date_int_list[1] > 12:
            return "Entered date: " + str(date_int_list) + ". Month cannot be less then 1 or grater than 12!\n"
        else:
            return "Given date: " + str(date_int_list) + " is more or less correct.\n"


date_list = Date.date_converter("07-10-2012")
print(Date.date_validator(date_list))

date_list = Date.date_converter("07-18-2012")
print(Date.date_validator(date_list))

# Problem 2:
class SafeDivision:

    @staticmethod
    def division(divisible, divisor):
        result = 0
        try:
            result = divisible / divisor

        except ZeroDivisionError:
            print("Cannot divide by 0!")

        else:
            print(str(divisible) + " / " + str(divisor) + " = " + str(result))

        finally:
            print("See you later!\n")

SafeDivision.division(15, 5)
SafeDivision.division(12, 0)