API_TEST_EVENT := service/events/api.json
PROCESSOR_TEST_EVENT := service/events/process.json
KEY_UPDATE_TEST_EVENT := service/events/keyUpdate.json
LOCAL_ENV_FILE := service/events/env.json

default: sam

clean:
	rm -rf .aws-sam/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

sam:
	sam validate --lint
	sam build

invoke-api: sam
	sam local invoke BracketologistApi --event $(API_TEST_EVENT) --env-vars $(LOCAL_ENV_FILE)

invoke-processor: sam
	sam local invoke BracketologistProcessor --event $(PROCESSOR_TEST_EVENT) --env-vars $(LOCAL_ENV_FILE)

invoke-key-update: sam
	sam local invoke BracketologistKeyUpdate --event $(KEY_UPDATE_TEST_EVENT) --env-vars $(LOCAL_ENV_FILE)

serve-local: sam
	sam local start-lambda

deploy: sam
	sam deploy --guided
