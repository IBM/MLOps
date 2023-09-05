
# MLOps using IBM Cloud Pak for Data
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

TODO: add step by step images

</details>


## 2.   Create one git-enabled project called "00-datascience-playground"

<details>
<summary><b> need a detailed description?</b></summary>


![Alt text](/images/2023-08-31-09_10_14.png)
*this is the proect that we are creating in this step*

TODO: add step by step images

Use the github repo address and your private access token 
You can Alter the notebooks to your needs if you want to. It is important that you keep the naming of the notebooks.
</details>


## 3. Create one git-enabled project called "01-staging-area"

<details>
<summary><b> need a detailed description?</b></summary>


TODO: add overview image
TODO: add step by step images

Use the github repo address and your private access token 
Create a job for every one of the notebooks 
</details>




## 4. Create a NON-git-enabled project called "02-automation-area"

<details>
<summary><b> need a detailed description?</b></summary>


TODO: add overview image
TODO: add step by step images

Create a Watson Pipeline Instance
configure all the jobs from the "staging-area" to run after each other
</details>


## 5. Configure Jobs in "01-staging-area"
<details>
<summary><b> need a detailed description?</b></summary>

TODO: add overview image
TODO: add step by step images

</details>

## 6. Configure pipeline in "02-automation-area"
<details>
<summary><b> need a detailed description?</b></summary>

TODO: add overview image
TODO: add step by step images

</details>

## 7. Setup Github Actions 
<details>
<summary><b> need a detailed description?</b></summary>

TODO: add overview image
TODO: add step by step images

</details>

## 8. Try it out :-) 

## 9. Setup monitoring using open scale
   wip -- coming soon

    
