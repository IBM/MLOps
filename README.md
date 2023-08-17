
# make-mlops-with-cpd-easy
https://aotweb.dal1a.cirrus.ibm.com/initiatives/63f7611a0255320017189a63
![2023-08-02 06_44_15-2023_04_MLOps_AOT_Initiative drawio - diagrams net](https://media.github.ibm.com/user/396829/files/5d46b441-d584-4b98-8af1-5927f8f5ee1c)



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

    
