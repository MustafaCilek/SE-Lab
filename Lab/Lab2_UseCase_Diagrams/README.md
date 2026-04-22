------------------------------
ATM System

The ATM system outlines the interactions between a Customer and the system's Server.

    The Customer can initiate transactions to Deposit Cash , Check Balance , and Withdraw Cash.

    These primary actions require interactions with the Server, which manages the Print Receipt and Validate PIN  functions.

    The transactions can optionally be extended to Print Receipt.
------------------------------


------------------------------
Medical Clinic System

The Medical Clinic System  maps out the processes for patients and clinic staff.

    A Patient can Schedule Appointment and View Medical History.

    A Receptionist is also involved in the Schedule Appointment process.

    A Doctor interacts with the system to View Medical History , Update Patient Record , and Write Prescription.

    An external Insurance actor handles the Authorize Insurance use case , which can optionally extend to the Update Patient Record process.
------------------------------

	
------------------------------
Car Insurance

The Car Insurance system  defines how customers and agents manage policies and claims.

    A Customer interacts with the system to Purchase Policy or File Claim.

    Purchasing a policy includes a mandatory step to Process Payment , which is handled by a Bank.

    The payment process can optionally be extended to Apply Discount.

    An Insurance Agent handles the Approve Application process , which includes a mandatory step to Validate VIN against a Vehicle Database.
------------------------------
