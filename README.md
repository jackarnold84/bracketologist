# Bracketologist

An app to predict who will win your ESPN March Madness bracket
group by simulating future outcomes.

Automated updates powered by:
- Beautiful Soup
- AWS Lambda
- AWS DynamoDB

https://jackarnold84.github.io/bracketologist/

Setup:
- Add AWS key pair to `loader/credentials.py` and `service/credentials.py`
- Add required information to each `config.*`
- Fetch and store a group + brackets using `loader/load.py`
- Run analysis using the `admin.html` page
