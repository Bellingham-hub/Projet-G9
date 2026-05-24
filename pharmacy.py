# =============================================================================
# pharmacy.py — Pharmacy Stock Management
# =============================================================================
# File Structure:
#   PART 1 — Foundations     : input and validation functions
#   PART 2 — Inheritance     : classes Medicine and PrescriptionDrug
#   PART 3 — Magic methods   : __str__ and __eq__
#   PART 4 — Decorators     : @staticmethod
#   MAIN PROGRAM            : main()
# =============================================================================


# =============================================================================
# PART 1 — FOUNDATIONS
# =============================================================================

def get_text(message):
    
    # Ask for a non-empty string input and check if the input is empty
    while True:
        value = input(message).strip()
        if not value:
            print(" Error: this field cannot be empty. Please try again\n")
        else:
            return value  


def get_integer(message):
    # Ask for a positive integer input
    
    while True:
        try:
            value = int(input(message))  
            if value < 0:
                print("Invalid Input: the number must be positive or zero. Please try again.\n")
            else:
                return value  
        except ValueError:
            print(" Error: please enter an integer Try again.\n")


def get_float(message):
    
    # Ask for a positive float input
   
    while True:
        try:
            value = float(input(message))  
            if value <= 0:
                print("Invalid Input: the price must be positive. Please try again.\n")
            else:
                return value 
        except ValueError:
            print(" Error: please enter a valid number. Try again.\n")


def get_boolean(message):
    

    
    
    while True:
        value = input(message).strip().lower()
        if value == "yes":
            return True   
        elif value == "no":
            return False  
        else:
            print("Please answer with 'yes' or 'no'. Try again.\n")


def get_choice(message, min_val, max_val):
    
    # Ask the user for a choice between min_val and max_val (inclusive). Validates that the input is an integer within the specified range.
    
    while True:
        try:
            value = int(input(message))
            if value < min_val or value > max_val:
                print(f"Invalid Input: choose between {min_val} and {max_val}. Please try again.\n")
            else:
                return value  
        except ValueError:
            print(f"Error: Enter a number between {min_val} and {max_val}. Please try again.\n")


def get_date(message):
    from datetime import datetime
    while True:
        value = input(message).strip()
        try:
            datetime.strptime(value, "%d/%m/%Y")
            return value
        except ValueError:
            print("Error: Invalid date format. Please use DD/MM/YYYY.\n")


def get_doctor_name(message):
    while True:
        value = input(message).strip()
        if not value:
            print("Error: this field cannot be empty. Please try again\n")
            continue
        if all(c.isalpha() or c.isspace() or c == '-' or c == '.' for c in value):
            return value
        else:
            print("Error: Doctor name must contain only letters, spaces, hyphens, or periods.\n")


def get_supply_mode(message):
    valid_modes = ["wholesaler", "lab", "donation"]
    while True:
        value = input(message).strip()
        if value.lower() in valid_modes:
            return value.capitalize()
        else:
            print("Error: Supply mode must be Wholesaler, Lab, or Donation.\n")


def get_supplier_name(message):
    while True:
        value = input(message).strip()
        if not value:
            print("Error: this field cannot be empty. Please try again\n")
            continue
        if all(c.isalpha() or c.isspace() or c in "-.&" for c in value):
            return value
        else:
            print("Error: Supplier name contains invalid characters. Use letters, spaces, hyphens, periods or ampersands.\n")


# =============================================================================
# PART 2 — INHERITANCE
# Parent class: Medicine
# Child class : PrescriptionDrug
#
# PART 3 — MAGIC METHODS
# __str__ : defines what is displayed with print(object)
# __eq__  : defines comparison with object1 == object2
#
# PART 4 — DECORATORS
# @staticmethod : method that belongs to the class but not to an instance
# =============================================================================

