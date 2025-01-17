FROM docker.io/amazon/aws-glue-libs:glue_libs_4.0.0_image_01

USER roor

RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3 pandas hvac

COPY wheel/{fileName}  /opt/wheels/
RUN pip3 install /opt/wheels/{fileName}

ENV AWS_REGION= us-east-1

ENTRYPOINT ["/bin/bash"]
