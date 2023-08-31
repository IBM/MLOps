
# MLOps using IBM Cloud Pak for Data
---

This repo can be used as a starter kit to setup a fully git integrated Machine Learning Operations Enviroment using Cloud Pak for Data. It uses a simple "credit score prediction" usecase that is split up into 4 jupyter notebooks as an example, which can easily be adapted to your business problem. 

![2023-08-22 08_54_46-2023_04_MLOps_AOT_Initiative drawio - diagrams net](https://media.github.ibm.com/user/396829/files/f34924e4-e74a-4177-911c-222fd785e6a2)
*high level overview using three stages*



# Setup Instructions
These instructions will guide you through the setup of a simple MLOps environment that uses just two stages ("dev" and "prod"). The setup can be easily extended to more stages if needed. 

It is assumed that you have a "Cloud Pak for Data" instance available and that you have admin rights to it (This will not work with the cloud based "as a Service" Offering). 

![Alt text](images\image-1.png)
*detailed view using two stages*
## 1. Fork this repo

<details>
<summary><b> need a detailed description?</b></summary>

tbd...

</details>


## 2. setup at least 3 different CP4D projects (for a two stage setup)
### 1.   Create at least one git-enabled project called "00-datascience-playground"

<details>
<summary><b> need a detailed description?</b></summary>

tbd...
![Alt text](/images/2023-08-31-09_10_14.png)

Use the github repo address and your private access token 
You can Alter the notebooks to your needs if you want to. It is important that you keep the naming of the notebooks.
</details>


### 2. Create a NON-git-enabled project called "01-staging-area"
Use the github repo address and your private access token 
Create a job for every one of the notebooks 
### 3. Create a git-enabled project called "02-automation-area"
Create a Watson Pipeline Instance
configure all the jobs from the "staging-area" to run after each other

## 3. Setup Automation using github actions
   1. tbd.
## 4. Setup monitoring using open scale
   1. tbd




![2023-08-02 06_44_15-2023_04_MLOps_AOT_Initiative drawio - diagrams net](https://media.github.ibm.com/user/396829/files/5d46b441-d584-4b98-8af1-5927f8f5ee1c)
*technical detailed view using two stages*

    