class Medicine:
    
    # PART 2 — Parent class: Represents a classic drug sold without a prescription
    


    def __init__(self, medicine_name, unit_price, incoming_quantity,outgoing_quantity, minimum_threshold, is_generic,entry_date, expiry_date, lot_number,
                 supply_mode, supplier_name):
        
        self.medicine_name= medicine_name      
        self.entry_date= entry_date        
        self.expiry_date= expiry_date        
        self.lot_number= lot_number         
        self.supply_mode= supply_mode        
        self.supplier_name=supplier_name      

        self.unit_price=unit_price         
        self.incoming_quantity=incoming_quantity  
        self.outgoing_quantity=outgoing_quantity  
        self.minimum_threshold=minimum_threshold  
        self.is_generic=is_generic         

    # ─────────────────────────────────────────────────────────────────────────
    # PART 3 — MAGIC METHOD: __str__
    # ─────────────────────────────────────────────────────────────────────────
    # Called automatically by print(medicine)
    # Without __str__ : Python displays <pharmacy.Medicine object at 0x...>
    # With __str__ : Python displays our formatted sheet
    # ─────────────────────────────────────────────────────────────────────────

    def __str__(self):
        """
        PART 3 — Magic method __str__
        Returns a readable record of the medication.
        Called automatically by print(medicine)
        """
        stock=self.calculate_available_stock()
        generic_label="yes" if self.is_generic else "no"
        stock_alert= " Alert" if stock <= self.minimum_threshold else " OK"

        return (
            f"\n{'─' * 50}\n"
            " MEDICATION SHEET\n"
            f"{'─' * 50}\n"
            f"Name:{self.medicine_name}\n"
            f"Batch number:{self.lot_number}\n"
            f"Supplier:{self.supplier_name}\n"
            f"Supply mode:{self.supply_mode}\n"
            f"Unit price:{self.unit_price:.0f} FCFA\n"
            f"Generic:{generic_label}\n"
            f"Entry date:{self.entry_date}\n"
            f"Expiry date:{self.expiry_date}\n"
            f"Available stock : {stock} units{stock_alert}\n"
            f"{'─' * 50}"
        )

    # ─────────────────────────────────────────────────────────────────────────
    # PART 3 — MAGIC METHOD: __eq__
    # ─────────────────────────────────────────────────────────────────────────
    # Called automatically by medicine1 == medicine2
    # Without __eq__ : Python compares memory addresses (always False)
    # With __eq__ : we compare by lot number to detect duplicates
    # ─────────────────────────────────────────────────────────────────────────

    def __eq__(self, other):
        """
        PART 3 — Magic method __eq__
        Compares two medicines by their batch number.
        Automatically called by medicine1 == medicine2
        """
        if not isinstance(other, Medicine):
            return False
        return self.lot_number == other.lot_number

    def calculate_available_stock(self):
        # Available stock = Incoming quantity - Outgoing quantity
        
        return self.incoming_quantity - self.outgoing_quantity  

    def calculate_stock_value(self):
        
        # Stock value = Unit price × Available stock
        
        stock = self.calculate_available_stock()
        return self.unit_price * stock  

    # ─────────────────────────────────────────────────────────────────────────
    # PART 4 — DECORATOR: @staticmethod
    

    @staticmethod
    def calculate_storage_duration(entry_date, expiry_date):
        
        # PART 4 — Decorator @staticmethod, Duration = Expiration date - Entry date (in days)
        
        from datetime import datetime
        try:
            entry     = datetime.strptime(entry_date,  "%d/%m/%Y")
            expiry = datetime.strptime(expiry_date, "%d/%m/%Y")
            
            return (expiry - entry).days  
        except ValueError:
            return -1

    def check_alert(self):
        """
        Check the critical stock and expiration alerts. Return a list of alert messages.
        """
        from datetime import datetime
        alerts = []

        
        stock = self.calculate_available_stock()
        critical_stock = stock <= self.minimum_threshold  
        if critical_stock:
            alerts.append(
                f"   STOCK LOW: {stock} units "
                f"(minimum threshold : {self.minimum_threshold})"
            )

        
        try:
            expiry_datetime = datetime.strptime(self.expiry_date, "%d/%m/%Y")
            today = datetime.today()
            remaining_days = (expiry_datetime - today).days
            if remaining_days < 0:
                alerts.append(f"EXPIRED MEDICATION since {abs(remaining_days)} days !")
            elif remaining_days <= 90:
                alerts.append(f"NEAR EXPIRATION:: {remaining_days} days remaining")
        except ValueError:
            pass

        return alerts


