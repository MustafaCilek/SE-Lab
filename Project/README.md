------------------------------
This Use Case Diagram defines the system boundary for the "Your Path" platform and outlines the primary interactions between the system and its three main external actors: the User, the Mentor, and HR.

1. User (Student/Candidate) Workflows
The User actor represents the primary consumer of the platform's guidance and networking features. They directly initiate three main use cases:

    Request Mentorship: The user can browse and send formal requests to connect with professionals.

    Conduct Mentorship Session: The user participates in shared, active sessions with a connected mentor.

    Generate Career Roadmap: The user interacts with the system to build a personalized learning path. This use case features an <<extend>> relationship to Connect External Platforms. This indicates that while generating a roadmap is a standalone function, the user has the optional ability to link outside accounts to expand or enhance the roadmap's data.

2. Mentor Workflows
The Mentor actor represents industry professionals who volunteer to guide students. They interact with two main use cases:

    Conduct Mentorship Session: Mentors share this use case with Users, engaging in the actual communication and session execution.

    Manage Mentorship Tasks: Mentors organize the workload for their students. This use case has an <<include>> relationship with Assign Tasks & Feedback. This means that the act of managing tasks strictly requires the system to process the assignment of work and the delivery of feedback; it is a mandatory sub-process.

3. HR (Recruiter) Workflows
The HR actor represents company recruiters utilizing the platform to find verified talent.

    Manage Recruitment: HR users interact with the system to handle their hiring pipelines. This use case has an <<include>> relationship with View Candidates, indicating that the recruitment management process inherently requires the recruiter to view and access the candidate pool as a mandatory function.
------------------------------


------------------------------
This Class Diagram illustrates the static, structural backend model of the "Your Path" platform. It defines the core data entities, their internal attributes and methods, and the relationships that govern how they interact within the system.

1. Core User Data & Composition
At the center of the system is the User class, which stores primary applicant data such as their userName and verifiedSkills.

    Relationship to CareerRoadMap: There is a strict 1-to-1 Composition relationship (represented by the solid black diamond) between the User and the CareerRoadMap class. This indicates strong ownership: a user has exactly one roadmap tailored to their targetRole, and if the user account is deleted, their specific roadmap is entirely destroyed along with it. The CareerRoadMap handles its own logic for generateAIPath() and calculating the completionPercentage.

2. Mentorship Architecture & Aggregation
The system facilitates mentorship not through a direct link between people, but by utilizing a MentorshipSession class to manage the interactions.

    Relationship to User: There is a 1-to-many (*) Aggregation (represented by the hollow diamond) from the User to the MentorshipSession. A single user can participate in multiple sessions over time.

    Relationship to Mentor: Similarly, there is a 1-to-many (*) Aggregation from the Mentor class to the MentorshipSession. A single mentor can manage multiple sessions across their availableHours.

    This structure allows the MentorshipSession to handle the specific logistics of a meeting (like the scheduledDate and meetingLink) while the Mentor class handles the overarching pedagogical actions like assignTask() and provideFeedback().

3. Recruitment Pipeline
The JobPosting class represents the HR side of the platform.

    Relationship to User: There is a standard association between the JobPosting and the User. The job posting defines requirements (like a minimumMatchScore), and the system uses the calculateCandidateMatch() method to evaluate a user's verifiedSkills against the posting. This allows HR to seamlessly update a user's state via the updateRecruitmentStage() method.
------------------------------


------------------------------
This Activity Diagram maps the dynamic workflow and parallel processing required to generate a personalized learning path within the "Your Path" platform. The process is divided across three distinct swimlanes to define the responsibilities of the User, the internal System (AI), and External APIs (such as GitHub or LinkedIn).

1. Initiation Phase
The workflow begins in the User swimlane when the user inputs a target job title. This action immediately triggers the System to generate a foundational baseline roadmap based on general industry data.

2. Parallel Processing (The Fork)
Following the baseline generation, the workflow reaches a Fork Node (represented by the first thick horizontal bar). This splits the process into two concurrent, parallel tracks:

    Track A (System Calculation): The AI System independently begins calculating the specific, granular technical skills required for the target role.

    Track B (External Integration): Simultaneously, the User is prompted to link their external accounts. If linked, this triggers the External APIs to fetch the user's existing profile data.

3. Synchronization (The Join)
The defining structural feature of this workflow is the Join Node (represented by the second thick horizontal bar). This is a critical synchronization point: the system is forced to wait until both parallel tracks are fully complete. It cannot proceed until the required skills have been calculated AND the external profile data has been successfully fetched.

4. Resolution and Completion
Once synchronized, the workflow merges back into a single, linear path within the System swimlane:

    The System cross-references the newly calculated required skills against the data fetched from the user's external profiles, marking any matches as "Verified."

    The System mathematically updates the user's overall completion percentage based on those verified skills.

    Finally, the System outputs a finalized, visual timeline for the User, successfully terminating the activity workflow.
------------------------------


------------------------------
This State Diagram models the dynamic lifecycle and status transitions of a single mentorship task within the "Your Path" platform. It tracks the task from its initial creation by a mentor to its final verified completion by the user.

1. Initiation
The lifecycle begins at the initial start node (the solid black circle), which immediately places a newly assigned task into the Not Started state.

2. Active Execution
The task remains dormant until an event triggers a change in status:

    When the user starts working on the assignment, the "User Begins Work" event transitions the task into the In Progress state.

    Once the user finishes the assignment, the "User Marks as Complete" event transitions the task forward into the Under Mentor Review state, shifting the responsibility back to the mentor.

3. Evaluation & The Feedback Loop
From the review state, the workflow enters a Decision Node (the pink diamond), branching into two mutually exclusive paths based on the mentor's evaluation:

    The Revision Loop: If the mentor determines the work is incorrect or incomplete, the [Needs Revision] condition transitions the task backwards to the In Progress state. This creates an iterative feedback loop, keeping the task active until the user updates and resubmits their work.

    Approval: If the mentor is satisfied with the submission, the [Approved] condition transitions the task forward to the final stage.

4. Completion
Following mentor approval, the task enters the Verified state. This acts as the terminal state of the task process, leading directly to the final end node (the bullseye) and successfully concluding the task lifecycle.
------------------------------


------------------------------
This Sequence Diagram maps the chronological, step-by-step messaging and interactions between the User, the System, and a Mentor to establish a formal mentorship connection within the "Your Path" platform.

1. Discovery Phase
The sequence begins with the User initiating an active call to the System via searchByExpertise(topic). The System processes this request and replies with a passive return message, returnFilteredList(), providing the User with suitable mentor candidates.

2. Request & Acknowledgment Phase
Once a candidate is selected, the User sends a direct sendMentorshipRequest() message to the Mentor's lifeline. The Mentor's interface immediately sends back a dashed return message setting the status = Pending on the User's end, acknowledging receipt of the request.

3. Evaluation & Acceptance
The Mentor performs a self-call, reviewProfile(), representing an independent action where the mentor evaluates the user's suitability. Following a successful review, the Mentor initiates an active command, acceptRequest(), sending the approval back to the User.

4. Initialization Phase
To finalize the connection, the Mentor sends a command to the System to initializeSessionDashboard(). The System processes this setup and concurrently sends a dashboardCreated() return message to both the User and the Mentor. This final synchronization confirms that the shared workspace is ready and the mentorship connection is fully established.
------------------------------