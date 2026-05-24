\# Pharmacy — Stock Management System

\*\*PRG1406 — Advanced Programming (Python and C)\*\*

Institut de Technologie du Burkina Faso · May 2026



\---



\## Project Description



This program simulates a \*\*pharmacy stock management system\*\*. It allows users to register medications (classic or prescription-based), calculate financial values and storage durations, and automatically generate alerts for critical stock levels or upcoming expiration dates. The user interacts entirely through the terminal.



\---



\## Requirements



\- \*\*Python 3.8 or higher\*\*

\- No external libraries required (only the standard `datetime` module)



\---



\## How to Run



```bash

python pharmacy.py

```



\---



\## Program Flow



1\. \*\*Welcome screen\*\* : the program displays an introduction message

2\. \*\*Number of medications\*\* : the user enters how many medications to register (between 1 and 10)

3\. \*\*Medication entry\*\* : for each medication, the user selects the type and fills in the fields

4\. \*\*Stock report\*\* : displays stock levels and storage durations

5\. \*\*Comparison\*\* : if 2 or more medications are registered, they are compared by batch number (`\_\_eq\_\_`)

6\. \*\*System alerts\*\* : critical stock and near-expiration warnings

7\. \*\*Final report\*\* : complete summary table with total stock value



\---



\## Example Session



```

=======================================================

&#x20;      PHARMACY— STOCK MANAGEMENT SYSTEM

=======================================================

Welcome to the stock management system.

Register your medications and monitor your inventory.



&#x20; How many medications would you like to register?

&#x20; Number of medications (1-10) : 2



═══════════════════════════════════════════════════════

&#x20; MEDICINE 1 of 2

═══════════════════════════════════════════════════════

What type of medicine?

1 — Classic medicine (without prescription)

2 — Prescription medicine

&#x20; Your choice (1 or 2) : 1



REGISTRATION — CLASSIC MEDICINE

─────────────────────────────────────────────

Medicine name: Paracetamol

Unit price: 500

Incoming quantity: 100

Outgoing quantity: 80

minimum alert threshold: 15

Generic? (yes/no): yes

Entry date (DD/MM/YYYY): 01/01/2025

Expiry date (DD/MM/YYYY): 01/01/2027

&#x20;Batch number : LOT-2025-001

&#x20;Supply mode (Wholesaler/Lab/Donation) : wholesaler

Supplier name : Laborex

```



\---



\## Input Fields (14 inputs)



| # | Field | Type | Validation |

|---|-------|------|------------|

| 1 | Medicine name | str | Cannot be empty |

| 2 | Unit price (FCFA) | float | > 0 |

| 3 | Incoming quantity | int | ≥ 0 |

| 4 | Outgoing quantity | int | ≤ incoming quantity |

| 5 | Minimum alert threshold | int | ≥ 0 |

| 6 | Generic? (yes/no) | bool | "yes" or "no" only |

| 7 | Entry date | str | DD/MM/YYYY format |

| 8 | Expiry date | str | DD/MM/YYYY format |

| 9 | Batch number | str | Cannot be empty |

| 10 | Supply mode | str | wholesaler / lab / donation |

| 11 | Supplier name | str | Letters, spaces, hyphens, \& |

| 12 | Doctor name \*(prescription only)\* | str | Letters, spaces, hyphens, periods |

| 13 | Treatment duration \*(prescription only)\* | int | ≥ 0 |

| 14 | Renewable? \*(prescription only)\* | bool | "yes" or "no" only |



> Inputs 12, 13, and 14 are only asked for prescription medications.



\---



\## Code Structure



The project is contained in a single file: `pharmacy.py`, organized into 4 parts.



\### Part 1 — Input \& Validation Functions



Reusable utility functions that collect user input safely (`while` loop + `try/except`):



| Function | Role |

|----------|------|

| `get\_text(message)` | Non-empty text input |

| `get\_integer(message)` | Positive or zero integer input |

| `get\_float(message)` | Positive decimal input |

| `get\_boolean(message)` | yes/no input → True/False |

| `get\_choice(message, min, max)` | Numeric choice within a range |

| `get\_date(message)` | Date in DD/MM/YYYY format |

