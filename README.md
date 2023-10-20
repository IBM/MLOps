
# README
---

This repo can be used as a starter kit to setup a fully git integrated Machine Learning Operations enviroment using Cloud Pak for Data. It uses a simple "credit score prediction" usecase that is split up into 4 jupyter notebooks as an example, which can easily be adapted to your business problem. 

![high level overview using three stages](/images/2023-09-05-11_00_27.png)

*high level overview using three stages*



# Setup Instructions
These instructions will guide you through the setup of a simple MLOps environment that uses just two stages ("dev" and "prod"). The setup can be easily extended to more stages if needed. 

It is assumed that you have a "Cloud Pak for Data" instance available and that you have admin rights to it (This will not work with the cloud based "as a Service" Offering). 

![Alt text](/images/image-1.png)
*detailed view using two stages*
## 1. Fork this repo

<details>
<summary><b> need a detailed description?</b></summary>

![Alt text](/images/image-1.png)

click the "Fork" button in the upper right corner of this repo. **IMPORTANT: uncheck the "only fork the master branch" checkbox.**
 This will create a copy of this repo in your own github account. We will be using this copy in the following steps.
</details>


## 2.   Create one git-enabled project called "00-datascience-playground"

<details>
<summary><b> need a detailed description?</b></summary>


![Alt text](/images/2023-08-31-09_10_14.png)
*this is the project that we are creating in this step*
![Alt text](/images/image-2.png)
navigate to all projects
![Alt text](/images/image-4.png)
create a project that is "integrated with git". In the next window we will need to provide the github repo address and a private access token. So lets create that token first.
![Alt text](/images/image-5.png)
navigate to https://github.com/settings/tokens and choose "Generate new token". Give it a name and select the "repo" scope as shown in the next image. 
![Alt text](/images/image-6.png)
**Copy the generated token to your clipboard.** You will not be able to see it again after you close the window.
![Alt text](/images/image-7.png)
Make this token available within your CP4D by creating a "New Token" and using the token you just created. Once you created it use the dropdown to select it.
![Alt text](/images/image-8.png)
add the Repo URL (dont forget the .git at the end ;-) and choose the main branch. Then hit "Create"

Use the github repo address and your private access token 
You can Alter the notebooks to your needs if you want to. It is important that you keep the naming of the notebooks.
</details>


## 3. Create one git-enabled project called "01-staging-area"

<details>
<summary><b> need a detailed description?</b></summary>

![Alt text](/images/image-2.png)
navigate to all projects
![Alt text](/images/image-4.png)
In your CP4D Instance you access the project overview by clicking on the "Projects" Icon in the upper left corner. Then click on "New Project" and select "Create a project integrated with a Git repository". Give it the name "01-staging-area" and select "create"

Use the same github repo address and your private access token as in 2
 
</details>

## 4. Configure Jobs in "01-staging-area"
<details>
<summary><b> need a detailed description?</b></summary>

![Alt text](/images/image-9.png)
navigate to "view local branch"

![Alt text](/images/image-11.png)
click "New code job"

![Alt text](/images/image-12.png)
choose the first notebook "00-git-pull.ipynb" and click "configure job"

![Alt text](/images/image-13.png)
give it the same name as the notebook and click "next"
accept all the defaults and click "next" until you can click "create job"
repeat those steps for all five notebooks.

![Alt text](/images/image-14.png)
once you are done it should look like this.


</details>

## 5. Create a NON-git-enabled project called "02-automation-area"

<details>
<summary><b> need a detailed description?</b></summary>

![Alt text](/images/image-3.png)
repeat the same steps as in 2 and 3 but choose "create an empty project" to create a NON-git-enabled project. Name it "02-automation-area"


</details>



## 6. Configure pipeline in "02-automation-area"
<details>
<summary><b> need a detailed description?</b></summary>

![Alt text](/images/image-16.png)
Click "New Asset" and choose "Pipeline". Name the pipeline "mlops_pipeline"

![Alt text](/images/image-18.png)
go to "Run">"Run Notebook Job" and drag it onto the plane. Then doubleclick this newly created node and click "select Job".

![Alt text](/images/image-19.png)
choose "01-staging-area" and there the first notebook "00-git-pull.ipynb" and click "choose" and then "save"

![Alt text](/images/image-20.png)
repeat those steps for all notebooks until you end up with something that looks like this.

![Alt text](/images/image-29.png)
Click "Run Pipeline" and then "create job". Give it a name like "mlops_pipeline_job" . **IMPORTANT: The github action assumes that you only have ONE job in this project. If you have more than one job you will need to change the github action accordingly.**


</details>

## 7. Setup Github Actions 
<details>
<summary><b> need a detailed description?</b></summary>

We need a set of secrets to be able to run the github actions. Those secrets are:

- **API_KEY**
- **USER_NAME**
- **CLUSTER_URL**
- **PROJECT_ID**
- **PERSONAL_ACCESS_TOKEN_GITHUB**


We will now go through all those step by step:

![Alt text](/images/image-21.png)
navigate to your fork of the github repo then "Settings">"Secrets and variables">"actions">"new repository secret" 

### 7.1. retriving your CP4D **API_KEY** and **USER_NAME**

![Alt text](/images/image-22.png)
go to the "profile and settings" tab in your cp4d instance

![Alt text](/images/image-23.png)
copy the api key to your clipboard (and write it down somewhere. You will not be able to see it again after you close the window)

![Alt text](/images/image-24.png)
go back to github and creaete a new repository secret called "API_KEY"

![Alt text](/images/image-27.png)

Also create the repository secret USER_NAME using the username that you use to login to your CP4D instance


### 7.2. retriving your CP4D **CLUSTER_URL**

this one is simple :-) 
![Alt text](/images/image-25.png)

just take the URL of the cluster that you have been workin on

![Alt text](/images/image-26.png)

and use it to create a secret called "CLUSTER_URL"

### 7.3. retriving your CP4D **PROJECT_ID**

![Alt text](/images/image-28.png)

### 7.4. retriving your github **PERSONAL_ACCESS_TOKEN_GITHUB**

You can use the same token you used in step 2. If you dont have it anymore you can create a new one by following the steps in 2.



</details>

## 8. Try it out :-) 

## 9. Setup monitoring using open scale
   wip -- coming soon


    