# =============================================================================
# PART 2 — CHILD CLASS: PrescriptionDrug
# =============================================================================
# Inherits from Medicine via: class PrescriptionDrug(Medicine)
# =============================================================================

class PrescriptionDrug(Medicine):
    # PART 2 — Child class
    # Inherits from Medicine and adds prescription information
    

    def __init__(self, medicine_name, unit_price, incoming_quantity,
                 outgoing_quantity, minimum_threshold, is_generic,
                 entry_date, expiry_date, lot_number,
                 supply_mode, supplier_name,
                 doctor_name, treatment_duration, is_renewable):
        

        
        super().__init__(
            medicine_name, unit_price, incoming_quantity,
            outgoing_quantity, minimum_threshold, is_generic,
            entry_date, expiry_date, lot_number,
            supply_mode, supplier_name
        )

        
        self.doctor_name=doctor_name         
        self.treatment_duration=treatment_duration  
        self.is_renewable=is_renewable        

    # ─────────────────────────────────────────────────────────────────────────
    # PART 3 — MAGIC METHOD: __str__ (overridden)
    # ─────────────────────────────────────────────────────────────────────────
    # We override __str__ from parent to add prescription information.
    # super().__str__() calls the parent's __str__ to reuse the sheet.
    # ─────────────────────────────────────────────────────────────────────────

    def __str__(self):
        """
        PART 3 — Overridden magic method __str__
        Displays the parent's record + prescription information
        """
        parent_sheet= super().__str__()
        renewable_label = "yes" if self.is_renewable else "No"

        prescription_form = (
            f"\n{'─' * 50}\n"
            f"PRESCRIPTION INFORMATION\n"
            f"{'─' * 50}\n"
            f"  Doctor         : Dr. {self.doctor_name}\n"
            f"  Treatment Duration : {self.treatment_duration} days\n"
            f"  Renewable     : {renewable_label}\n"
            f"{'─' * 50}"
        )

        return parent_sheet + prescription_form


# =============================================================================
# DATA COLLECTION FUNCTIONS
# Use the functions from Part 1 to collect the 14 inputs
# =============================================================================

def collect_medicine():
    
    # Collect the  inputs to create a Medicine. 
    
    print("\nREGISTRATION — CLASSIC MEDICINE")
    print("─" * 45)

    medicine_name=get_text("Medicine name: ")        
    unit_price=get_float("Unit price: ")       
    incoming_quantity=get_integer("Incoming quantity: ")     
    outgoing_quantity=get_integer("Outgoing quantity: ")     

    
    while outgoing_quantity > incoming_quantity:
        print(f"Error: outgoing quantity ({outgoing_quantity}) > incoming ({incoming_quantity}).\n")
        outgoing_quantity = get_integer("  outgoing quantity: ")

    minimum_threshold = get_integer("minimum alert threshold: ")    
    is_generic= get_boolean("Generic? (yes/no): ")    
    entry_date= get_date("Entry date (DD/MM/YYYY): ")       
    expiry_date=get_date("Expiry date (DD/MM/YYYY): ")       
    lot_number=get_text(" Batch number : ")       
    supply_mode=get_supply_mode(" Supply mode (Wholesaler/Lab/Donation) : ")  
    supplier_name=get_supplier_name("Supplier name : ")       

    return Medicine(
        medicine_name, unit_price, incoming_quantity,
        outgoing_quantity, minimum_threshold, is_generic,
        entry_date, expiry_date, lot_number,
        supply_mode, supplier_name
    )


