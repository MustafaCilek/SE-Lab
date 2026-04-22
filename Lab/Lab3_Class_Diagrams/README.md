------------------------------
ATM System Class Diagram

This diagram maps the structural relationships within a banking system.

    A Bank (which stores its name and customer count) can add accounts and authorize cards. It is associated with multiple ATMs, which track their physical location and available cash, and handle verifying PINs and dispensing the money.

    A Bank is composed of zero or more Accounts. Each Account holds an account number and current balance, and allows users to make deposits and withdrawals.

    Each Account is composed of zero or more Transactions. These record a unique transaction ID and timestamp, and contain logic to process the request or check its status.

    A Withdrawal represents a specific subclass of a Transaction. It inherits the basic transaction details but adds specific data like the withdrawal amount and the ID of the ATM used, along with actions to actually dispense the cash and check withdrawal limits.
------------------------------


------------------------------
Medical Clinic System Class Diagram

This diagram outlines the entities in a medical setting.

    Both Patient and Doctor inherit from a common Person class. This means they both share basic details (like a full name and contact number) and standard actions (like retrieving details or updating contact info).

    A Patient who also holds an insurance ID and blood type, and can request appointments or view their history is linked to zero or more Medical Records.

    A Doctor identified by a license number and specialization, who can prescribe medication and record vitals interacts with multiple Medical Records.

    These Medical Records store a unique record ID and a diagnosis, and allow staff to add clinical notes or update treatment plans.

    Finally, a Doctor operates within a Clinic, which holds its own name and address, and manages the logistics of scheduling appointments and assigning doctors to patients.
------------------------------


------------------------------
Car Insurance Class Diagram

This diagram defines the core data structures for managing auto insurance.

    An Insurance Company (tracking its name and phone number) manages the system by issuing new policies and processing claims.

    The company issues multiple Policies, which store a policy number and coverage limit, and include actions to renew the term or check eligibility.

    A Customer identified by a customer ID and driving license, who can file claims and pay premiums can hold multiple Policies.

    A Customer can also own multiple Vehicles, which track their VIN and model year, and allow the system to fetch or update the mileage.

    Finally, a single Policy can be tied to multiple Claims. These claims log a claim ID and its current status, and contain the logic to either approve a payout or reject the claim.