| `get\_supply\_mode(message)` | Controlled supply mode input |

| `get\_doctor\_name(message)` | Doctor name (valid characters only) |

| `get\_supplier\_name(message)` | Supplier name (valid characters only) |



\---



\### Part 2 — Inheritance (Classes)



\#### Parent class: `Medicine`



Represents a classic medication. It has 11 attributes:



```

medicine\_name, unit\_price, incoming\_quantity, outgoing\_quantity,

minimum\_threshold, is\_generic, entry\_date, expiry\_date,

lot\_number, supply\_mode, supplier\_name

```



\#### Child class: `PrescriptionDrug` (inherits from `Medicine`)



Represents a prescription medication. It calls `super().\_\_init\_\_()` to inherit the parent's 11 attributes, then adds 3 child-specific attributes:



```

doctor\_name, treatment\_duration, is\_renewable

```



\---



\### Part 3 — Magic Methods



| Method | Class | Triggered by | Role |

|--------|-------|--------------|------|

| `\_\_str\_\_` | `Medicine` | `print(med)` | Displays the formatted medication sheet |

| `\_\_str\_\_` | `PrescriptionDrug` | `print(med)` | Parent sheet + prescription information |

| `\_\_eq\_\_` | `Medicine` | `med1 == med2` | Compares two medications by batch number (duplicate detection) |



\---



\### Part 4 — `@staticmethod` Decorator



```python

@staticmethod

Medicine.calculate\_storage\_duration(entry\_date, expiry\_date)

```



Calculates the number of days between the entry date and the expiry date. This method does not rely on any instance attribute — it can be called directly on the class without creating an object.



\---



\## Automatic Calculations



| # | Calculation | Formula |

|---|-------------|---------|

| 1 | Available stock | `incoming quantity − outgoing quantity` |

| 2 | Total stock value | `unit price × available stock` |

| 3 | Storage duration | `expiry date − entry date` (in days) |



\---



\## Automatic Alerts



\- \*\*Critical stock\*\* : available stock ≤ minimum threshold

\- \*\*Near expiration\*\* : fewer than 90 days before expiry date

\- \*\*Expired medication\*\* : expiry date has already passed



\---



\## Example Final Report



```

╔═════════════════════════════════════════════════════╗

║              FINAL REPORT                           ║

╠═════════════════════════════════════════════════════╣

║  Medicines registered : 2                           ║

╠═════════════════════════════════════════════════════╣

║─────────────────────────────────────────────────────║

║  MEDICINE 1                                         ║

║─────────────────────────────────────────────────────║

║  Name: Paracetamol                                  ║

║  Lot Number: LOT-2025-001                           ║

║  Supplier: Laborex                                  ║

║  Unit Price : 500 FCFA                              ║

║  Generic : Yes                                      ║

║  Available Stock : 20 units  OK                     ║

║  Stock Value: 10000 FCFA                            ║

║  Storage Duration: 730 days OK                      ║

╠═════════════════════════════════════════════════════╣

║  TOTAL STOCK VALUE : 10000 FCFA                     ║

╚═════════════════════════════════════════════════════╝

```



\---



\## Course Requirements Covered



| Requirement | Implemented | Where |

|-------------|-------------|-------|

| 4 types (str, int, float, bool) | ✅ | Class attributes + inputs |

| 10+ inputs with type conversion | ✅ | 14 inputs, all validated |

| 3+ arithmetic expressions | ✅ | Stock, value, storage duration |

| `while` + `try/except` validation | ✅ | All input functions |

| F-strings + summary screen | ✅ | Complete final report |

| Parent class + child class | ✅ | `Medicine` → `PrescriptionDrug` |

| `super().\_\_init\_\_()` | ✅ | Inside `PrescriptionDrug.\_\_init\_\_` |

| Child-specific attribute | ✅ | `doctor\_name`, `treatment\_duration`, `is\_renewable` |

| `\_\_str\_\_` (magic method) | ✅ | `Medicine` and `PrescriptionDrug` |

| `\_\_eq\_\_` (magic method) | ✅ | Comparison by batch number |

| `@staticmethod` (decorator) | ✅ | `calculate\_storage\_duration()` |



