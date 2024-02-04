 aws cloudformation validate-template --template-body file://template.yml



 aws cloudformation create-stack --stack-name dynamoDBCloudformation --template-body file://template.yml

 aws cloudformation update-stack --stack-name dynamoDBCloudformation --template-body file://template.yml /
 --capabilities CAPABILITY_IAM
§

