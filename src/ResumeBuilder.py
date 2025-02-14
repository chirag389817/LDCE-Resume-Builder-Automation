from selenium import webdriver
from selenium.webdriver. common. by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import Data


driver = webdriver.Chrome()
driver.get("https://resume-builder-v1-ldce.netlify.app/")

btn_continue = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/button")
btn_continue.click()

def fill_input(val:str, xpath:str)->None:
    inp_element = driver.find_element(By.XPATH, xpath)
    inp_element.send_keys(val)

def select_input(idx:int, xpath:str)->None:
    inp_element = driver.find_element(By.XPATH, xpath)
    Select(inp_element).select_by_index(idx)


def fill_basic_details()->None:
    fill_input(Data.profile_path, "/html/body/div/div/div/div/div[2]/div[2]/div/input")
    fill_input(Data.name, "/html/body/div/div/div/div/div[2]/div[3]/input")
    fill_input(Data.email, "/html/body/div/div/div/div/div[2]/div[4]/input")
    fill_input(Data.mobile, "/html/body/div/div/div/div/div[2]/div[5]/input")
    fill_input(Data.linkedin_name, "/html/body/div/div/div/div/div[2]/div[6]/input")
    fill_input(Data.linkedin_link, "/html/body/div/div/div/div/div[2]/div[7]/input")
    fill_input(Data.github_name, "/html/body/div/div/div/div/div[2]/div[8]/input")
    fill_input(Data.github_link, "/html/body/div/div/div/div/div[2]/div[9]/input")
    fill_input(Data.about, "/html/body/div/div/div/div/div[2]/div[10]/textarea")

def fill_skills()->None:
    btn_addSkill = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[3]/div[2]/button")
    for i, skill in enumerate(Data.skills):
        btn_addSkill.click()
        fill_input(skill, f"/html/body/div/div/div/div/div[3]/div[2]/div[{i+1}]/input")

def fill_interests()->None:
    btn_addInterest = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[4]/div[2]/button")
    for i, interest in enumerate(Data.area_of_interests):
        btn_addInterest.click()
        fill_input(interest, f"/html/body/div/div/div/div/div[4]/div[2]/div[{i+1}]/input")

def fill_educations()->None:
    btn_addEdu = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[5]/button")
    for i,education in enumerate(Data.educations):
        btn_addEdu.click()
        fill_input(education.get('college'), f"/html/body/div/div/div/div/div[5]/div[{i+2}]/div[1]/input")
        fill_input(education.get('degree'), f"/html/body/div/div/div/div/div[5]/div[{i+2}]/div[2]/input")
        fill_input(education.get('percentage'), f"/html/body/div/div/div/div/div[5]/div[{i+2}]/div[3]/input")
        fill_input(education.get('s_year'), f"/html/body/div/div/div/div/div[5]/div[{i+2}]/div[4]/input")
        fill_input(education.get('e_year'), f"/html/body/div/div/div/div/div[5]/div[{i+2}]/div[5]/input")

def fill_projects()->None:
    btn_addProject = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[6]/button")
    for i, project in enumerate(Data.projects):
        btn_addProject.click()
        fill_input(project.get('title'), f"/html/body/div/div/div/div/div[6]/div[{i+2}]/div[1]/input")
        fill_input(project.get('link'), f"/html/body/div/div/div/div/div[6]/div[{i+2}]/div[2]/input")
        fill_input(project.get('desc'), f"/html/body/div/div/div/div/div[6]/div[{i+2}]/div[3]/textarea")

def fill_experiences()->None:
    btn_addExperience = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/button")
    for i, experience in enumerate(Data.experiences):
        btn_addExperience.click()
        fill_input(experience.get('company'), f"/html/body/div/div/div/div/div[7]/div[{i+2}]/div[1]/input")
        fill_input(experience.get('designation'), f"/html/body/div/div/div/div/div[7]/div[{i+2}]/div[2]/input")
        fill_input(experience.get('desc'), f"/html/body/div/div/div/div/div[7]/div[{i+2}]/div[3]/textarea")
        select_input(experience.get('s_month'), f"/html/body/div/div/div/div/div[7]/div[{i+2}]/div[4]/div/select")
        fill_input(experience.get('s_year'), f"/html/body/div/div/div/div/div[7]/div[{i+2}]/div[4]/div/input")
        select_input(experience.get('e_month'), f"/html/body/div/div/div/div/div[7]/div[{i+2}]/div[5]/div/select")
        fill_input(experience.get('e_year'), f"/html/body/div/div/div/div/div[7]/div[{i+2}]/div[5]/div/input")

def fill_hobbies()->None:
    btn_addHobby = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[8]/div[2]/button")
    for i,hobby in enumerate(Data.hobbies):
        btn_addHobby.click()
        fill_input(hobby, f"/html/body/div/div/div/div/div[8]/div[2]/div[{i+1}]/input")

def fill_achievements()->None:
    btn_addAchievements = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[9]/div[2]/button")
    for i,achievement in enumerate(Data.achievements):
        btn_addAchievements.click()
        fill_input(achievement, f"/html/body/div/div/div/div/div[9]/div[2]/div[{i+1}]/input")

def scroll_to_resume()->None:
    resume_element = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[11]")
    driver.execute_script("arguments[0].scrollIntoView(true);", resume_element)