def collect_prescription_drug():
    """
    Collect inputs to create a PrescriptionDrug. Return an instance of PrescriptionDrug
    """
    print("\n REGISTRATION — PRESCRIPTION MEDICINE")
    print("─" * 45)

    medicine_name= get_text("Medicine name: ")        
    unit_price= get_float("  Unit price (FCFA): ")       
    incoming_quantity= get_integer("Incoming quantity : ")     
    outgoing_quantity= get_integer("Outgoing quantity : ")     

    while outgoing_quantity > incoming_quantity:
        print(f"Error: outgoing quantity ({outgoing_quantity}) > incoming ({incoming_quantity}).\n")
        outgoing_quantity = get_integer("  Outgoing quantity: ")

    minimum_threshold = get_integer("Minimum alert threshold: ")    
    is_generic= get_boolean("Generic? (yes/no): ")    
    entry_date = get_date("Entry date (DD/MM/YYYY): ")       
    expiry_date= get_date("Expiry date (DD/MM/YYYY): ")       
    lot_number= get_text("Batch number: ")       
    supply_mode= get_supply_mode("Supply mode (Wholesaler/Lab/Donation): ")  
    supplier_name= get_supplier_name("Supplier name: ")       

    print("\nPrescription information:")
    doctor_name= get_doctor_name("Doctor name: ")      
    treatment_duration= get_integer("Treatment duration (days): ")   
    is_renewable= get_boolean("Renewable? (yes/no): ")   

    return PrescriptionDrug(
        medicine_name, unit_price, incoming_quantity,
        outgoing_quantity, minimum_threshold, is_generic,
        entry_date, expiry_date, lot_number,
        supply_mode, supplier_name,
        doctor_name, treatment_duration, is_renewable
    )


# =============================================================================
# DISPLAY FUNCTIONS
# =============================================================================

def display_stock_report(medicine):
    
    # Display stock report
    
    
    available_stock = medicine.calculate_available_stock()  
    stock_value = medicine.calculate_stock_value()     
    critical_stock = available_stock <= medicine.minimum_threshold  

    print(f"\n STOCK — {medicine.medicine_name}")
    print(f"  {'─' * 43}")
    print(f"Incoming quantity : {medicine.incoming_quantity} units")
    print(f"Outgoing quantity: {medicine.outgoing_quantity} units")
    print(f"Available stock : {available_stock} units ", end="")
    print("ALERT" if critical_stock else "OK")
    print(f"Value of stock: {stock_value:,.0f} FCFA")
    print(f"  {'─' * 43}")


def display_storage_duration(medicine):
    duration = Medicine.calculate_storage_duration(medicine.entry_date, medicine.expiry_date)

    print(f"Storage duration : ", end="")
    if duration < 0:
        print("Invalid format")
    elif duration <= 90:
        print(f"{duration} days (EXPIRATION NEAR)")
    else:
        print(f"{duration} days OK")


def display_alert(medicines):
    
    print("\n" + "=" * 55)
    print("  SYSTEM ALERTS")
    print("=" * 55)

    has_alerts = False  

    for medicine in medicines:
        alerts = medicine.check_alert()
        if alerts:
            has_alerts = True
            print(f"\n  Medicine: {medicine.medicine_name}")
            for alert in alerts:
                print(alert)

    if not has_alerts:
        print("No alerts — all stocks are in order")

    print("=" * 55)


