------------------------------
ATM Sequence Diagram

This diagram shows step-by-step interactions between the actors and the system for a successful cash withdrawal:

    Authentication: The Customer inserts their card, which the ATM validates with the Bank Server. Once the card is validated, the ATM prompts the Customer for their PIN. The Customer enters it, and the ATM sends it to the Bank Server for verification.

    Transaction Request: After successful PIN verification, the Customer requests a specific withdrawal. The ATM takes this request and forwards it to the Bank Server to be processed.

    Backend Processing: The Bank Server communicates directly with the Account database to check the available funds and deduct the requested amount. The Account then confirms the new balance back to the Server.

    Fulfillment: The Bank Server sends the final withdrawal approval down to the ATM, which completes the transaction by dispensing the cash to the Customer.
------------------------------


------------------------------
Medical Clinic State Diagram Workflow

This diagram shows the process of a patient's visit through a medical clinic:

    Arrival and Intake: The workflow begins when the patient enters the Patient Arrives state. Once check-in is complete, they transition to Registration. When a nurse becomes available, the patient moves into Triage.

    The Consultation Loop: After vitals are recorded, the patient enters the core Consultation state. From here, the path branches based on the doctor's medical assessment:

        If tests are needed, the patient moves into the Tests state. Once the results are reviewed, they loop back into Consultation.

        If medication is prescribed, they move to the Prescription state. After the pharmacy details are finalized, they proceed to Billing.

        If no further treatment or medication is necessary, the patient bypasses the prescription phase entirely and goes directly to Billing.

    Completion: Once the patient reaches the Billing state and the payment is completed, the visit successfully concludes at the final end state.
------------------------------


------------------------------
Car Insurance Activity Diagram

This diagram shows the step-by-step workflow and parallel responsibilities between a Customer and an Insurance Company during a vehicle claim process:

    Initiation & Verification: The process kicks off when the Customer reports a vehicle accident. The system immediately routes this to the Insurance Company, which verifies that the policy is active and covers the incident.

    Parallel Processing: Once coverage is confirmed, the workflow splits into two simultaneous tracks: the Customer works on submitting the official police report, while the Insurance Company concurrently begins formulating a settlement offer.

    The Decision Path: After the Customer submits the police report, the claim is evaluated. If it is a standard claim, it takes the [Eligible] path for a pre-approved payout. If it is more complex, it takes the [Requires Review] path, triggering a field adjuster inspection. Both of these possible outcomes then merge back into a single workflow path.

    Synchronization: The system uses a "Join" step to ensure both parallel tracks are completely finished before moving on. It waits until the customer's evaluation path is complete and the insurance company has finished formulating the settlement offer.

    Completion: Once both sides are ready, the Insurance Company processes the final payout, and the claim workflow successfully ends.
------------------------------
