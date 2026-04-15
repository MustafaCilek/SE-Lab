ATM Sequence Diagram

This diagram details the interaction flow during a banking session.

    A Customer initiates the process by inserting a card and entering a PIN.

    The ATM communicates with the BankServer to verify the PIN.

    During an active session loop, the ATM sends a request to authorize a withdrawal.

    The BankServer then checks funds against the Account, which returns a balance confirmation.

Medical Clinic State Diagram

This diagram illustrates a patient's progression through distinct clinic states.

    The sequence begins with the patient's arrival, followed by registration and triage.

    The core "Visit Workflow" centers on a Consultation.

    From the consultation state, the workflow can branch to Tests (looping back after results are reviewed), proceed to Prescription, or advance directly to Billing if no further treatment is needed.

    The process concludes once payment is completed.

Car Insurance Activity Diagram

This diagram maps the concurrent tasks and decisions divided between Customer and Insurance swimlanes.

    The Customer reports a vehicle accident while the Insurance provider verifies policy coverage.

    Following a synchronization step, the Customer submits a police report, and the Insurance provider formulates a settlement offer.

    The flow then splits based on a decision node: eligible claims proceed to a pre-approved payout, while claims requiring review trigger a field adjuster inspection.

    Both paths eventually converge, allowing the Insurance provider to process the final payout.

