"""
Job Market Trends Analysis System
Student ID: [YourID]
Author: [Your Name]
Module: Software Quality Assurance (COMP 30010.1)
"""

# ------------------------------------------------------------------
# Requirement 1: Classify job postings by sector and experience level
# Requirement 2: Calculate and report sector unemployment/hiring rate
# ------------------------------------------------------------------

def get_sector_name(sector_code):
    """Return sector name using switch-like structure (dictionary dispatch)."""
    sector_map = {
        1: "Information Technology",
        2: "Healthcare",
        3: "Finance & Banking",
        4: "Education",
        5: "Manufacturing",
    }
    return sector_map.get(sector_code, "Unknown Sector")


def classify_job_posting(sector_code, vacancies, applications, experience_years):
    if vacancies < 0 or applications < 0:
        raise ValueError("Inputs must be non-negative integers")
    """
    Classify a job posting and compute hiring metrics.

    Uses:
      - switch statement (via if/elif chain) for sector classification
      - if-else statements for experience-level and demand evaluation
    """

    # ---------- SWITCH STATEMENT (sector classification) ----------
    if sector_code == 1:
        sector = "Information Technology"
        base_salary = 55000
    elif sector_code == 2:
        sector = "Healthcare"
        base_salary = 50000
    elif sector_code == 3:
        sector = "Finance & Banking"
        base_salary = 60000
    elif sector_code == 4:
        sector = "Education"
        base_salary = 35000
    elif sector_code == 5:
        sector = "Manufacturing"
        base_salary = 40000
    else:
        sector = "Unknown Sector"
        base_salary = 30000

    # ---------- IF-ELSE STATEMENT (experience classification) ----------
    if experience_years < 1:
        level = "Entry Level"
        salary_multiplier = 1.0
    elif experience_years < 3:
        level = "Junior"
        salary_multiplier = 1.15
    elif experience_years < 6:
        level = "Mid-Level"
        salary_multiplier = 1.35
    elif experience_years < 10:
        level = "Senior"
        salary_multiplier = 1.60
    else:
        level = "Expert / Lead"
        salary_multiplier = 1.90

    estimated_salary = base_salary * salary_multiplier

    # ---------- IF-ELSE STATEMENT (market demand evaluation) ----------
    if vacancies == 0:
        demand_status = "No Vacancies"
        competition_ratio = 0
    else:
        competition_ratio = round(applications / vacancies, 2)
        if competition_ratio > 10:
            demand_status = "Very High Demand (Employer's Market)"
        elif competition_ratio > 5:
            demand_status = "High Demand"
        elif competition_ratio > 2:
            demand_status = "Moderate Demand"
        else:
            demand_status = "Low Demand (Candidate's Market)"

    return {
        "sector": sector,
        "experience_level": level,
        "estimated_annual_salary": round(estimated_salary, 2),
        "competition_ratio": competition_ratio,
        "demand_status": demand_status,
    }


def calculate_hiring_rate(total_vacancies, filled_positions):
    """
    Calculate the hiring rate percentage for a sector.
    Args:
        total_vacancies (int): Total number of job vacancies available.
        filled_positions (int): Number of positions successfully filled.
    Returns:
        tuple: (hiring_rate float, quality_label str)
    """
    """Calculate and evaluate sector hiring rate."""
    if total_vacancies == 0:
        return 0.0, "No data available"

    hiring_rate = (filled_positions / total_vacancies) * 100

    if hiring_rate >= 90:
        quality = "Excellent hiring efficiency"
    elif hiring_rate >= 70:
        quality = "Good hiring efficiency"
    elif hiring_rate >= 50:
        quality = "Average hiring efficiency"
    else:
        quality = "Poor hiring efficiency - review process"

    return round(hiring_rate, 2), quality


# ======================== MAIN PROGRAM ========================
if __name__ == "__main__":
    print("=" * 60)
    print("   JOB MARKET TRENDS ANALYSIS SYSTEM")
    print("=" * 60)

    # Test Data Set 1 - IT Senior Role
    result1 = classify_job_posting(
        sector_code=1, vacancies=10, applications=150, experience_years=7
    )
    print("\n[Test Case 1] IT Senior Role")
    for k, v in result1.items():
        print(f"  {k:<30}: {v}")

    # Test Data Set 2 - Healthcare Entry Level
    result2 = classify_job_posting(
        sector_code=2, vacancies=20, applications=30, experience_years=0
    )
    print("\n[Test Case 2] Healthcare Entry Level")
    for k, v in result2.items():
        print(f"  {k:<30}: {v}")

    # Test Data Set 3 - Unknown Sector
    result3 = classify_job_posting(
        sector_code=9, vacancies=5, applications=10, experience_years=3
    )
    print("\n[Test Case 3] Unknown Sector Mid-Level")
    for k, v in result3.items():
        print(f"  {k:<30}: {v}")

    # Test Data Set 4 - Zero Vacancies Edge Case
    result4 = classify_job_posting(
        sector_code=3, vacancies=0, applications=50, experience_years=5
    )
    print("\n[Test Case 4] Finance Zero Vacancies")
    for k, v in result4.items():
        print(f"  {k:<30}: {v}")

    # Hiring Rate Calculation
    print("\n[Hiring Rate Analysis]")
    rate, quality = calculate_hiring_rate(total_vacancies=50, filled_positions=43)
    print(f"  Hiring Rate: {rate}%")
    print(f"  Assessment : {quality}")

    print("\n" + "=" * 60)
    print("   ANALYSIS COMPLETE")
    print("=" * 60)
