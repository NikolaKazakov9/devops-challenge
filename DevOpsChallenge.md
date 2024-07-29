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
  - Ansible, Pupet 
  - Crossplane

The most important when choosing is the availability of ready modules and ease of use. Another point when we should consider the proper tool is the state management. 

## Observability

Mondern observability is based on logs, traces and metrics. 

# Logs
Logs are produced by application and can have different levels. The idea is to be able to index the logs and identify problematic areas. In context of microservices/k8s we usually use following system for the logs:

- Loki 
- Elastic search

# Metrics

Each system provides different metrics like usage of CPU, Memory, Threads and other componets for example JVM. The following systems are used to "scrape" metrics from diffferent pods. Usually these are the measurments that represent the health of the application. Development teams can also create specific metrics.

- Prometheus with Thanos
- Victoria Metrics
- Datadog and other 

# Traces

Traces are usually data that tracks the application flow. With additional agent in most of the cases we can generate spans that represent actions in the applications. This is very useful in terms of tracing performance issues in contect of microservices and external services.

- Skywalking APM
- Datadog APM
- Opentelemtry ( we can different agents and collectors)

Basically when we have distributed environment the monitoring is a challenge. Through usage of all pillars of the Observability we can improve the visibility in the communication between the services. This can improve the solving of criticial issues on time and even predict in case of performance degradation is ongoing.

## Security 

Imagine you would join our team and put in charge of securing our AWS infrastructure. What are the first three things that you check, to limit the risk of a breach? Explain why.

I would check the following systems in AWS:

1. Security hub is enabled and report of scanning. 

AWS already provides a system to check against CIS cerfication and identifies risks in the AWS accounts. It includes many best practicdes:

- MFA 
- open security groups  (0.0.0.0/0)
- IAM accounts instead of rules and policies
- EC2 with direct public access without protection
- least privilege 

2. Publicly available resources like Loadbalancers and other systems are protected with WAF. Usually we use Hub and Spoke accounts with firewalls to protect outgoing and incoming traffic. Production, Staging and Development are in different groups and networks.

3. SSO is enabled with strict policies are applied for accesing multiple accounts. Production accounts are restricted with proper groups and only authroized persons have access to them.