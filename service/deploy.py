import io
import os
import json
from zipfile import ZipFile
from boto3.session import Session
import credentials

# Updates all lambdas in the lambdas/ directory
# aws credentials must be defined in credentials.py

session = Session(
    aws_access_key_id=credentials.aws_access_key,
    aws_secret_access_key=credentials.aws_secret_access_key,
    region_name=credentials.aws_region
)
aws_lambda = session.client('lambda')
print('--> AWS SDK Connected')


def files_to_zip(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            full_path = os.path.join(root, f)
            archive_name = full_path[len(path) + len(os.sep):]
            yield full_path, archive_name


def make_zip_file_bytes(path):
    buf = io.BytesIO()
    with ZipFile(buf, 'w') as z:
        for full_path, archive_name in files_to_zip(path=path):
            z.write(full_path, archive_name)
    return buf.getvalue()


def update_lambda(lambda_name, lambda_code_path):
    if not os.path.isdir(lambda_code_path):
        raise ValueError('Lambda directory does not exist: %s' %
                         lambda_code_path)
    print('\n--> Updating %s' % lambda_name)
    status = aws_lambda.update_function_code(
        FunctionName=lambda_name,
        ZipFile=make_zip_file_bytes(path=lambda_code_path)
    )
    print(json.dumps(status, indent=2))


# iterate and call update for all lambdas in lambdas/ directory
assert(os.path.isdir('service/lambdas/'))
for dir_name in os.scandir('service/lambdas/'):
    lambda_name = dir_name.name
    lambda_code_path = 'service/lambdas/%s' % lambda_name
    update_lambda(lambda_name, lambda_code_path)
