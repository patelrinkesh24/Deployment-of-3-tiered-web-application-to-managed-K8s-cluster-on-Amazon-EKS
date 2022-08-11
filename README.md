# Deployment-of-3-tiered-web-application-to-managed-K8s-cluster-on-Amazon-EKS

![workflow](https://user-images.githubusercontent.com/50281621/184049568-ed128ef5-211d-493c-96c5-07d39fe2913f.png)


•	GitHub to store your application’s code and K8s manifests
•	GitHub Actions to automate build and publishing of application’s image 
•	Docker cli to build the image, test it locally and as part of GitHub Actions and publish it to Amazon ECR
•	Amazon ECR to securely store your Docker images
•	Amazon EKS to host your application
•	Amazon EBS to provide persistent storage for MySQL DB
•	Amazon S3 to store image that your application uses as a background
•	AWS IAM to grant application access to you private Amazon S3 bucket
•	Cloud9 IDE or your local environment to develop your application and build container images 
•	kubectl to work with your Amazon EKS cluster
•	eksctl to create and delete your cluster 

