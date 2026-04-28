import pytest
from YourPath import CareerRoadMap, User, Task, Mentor, JobPosting, CandidatePipeline

# --- 1. USER MODULE TESTS ---

def test_roadmap_zero_skills_returns_zero():
    roadmap = CareerRoadMap()
    assert roadmap.update_progress(verified_skills=0, total_required_skills=10) == 0.0

def test_roadmap_half_skills_returns_fifty():
    roadmap = CareerRoadMap()
    assert roadmap.update_progress(verified_skills=5, total_required_skills=10) == 50.0

def test_roadmap_zero_required_skills_returns_hundred_without_crashing():
    roadmap = CareerRoadMap()
    assert roadmap.update_progress(verified_skills=0, total_required_skills=0) == 100.0

def test_user_can_request_mentorship_if_under_limit():
    user = User()
    assert user.request_mentorship(active_requests=0) == True

def test_user_blocked_from_requesting_if_at_limit():
    user = User()
    # Expect a ValueError to be raised if they already have 3 active requests
    with pytest.raises(ValueError, match="Maximum active requests reached."):
        user.request_mentorship(active_requests=3)


# --- 2. MENTOR MODULE TESTS ---

def test_task_loops_to_in_progress_if_needs_revision():
    task = Task()
    new_state = task.process_feedback(current_state="Under Mentor Review", mentor_decision="[Needs Revision]")
    assert new_state == "In Progress"

def test_task_advances_to_verified_if_approved():
    task = Task()
    new_state = task.process_feedback(current_state="Under Mentor Review", mentor_decision="[Approved]")
    assert new_state == "Verified"

def test_mentor_available_for_short_session():
    mentor = Mentor()
    # Has 4 hours free, wants to add a 1 hour session
    assert mentor.check_availability(free_hours=4, new_session_duration=1) == True

def test_mentor_unavailable_for_long_session():
    mentor = Mentor()
    # Only has 1 hour free, wants to add a 2 hour session
    assert mentor.check_availability(free_hours=1, new_session_duration=2) == False


# --- 3. HR MODULE TESTS ---

def test_job_posting_calculates_correct_match_score():
    job = JobPosting()
    user_skills = ["Python"]
    required_skills = ["Python", "SQL"]
    # 1 out of 2 skills = 50%
    assert job.calculate_match_score(user_skills, required_skills) == 50

def test_pipeline_allows_valid_transition():
    pipeline = CandidatePipeline()
    # Applied -> Interview is exactly one step forward
    assert pipeline.update_stage(current_stage="Applied", new_stage="Interview") == "Interview"

def test_pipeline_blocks_skipping_stages():
    pipeline = CandidatePipeline()
    # Skipping the Interview stage straight to Offer should fail
    with pytest.raises(ValueError, match="InvalidStageTransition"):
        pipeline.update_stage(current_stage="Applied", new_stage="Offer")