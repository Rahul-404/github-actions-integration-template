# Github Actions Integration Template

![Deployment-Architecture](/docs/AWS-CI:CD.jpg)

Deployment using github actions on AWS, requires a virtual machine (to run project as docker image), a remote repository (to push and pull docker image) and a storage service (to access or save artifacts generated in the process like logs, ingested data, trained models), so we have to start with :

## Deployment on Local Environment:

1. Test the application in local system, docker images possible or not

    a. build docker image in local environment
    ```bash
    docker build -t <image-name> .
    ```
    b. export image name
    ```bash
    export IMAGE_NAME="<image-name>"
    ```
    c. run image 
    ```bash
    docker compose up
    ```

    d. app is running , open the given url in to browser

## Deployment on Cloud Environment:

1. Login to AWS console.

2. [Create IAM user](https://medium.com/@rahulshelke3399/how-to-attach-policies-to-an-iam-user-in-aws-with-custom-policy-example-079f6ec3fdbb) for deployment
    This user should have specific access like 
    1. EC2 instance aceess : it is a virtual machine.
    2. ECR : elastic container registry to save your docker image.

    [Policies to attach](https://medium.com/@rahulshelke3399/how-to-attach-policies-to-an-iam-user-in-aws-with-custom-policy-example-079f6ec3fdbb):
    1. AmazonEC2ContainerRegistryFUllAccess
    2. AmazonEC2FullAccess
    3. AmazonS3FullAccesss

3. [Create S3 bucket]()

4. [Create ECR repository](https://medium.com/@rahulshelke3399/how-to-create-an-ecr-repository-in-aws-3af21c2f1309) to store/save dcoker image
    - Save the URI: <12-digit-code>.dkr.ecr.<region-name> .amazons.com/<repository-name>

5. [Create EC2 machine](https://medium.com/@rahulshelke3399/how-to-create-an-ec2-instance-in-aws-c0c09f100988) (Ubuntu)

6. Open EC2 and install docker in EC2 machine:

    a. Optional:
    ```bash
    sudo apt-get update -y
    sudo apt-get upgrade -y
    ```

    b. Install Docker on EC2:
    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```
7. Configure EC2 as [self-hosted runner](https://medium.com/@rahulshelke3399/how-to-setup-self-hosted-runner-in-your-github-repository-fa00b3f7c824):
    > Setting -> actions -> runner -> new self hosted runner -> choose os -> then run command one by one

8. Setup github secrets:
   ```bash
    AWS_ACCESS_KEY_ID = ""
    AWS_SECRET_ACCESS_KEY = ""
    AWS_REGION = ""
    AWS_ECR_LOGIN_URI = <12-digit>.dkr.ecr.ap-south-1.amazonaws.com 
    ECR_REPOSITORY_NAME = <repository-name> 
   ```
