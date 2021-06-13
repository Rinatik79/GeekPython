# Hi dear Maria!

# Problem 1:
# class Date:
#
#     @classmethod
#     def date_converter(cls, string_date):
#         date_int_list = string_date.split("-")
#         for i in range(len(date_int_list)):
#             date_int_list[i] = int(date_int_list[i])
#
#         return date_int_list
#
#     @staticmethod
#     def date_validator(date_int_list):
#         if date_int_list[0] < 1 or date_int_list[0] > 31:
#             return "Entered date: " + str(date_int_list) + ". Day cannot be less then 1 or grater than 31!\n"
#         elif date_int_list[1] < 1 or date_int_list[1] > 12:
#             return "Entered date: " + str(date_int_list) + ". Month cannot be less then 1 or grater than 12!\n"
#         else:
#             return "Given date: " + str(date_int_list) + " is more or less correct.\n"
#
#
# date_list = Date.date_converter("07-10-2012")
# print(Date.date_validator(date_list))
#
# date_list = Date.date_converter("07-18-2012")
# print(Date.date_validator(date_list))

# Problem 2:
# class SafeDivision:
#
#     @staticmethod
#     def division(divisible, divisor):
#         result = 0
#         try:
#             result = divisible / divisor
#
#         except ZeroDivisionError:
#             print("Cannot divide by 0!")
#
#         else:
#             print(str(divisible) + " / " + str(divisor) + " = " + str(result))
#
#         finally:
#             print("See you later!\n")
#
# SafeDivision.division(15, 5)
# SafeDivision.division(12, 0)

# Problem 3:
# list_of_numbers = []
# answer = ""


# class Verifier:
#
#     @staticmethod
#     def verify(given_string):
#         out = given_string
#         try:
#             out = float(given_string)
#
#         except ValueError:
#             if given_string != "stop":
#                 return ("Wrong type!")
#
#         else:
#             return out
#
#
# while answer != "stop":
#     answer = input("Enter number please: ")
#     result = Verifier.verify(answer)
#
#     if result == "Wrong type!":
#         print(result)
#     elif result is None:
#         print(list_of_numbers)
#     else:
#         list_of_numbers.append(result)
#
# print("Bye!")

# Problem 4,5,6:

# current_warehouse_state = {"Printers": 0, "Scanners": 0, "Copiers": 0}
# current_division_state = []

