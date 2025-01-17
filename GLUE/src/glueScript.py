import sys
import boto3
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args= getResolvedOptions(sys.argv, ['JOB_NAME'])
sc= SparkContext()
glueContext= GlueContext(sc)
spark = glueContext.spark_session
job= Job(glueContext)
job.init(args['JOB_NAME'],args)

s3= boto3.client('s3')
buckets= s3.list_buckets()

for bucket in buckets['Buckets']:
    print(f" {bucket['Name']}")

job.commit()c 
