# Problem Solving

I have decided to use python due to simplicity and fast development. In order for the code to be more re-usable and extensible I have used OOP.
Boto3 is one of the main libraries to interact with AWS and argparse is used to simplify the argument parsing.

# Communication skills

I believe this needs to be addressed in the call.

# Concepts

## IaC

IaC is a way to automate the infrastructure through usage of code instead of manual process which can lead the errors.
Some of the benefits are:
  - easily recreate environments
  - limit the configuration errors
  - increases speed of the development
  - improves audit and security

You can have the following types of IaC:

  - Declaritive 
  Here we can define the desired state and execute the code. Good example is terraform.
  - Imperative 
  Define sequence of tasks which is modifing the state of the system.

Another approach we have is the CDK where we have mixture between imperative and declaritive. Examples are Pulumi and AWS CDK where we can use fully functional language like java, python and typscript. This enables the development team to use the same language for development and infrastructure.

Popular infrastructure as a code systems are:
  - Terraform / OpenTofu
  - Pulumi, AWS CDK
  - Ansible, Pupet ( you can use them to manipulate resources but in general they are configurational management systems )
  - Crossplane

The most important when choosing is the availability of ready modules and ease of use. Another point when we should consider the proper tool is the state management. 

## Observability

Mondern observability is based on logs, traces and metrics.

# Logs
Logs are produced by application and can have different levels. The idea is to be able to index the logs and identify problematic areas. In context of microservices/k8s we usually use following system for the logs:

- Loki 
- Elastic search
- Cloudwatch Logs ( aggregates logs for native services or through cloudwatch agent )
- Amazon Opensearch ( it can be used as SIEM but logs needs to be preprocessed to be integrated with it )

# Metrics

Each system provides different metrics like usage of CPU, Memory, Threads and other componets for example JVM. The following systems are used to "scrape" metrics from diffferent pods. Usually these are the measurments that represent the health of the application. Development teams can also create specific metrics.

- Prometheus with Thanos
- Victoria Metrics
- Datadog and other 
- Cloudwatch ( we can find there many metrics that already available for aws resources )

# Traces

Traces are usually data that tracks the application flow. With additional agent in most of the cases we can generate spans that represent actions in the applications. This is very useful in terms of tracing performance issues in contect of microservices and external services.

- Skywalking APM
- Datadog APM
- Opentelemtry ( we can different agents and collectors)
- X-Ray ( in AWS can work as APM )

Basically when we have distributed environment the monitoring is a challenge. Through usage of all pillars of the Observability we can improve the visibility in the communication between the services. This can improve the solving of criticial issues on time and even predict in case of performance degradation is ongoing.


## Security 

Imagine you would join our team and put in charge of securing our AWS infrastructure. What are the first three things that you check, to limit the risk of a breach? Explain why.

Risk of the breach is usually due to badly organized access and controls. Another reason could be unencrypted data at rest or in motion. In next section I have revised few option that can help identify potential threads and identify risk of breach.

1. Security hub is enabled and report of scanning. 

AWS already provides a service(Security Hub) to check CIS compliance and identifies risks in the AWS accounts. It validates through Config and other services for security controls of the environment:

- MFA is enabled for all accounts
- there are no open security groups  (0.0.0.0/0)
- IAM user account access key should be removed
- Strong password policy for all accounts
- Users not used in the last 45 to be deleted
- Least privilege principle is applied on all levels
- Cloud Trail is activated 
- VPC flow logs is activated for tracing of suspicious traffic
- Guard Duty is activated and alerting is organized for cirical threats
- S3 buckets are secured and encrypted (no public access where possible)
- Amazon Inspector is activated 

2. Publicly available resources like Loadbalancers and other systems are protected with WAF. Important step for WAF is to activate the managed rules so we get protection of most common threats and DDOS attacks. This includes:

- Rate limiting
- Bad inputs
- Blocks ips with bad reputation
and other

3. Separation of Production and Non-Production accounts and traffic. We have a possibility that breach can come from internal user or account. Best practice is to use landing zones with AWS Organization and Tower. Here we can apply security policies based on account. Moreover landing zone should support hub and spoke topolgy where network account is dedicated to aggregate traffic. Here we apply AWS Firewall for better control of incoming and outgoing traffic. The accounts for production and non production should be split and access to them is organized through SSO with striclty defined groups of users.