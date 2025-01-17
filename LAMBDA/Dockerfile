FROM amazon/aws-lambda-python:3.11

COPY requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r /tmp/requirements.txt

COPY app.py ./
COPY .aws ./.aws

CMD ["app.lambda_handler"]
