# SinAroundU
For better life in Singapore

### Code
#### FrontEnd Files
|-- index.html<br>
|-- about-us.html<br>
|-- main.html<br>
|-- css/<br>
|-- img/<br>
|-- js/<br>
|-- echarts/
#### BackEnd Files        
|-- LoadData.py<br>
|-- LoadDataDBPolicy.json<br>
|-- LoadDataS3Policy.json<br>
|-- SinAroundU.py<br>
|-- SinAroundUDBPolicy.json
|-- SinAroundUS3Policy.json<br>

### Instructions for Application Deployment
1. Deploy frontend html pages, css and js customization and image/video files using AWS Amplify service
2. Create S3 buckets for image/video and data storage, then upload required files; 
3. Construct and deploy Lambda functions SinAroundU.py and LoadData.py on AWS Lambda service; 
4. Create a RESTful API on AWS API Gateway
	* Create POST methods for our lambda functions
	* Choose Lambda Function for integration type
	* Enable CORS
	* Deploy API
	* Set the method requests status to be 200 if lambda function is correctly executed
5. Add IAM policy to lambda functions for I/O operations. In the configuration part of a lambda function, click on the permission and then click into the IAM management console. Then, we can add inline policy to the lambda function. The policies for LoadData function and SinAroundU function are stored in LoadDataPolicy.json and SinAroundUPolicy.json; 
6. Build tables in DynamoDB for each dataset using `district id` as partition key and `facility` as sorted key, then load data from S3 to DynamoDB using LambdaFunction LoadData.py. 

### Web UI
Home page: Each district in the map is a button, connecting to main.html and showing facility information in the same district.

![image](https://user-images.githubusercontent.com/76780790/163177294-f9a63508-079e-4d4f-928c-0355349868f4.png)

Map and information for facilities in each district:

![image](https://user-images.githubusercontent.com/76780790/163177477-d4f58689-3ade-4ed5-81cb-c165d8a3c92c.png)

Flat rent price trend chart:

![image](https://user-images.githubusercontent.com/76780790/163177515-4c30b0f7-e183-44db-929a-dd3bd6fd5bc6.png)