class OfficeEquipmentWarehouse:
    current_warehouse_state = {"Printers": 0, "Scanners": 0, "Copiers": 0}
    current_division_state = []

    # def __init__(self):
    #     self.current_warehouse_state = {"Printers": 0, "Scanners": 0, "Copiers": 0}
    #     self.current_division_state = []

    @staticmethod
    def convert_to_int(given_string):
        out = given_string
        try:
            out = int(given_string)

        except ValueError:
            return "Enter int number please!"

        else:
            return out

    def division_with_name_index(self, division):
        for i in range(len(self.current_division_state)):
            if type(self.current_division_state[i].get(division)) == dict:
                return i

    def add_printers_to_warehouse(self, adding_qty):
        printers_to_add = OfficeEquipmentWarehouse.convert_to_int(adding_qty)
        if printers_to_add == "Enter int number please!":
            print(printers_to_add)

        else:
            self.current_warehouse_state["Printers"] += printers_to_add

    def add_scanners_to_warehouse(self, adding_qty):
        scanners_to_add = OfficeEquipmentWarehouse.convert_to_int(adding_qty)
        if scanners_to_add == "Enter int number please!":
            print(scanners_to_add)

        else:
            self.current_warehouse_state["Scanners"] += scanners_to_add

    def add_copiers_to_warehouse(self, adding_qty):
        copiers_to_add = OfficeEquipmentWarehouse.convert_to_int(adding_qty)
        if copiers_to_add == "Enter int number please!":
            print(copiers_to_add)

        else:
            self.current_warehouse_state["Copiers"] += copiers_to_add

    def send_printers_to_division(self, sending_qty, division):
        printers_to_send = OfficeEquipmentWarehouse.convert_to_int(sending_qty)
        if printers_to_send == "Enter int number please!":
            print(printers_to_send)

        if printers_to_send > self.current_warehouse_state.get("Printers"):
            print("Warehouse doesn't have asking qty: " + str(sending_qty))

        else:
            self.current_warehouse_state["Printers"] -= OfficeEquipmentWarehouse.convert_to_int(sending_qty)
            needed_division_position = self.division_with_name_index(division)
            if needed_division_position is None:
                division_to_add = {division:
                                       {"Printers": printers_to_send,
                                        "Scanners": 0,
                                        "Copiers": 0}
                                   }
                self.current_division_state.append(division_to_add)
            else:
                new_printers_qty = self.current_division_state[needed_division_position].get(division).get(
                    "Printers") + printers_to_send
                self.current_division_state[needed_division_position][division]["Printers"] = new_printers_qty

    def send_scanners_to_division(self, sending_qty, division):
        scanners_to_send = OfficeEquipmentWarehouse.convert_to_int(sending_qty)
        if scanners_to_send == "Enter int number please!":
            print(scanners_to_send)

        if scanners_to_send > self.current_warehouse_state.get("Scanners"):
            print("Warehouse doesn't have asking qty: " + str(sending_qty))

        else:
            self.current_warehouse_state["Scanners"] -= OfficeEquipmentWarehouse.convert_to_int(sending_qty)
            needed_division_position = self.division_with_name_index(division)
            if needed_division_position is None:
                division_to_add = {division:
                                       {"Printers": 0,
                                        "Scanners": scanners_to_send,
                                        "Copiers": 0}
                                   }
                self.current_division_state.append(division_to_add)
            else:
                new_scanners_qty = self.current_division_state[needed_division_position].get(division).get(
                    "Scanners") + scanners_to_send
                self.current_division_state[needed_division_position][division]["Scanners"] = new_scanners_qty

    def send_copiers_to_division(self, sending_qty, division):
        copiers_to_send = OfficeEquipmentWarehouse.convert_to_int(sending_qty)
        if copiers_to_send == "Enter int number please!":
            print(copiers_to_send)

        if copiers_to_send > self.current_warehouse_state.get("Copiers"):
            print("Warehouse doesn't have asking qty: " + str(sending_qty))

        else:
            self.current_warehouse_state["Copiers"] -= OfficeEquipmentWarehouse.convert_to_int(sending_qty)
            needed_division_position = self.division_with_name_index(division)
            if needed_division_position is None:
                division_to_add = {division:
                                       {"Printers": 0,
                                        "Scanners": 0,
                                        "Copiers": copiers_to_send}
                                   }
                self.current_division_state.append(division_to_add)
            else:
                new_copiers_qty = self.current_division_state[needed_division_position].get(division).get(
                    "Copiers") + copiers_to_send
                self.current_division_state[needed_division_position][division]["Copiers"] = new_copiers_qty


class OfficeEquipment(OfficeEquipmentWarehouse):
    pass


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Copier(OfficeEquipment):
    pass


class Division(OfficeEquipmentWarehouse):
    pass


warehouse = OfficeEquipmentWarehouse()
warehouse.add_printers_to_warehouse("11")
warehouse.add_scanners_to_warehouse("22")
warehouse.add_copiers_to_warehouse("33")
print(warehouse.current_warehouse_state)
warehouse.send_scanners_to_division("7", "IT")
warehouse.send_printers_to_division("8", "IT")
warehouse.send_scanners_to_division("7", "IT")
warehouse.send_copiers_to_division("2", "IT")
warehouse.send_copiers_to_division("1", "IT")
print(warehouse.current_division_state)
print(warehouse.current_warehouse_state)