def display_final_report(medicines):
    
  
    total_value = sum(med.calculate_stock_value() for med in medicines)

    print("\n")
    print("╔" + "═" * 53 + "╗")
    print("║" + "  FINAL REPORT  " + "║")
    print("╠" + "═" * 53 + "╣")
    print(f"║  Medicines registered : {len(medicines):<26}║")
    print("╠" + "═" * 53 + "╣")

    for i, med in enumerate(medicines):

        stock = med.calculate_available_stock()
        value = med.calculate_stock_value()
        duration = Medicine.calculate_storage_duration(med.entry_date, med.expiry_date)

        generic_label = "Yes" if med.is_generic else "No"
        stock_alert = " ALERT" if stock <= med.minimum_threshold else " OK"
        duration_alert = (" EXPIRED" if duration < 0
                          else " NEAR" if duration <= 90
                          else " OK")

        print("║" + "─" * 53 + "║")
        print(f"║  MEDICINE {i + 1:<42}║")
        print("║" + "─" * 53 + "║")
        print(f"║  Name: {med.medicine_name:<32}║")
        print(f"║  Lot Number: {med.lot_number:<32}║")
        print(f"║  Supplier: {med.supplier_name:<32}║")
        print(f"║  Supply Mode:{med.supply_mode:<32}║")
        print(f"║  Unit Price : {str(int(med.unit_price)) + ' FCFA':<32}║")
        print(f"║  Generic : {generic_label:<32}║")
        print(f"║  Entry Date: {med.entry_date:<32}║")
        print(f"║  Expiry Date: {med.expiry_date:<32}║")
        print("║" + "─" * 53 + "║")
        print(f"║  Incoming Qty : {str(med.incoming_quantity) + ' units':<32}║")
        print(f"║  Outgoing Qty: {str(med.outgoing_quantity) + ' units':<32}║")
        print(f"║  Available Stock : {str(stock) + ' units' + stock_alert:<32}║")
        print(f"║  Stock Value: {str(int(value)) + ' FCFA':<32}║")
        print(f"║  Storage Duration: {str(duration) + ' days' + duration_alert:<32}║")

        
        if isinstance(med, PrescriptionDrug):
            renewable_label = "yes" if med.is_renewable else "no"
            print("║" + "─" * 53 + "║")
            print(f"║  Prescription{'':<39}║")
            print(f"║  Doctor           : {'Dr. ' + med.doctor_name:<32}║")
            print(f"║  Treatment Duration : {str(med.treatment_duration) + ' days':<32}║")
            print(f"║  Renewable        : {renewable_label:<32}║")

    print("╠" + "═" * 53 + "╣")
    print(f"║  TOTAL STOCK VALUE : {str(int(total_value)) + ' FCFA':<31}║")
    print("╚" + "═" * 53 + "╝")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    # Program entry point

    
    print("=" * 55)
    print("       PHARMACY— STOCK MANAGEMENT SYSTEM")
    print("=" * 55)
    print(f"Welcome to the stock management system.")
    print(f"Register your medications and monitor your inventory.")
    print("=" * 55)
    print()
    print("Two types of medications can be registered:")
    print("    1.  Generic medication — sold without prescription")
    print("    2.  Prescription medication — prescribed by a doctor")
    print("=" * 55)
    print()

    # ── Number of medications to register ──────────────────────────────────
    print("  How many medications would you like to register?")
    number = 0
    while number < 1 or number > 10:
        try:
            number = int(input("  Number of medications (1-10) : "))
            if number < 1 or number > 10:
                print("Error: enter a number between 1 and 10\n")
        except ValueError:
            print("Error: enter an integer\n")

    
    medicines = []  
    for i in range(number):
        print(f"\n{'═' * 55}")
        print(f"  MEDICINE {i + 1} of {number}")
        print(f"{'═' * 55}")
        print("What type of medicine?")
        print("1 — Classic medicine (without prescription)")
        print("2 — Prescription medicine")

        choice = get_choice("  Your choice (1 or 2) : ", 1, 2)

        if choice == 1:
            med = collect_medicine()             
        else:
            med = collect_prescription_drug() 
        
        print("\n   Medicine registered!")
        print(med)

        medicines.append(med)

   
    print("\n" + "=" * 55)
    print("  STOCK REPORT")
    print("=" * 55)

    for med in medicines:
        display_stock_report(med)    
        display_storage_duration(med) 

   
    if len(medicines) >= 2:
        print("\n" + "─" * 55)
        print("COMPARISON OF MEDICATIONS (via __eq__)")
        print("─" * 55)
        # Call of __eq__ via the == operator — PART 3
        are_identical = (medicines[0] == medicines[1])
        if are_identical:
            print(f"Same batch number detected — possible duplicate!")
        else:
            print(f"{medicines[0].medicine_name} and {medicines[1].medicine_name}")
            print(f"     are two distinct medications.")
        print("─" * 55)

    # ── Alerts ────────────────────────────────────────────────────────────────
    display_alert(medicines)

    # ── Final Report ──────────────────────────────────────────────────────────
    display_final_report(medicines)

    print("\n  Thank you for using the stock management system.")
    print("  See you soon !\n")



if __name__ == "__main__":
    main()
