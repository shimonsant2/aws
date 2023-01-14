import boto3

print('boto3: {}'.format(boto3.__version__))

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

print ("sof")