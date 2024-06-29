import ResumeBuilder as builder

if __name__ == "__main__":
    # Remove or comment the section if not want to include
    # e.g. # builder.fill_hobbies()
    builder.fill_basic_details()
    builder.fill_skills()
    builder.fill_interests()
    builder.fill_educations()
    builder.fill_projects()
    builder.fill_experiences()
    builder.fill_hobbies()
    builder.fill_achievements()
    builder.scroll_to_resume()
    input()