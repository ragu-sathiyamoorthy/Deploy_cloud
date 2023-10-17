from aws_cdk import core
from aws_cdk import aws_s3 as s3

class MyCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket
        s3.Bucket(self, "MyS3Bucket")
