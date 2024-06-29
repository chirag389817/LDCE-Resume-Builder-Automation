# Leave empty string "" if not want to include
profile_path = r"C:\Users\csp38\Desktop\LDCE Resume\3.5 circle.png"
name = "Chirag Patel"
email = "chirag389817@gmail.com"
mobile = "+91 6354217280"
linkedin_name = "chirag389817"
linkedin_link = "https://www.linkedin.com/in/chirag389817/"
github_name = "chirag389817"
github_link = "https://github.com/chirag389817"
about = "I'm a full stack developer with a passion for Al and machine learning."

# make it empty if not want to include
# e.g. skills = []
skills = [
    "HTML",
    "CSS",
    "JavaScript"
]

# make it empty if not want to include
# e.g. area_of_interests = []
area_of_interests = [
    "Web Development", 
    "Cloud Computing"
]

# make it empty if not want to include
# e.g. educations = []
educations = [
    {
        "college":"L.D. College of Engineering, Ahmedabad", 
        "degree":"Bachelor's in Computer Engineering", 
        "percentage":"80", 
        "s_year":"2021", 
        "e_year":"pursuing"
    },
    {
        "college":"AB School, Chikhli", 
        "degree":"Higher Secondary Education", 
        "percentage":"70", 
        "s_year":"2020",
        # Leave empty string if not want to include
        # e.g. "e_year":""
        "e_year":"2021"
    }
]

# make it empty if not want to include
# e.g. projects = []
projects = [
    {
        "title":"Quick Quotes",
        # Leave empty string "" if not want to include
        "link":"",
        "desc":"A quote website where users can add and delete quotes. Built with NextJS and MongoDB, and used NextAuth for user authentication. The home page shows the latest quotes using ISR, and the profile page is dynamic."
    },
    {
        "title":"Personal Expense Tracker",
        "link":"",
        "desc":"A mini-project website for managing and analyzing personal expenses. Built with Sen,'lets and MySQL, the site allows users to add or remove categories, view expenses and total spendings by category."
    },
    {
        "title":"Notes",
        "link":"",
        "desc":"A notes website where users can add, delete, search, and update notes. Built with ReactJS and TailwindCSS, storing notes in the browser's local storage."
    },
]

# make it empty if not want to include
# e.g. experiences = []
experiences = [
    {
        "company":"Prakalpa Club - LDCE",
        "designation":"Web Development Head",
        "desc":"Managed and updated a Next.js website, making modifications to various pages.",
        # 1.Jan 2.Feb 3.Mar ... and so on
        "s_month":11,
        "s_year":"2023",
        # make it 0 if not want to include
        # e.g. "e_month":0
        "e_month":0,
        "e_year":"present"
    },
    {
        "company":"Smart India Hackathon",
        # Leave empty string "" if not want to include
        "designation":"",
        "desc":"Developed a dashboard using Next.js to analyze dropout students. Displayed district-wise data on a map of Gujarat.",
        "s_month":12,
        "s_year":"2023",
        "e_month":0,
        "e_year":""
    },
]

# make it empty if not want to include
# e.g. hobbies = []
hobbies =[
    "Playing Chess", 
    "Solving Sudoku"
]

# make it empty if not want to include
# e.g. achievements = []
achievements = [
    "AWS Cloud Certified",
    "Python Certification from Courcera",
]