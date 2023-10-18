
# MLOps using IBM Cloud Pak for Data
---

This repo can be used as a starter kit to setup a fully git integrated Machine Learning Operations Enviroment using Cloud Pak for Data. It uses a simple "credit score prediction" usecase that is split up into 4 jupyter notebooks as an example, which can easily be adapted to your business problem. 

![2023-08-22 08_54_46-2023_04_MLOps_AOT_Initiative drawio - diagrams net](https://media.github.ibm.com/user/396829/files/f34924e4-e74a-4177-911c-222fd785e6a2)
*high level overview using three stages*



# Setup Instructions

1. Fork this repo
2. You will need at least 3 different CP4D projects
    2. Create a git-enabled project called "staging-area"
        1. Use the github repo address and your private access token
        1. Create a job for every one of the notebooks
    1. Create a NON-git-enabled project called "automation-area"
        1. Create a Watson Pipeline Instance
        2. configure all the jobs from the "staging-area" to run after each other
    3. Create at least one git-enabled project called "datascience-playground"
        1. Do your datascience Magic here
3. Setup Automation using github actions
   1. tbd.
4. Setup monitoring using open scale
   1. tbd


![2023-08-02 06_44_15-2023_04_MLOps_AOT_Initiative drawio - diagrams net](https://media.github.ibm.com/user/396829/files/5d46b441-d584-4b98-8af1-5927f8f5ee1c)
*technical detailed view using two stages*

    
