Use Case Diagram
------------------------------
1. User (Student/Candidate) Workflows
The User actor represents the primary consumer of the platform's guidance and networking features. They directly initiate three main use cases:

    Request Mentorship: The user can browse and send formal requests to connect with professionals.

    Conduct Mentorship Session: The user participates in shared, active sessions with a connected mentor.

    Generate Career Roadmap: The user interacts with the system to build a personalized learning path. This use case features an <<extend>> relationship to Connect External Platforms. This indicates that while generating a roadmap is a standalone function, the user has the optional ability to link outside accounts to expand or enhance the roadmap's data.

2. Mentor Workflows
The Mentor actor represents industry professionals who volunteer to guide students. They interact with two main use cases:

    Conduct Mentorship Session: Mentors share this use case with Users, engaging in the actual communication and session execution.

    Manage Mentorship Tasks: Mentors organize the workload for their students. This use case has an <<include>> relationship with Assign Tasks & Feedback. This means that the act of managing tasks strictly requires the system to process the assignment of work and the delivery of feedback; it is a mandatory sub-process.

3. HR Workflows
The HR actor represents company recruiters utilizing the platform to find verified talent.

    Manage Recruitment: HR users interact with the system to handle their hiring pipelines. This use case has an <<include>> relationship with View Candidates, indicating that the recruitment management process inherently requires the recruiter to view and access the candidate pool as a mandatory function.
------------------------------

Class Diagram
------------------------------
1. User Data & Composition
At the center of the system is the User class, which stores primary applicant data such as their userName and verifiedSkills.

    Relationship to CareerRoadMap: There is a 1-to-1 Composition relationship between the User and the CareerRoadMap class.

2. Mentorship  Aggregation
    Relationship to User: There is a 1-to-many Aggregation  from the User to the MentorshipSession.

    Relationship to Mentor: Similarly, there is a 1-to-many.

3. Recruitment Pipeline
The JobPosting class represents the HR side of the platform.

    Relationship to User: There is a standard association between the JobPosting and the User.
------------------------------

Activity Diagram
------------------------------
1. Initiation Phase
The workflow begins in the User swimlane when the user inputs a target job title. This action immediately triggers the System to generate a foundational baseline roadmap based on general industry data.

2. Parallel Processing (The Fork)
Following the baseline generation, the workflow reaches a Fork Node. This splits the process into two concurrent, parallel tracks:

    Track A (System Calculation): The AI System independently begins calculating the specific technical skills required for the target role.

    Track B (External Integration): Simultaneously, the User is prompted to link their external accounts. If linked, this triggers the External APIs to fetch the user's existing profile data.

3. Synchronization (The Join)
This is a critical synchronization point: the system is forced to wait until both parallel tracks are fully complete. It cannot proceed until the required skills have been calculated and the external profile data has been successfully fetched.

4. Completion
Once synchronized, the workflow merges back into a single, linear path within the System swimlane:

    The System cross-references the newly calculated required skills against the data fetched from the user's external profiles, marking any matches as "Verified."

    The System mathematically updates the user's overall completion percentage based on those verified skills.

    Finally, the System outputs a finalized, visual timeline for the User, successfully terminating the activity workflow.
------------------------------

State Diagram
------------------------------
1. Initiation
The lifecycle begins at the initial start node (the solid black circle), which immediately places a newly assigned task into the Not Started state.

2. Active Execution
The task remains dormant until an event triggers a change in status:

    When the user starts working on the assignment, the "User Begins Work" event transitions the task into the In Progress state.

    Once the user finishes the assignment, the "User Marks as Complete" event transitions the task forward into the Under Mentor Review state, shifting the responsibility back to the mentor.

3. Evaluation & The Feedback Loop
From the review state, the workflow enters a Decision Node, branching into two mutually exclusive paths based on the mentor's evaluation:

    The Revision Loop: If the mentor determines the work is incorrect or incomplete, the [Needs Revision] condition transitions the task backwards to the In Progress state. This creates an iterative feedback loop, keeping the task active until the user updates and resubmits their work.

    Approval: If the mentor is satisfied with the submission, the [Approved] condition transitions the task forward to the final stage.

4. Completion
Following mentor approval, the task enters the Verified state. This acts as the terminal state of the task process, leading directly to the final end node and successfully concluding the task lifecycle.
------------------------------

Sequence Diagram
------------------------------
1. Discovery Phase
The sequence begins with the User initiating an active call to the System via searchByExpertise(topic). The System processes this request and replies with a passive return message, returnFilteredList(), providing the User with suitable mentor candidates.

2. Request & Acknowledgment Phase
Once a candidate is selected, the User sends a direct sendMentorshipRequest() message to the Mentor's lifeline. The Mentor's interface immediately sends back a dashed return message setting the status = Pending on the User's end, acknowledging receipt of the request.

3. Evaluation & Acceptance
The Mentor performs a self-call, reviewProfile(), representing an independent action where the mentor evaluates the user's suitability. Following a successful review, the Mentor initiates an active command, acceptRequest(), sending the approval back to the User.

4. Initialization Phase
To finalize the connection, the Mentor sends a command to the System to initializeSessionDashboard(). The System processes this setup and concurrently sends a dashboardCreated() return message to both the User and the Mentor. This final synchronization confirms that the shared workspace is ready for the mentorship connection.
------------------------------