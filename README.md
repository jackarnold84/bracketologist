# Bracketologist

An app to predict who will win your ESPN March Madness bracket group by simulating future outcomes.

https://jackarnold84.github.io/bracketologist/

![Bracketologist Logo](/static/images/icon.png)

### Components

Components:
- **Loader** - python script to load bracket selections into DB
- **KeyUpdate** - periodically checks for game updates using ESPN scoreboard API
- **Processor** - run simulations for the remaining bracket
- **Api** - GET endpoint for serving data to UI
- **BracketDB** - store individual bracket selections
- **GroupDB** - store analysis for each bracket group
- **UI** - Basic HTML+CSS+JS for displaying results

Backend deployed with AWS Serverless:
- Lambda
- DynamoDB
- API Gateway
- EventBridge

![Bracketologist Infra](/static/images/infra-diagram.png)

Setup:
- Add required information to each `config.*` file
- Fetch and store a group + brackets using `python -m loader.load <group-tag>`
- Use [Makefile](/Makefile) to build and deploy AWS infra
