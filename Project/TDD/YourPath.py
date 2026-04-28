class CareerRoadMap:
    def update_progress(self, verified_skills: int, total_required_skills: int) -> float:
        """Calculates the completion percentage of a career roadmap."""
        if total_required_skills == 0:
            return 100.0
        return (verified_skills / total_required_skills) * 100.0

class User:
    def request_mentorship(self, active_requests: int) -> bool:
        """Processes a mentorship request, enforcing a spam-prevention limit."""
        if active_requests >= 3:
            raise ValueError("Maximum active requests reached.")
        return True

class Task:
    def process_feedback(self, current_state: str, mentor_decision: str) -> str:
        """Handles the state transitions based on mentor feedback."""
        if current_state == "Under Mentor Review":
            if mentor_decision == "[Needs Revision]":
                return "In Progress"
            elif mentor_decision == "[Approved]":
                return "Verified"
        raise ValueError("Invalid state or decision.")

class Mentor:
    def check_availability(self, free_hours: int, new_session_duration: int) -> bool:
        """Checks if a mentor has enough free time for a new session."""
        return free_hours >= new_session_duration

class JobPosting:
    def calculate_match_score(self, user_skills: list, required_skills: list) -> int:
        """Calculates the percentage of required skills a user possesses."""
        if not required_skills:
            return 100
        matching_skills = set(user_skills).intersection(required_skills)
        return int((len(matching_skills) / len(required_skills)) * 100)

class CandidatePipeline:
    def update_stage(self, current_stage: str, new_stage: str) -> str:
        """Safely transitions a candidate through the hiring pipeline."""
        valid_pipeline = ["Applied", "Interview", "Offer"]
        
        if current_stage not in valid_pipeline or new_stage not in valid_pipeline:
            raise ValueError("InvalidStageTransition")
            
        current_idx = valid_pipeline.index(current_stage)
        new_idx = valid_pipeline.index(new_stage)
        
        # Enforce that stages cannot be skipped (must move exactly 1 step forward)
        if new_idx != current_idx + 1:
            raise ValueError("InvalidStageTransition")
            
        return new_stage