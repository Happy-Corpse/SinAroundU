# SinAroundU
For better life in Singapore

### Code
#### FrontEnd Files
index.html -- home page<br>
about-us.html -- about-us<br>
main.html -- main page for map, info and chart<br>
css/ -- style <br>
img/ -- logo, icon, background, video <br>
[comment]: # (We upload the video to S3, so the video is read through a url.)<br>
js/ --  map and scroll bar<br>
echarts/ -- line chart
#### BackEnd Files
LambdaFunctions:<br>             
SinAroundU.py<br>
LoadData.py<br>
lib/<br>
AWSDataWrangler-Python38

Instructions for Application Deployment

1. Deploy frontend html pages, css and js customization and image/video files using AWS Amplify service
2. Create S3 buckets for image/video and data storage, then upload required files; 
3. Construct and deploy Lambda functions SinAroundU.py and LoadData.py on AWS Lambda service; 
4. Create a RESTful API on AWS API Gateway
	* Create POST methods for our lambda functions
	* Choose Lambda Function for integration type
	* Enable CORS
	* Deploy API
	* Set the method requests status to be 200 if lambda function is correctly executed.
5. Add IAM policy to lambda functions for I/O operations. In the configuration part of a lambda function, click on the permission and then click into the IAM management console. Then, we can add inline policy to the lambda function. The policies for LoadData function and SinAroundU function are stored in LoadDataPolicy.json and SinAroundUPolicy.json
6. Build tables in DynamoDB for each dataset using `district id` as partition key and `facility` as sorted key, then load data from S3 to DynamoDB using LambdaFunction LoadData.py; 

