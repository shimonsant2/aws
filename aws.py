from typing import List, Any

import boto3

# get all ec2 instances
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

# get all users from the account
iam = boto3.client('iam')
for user in iam.list_users()['Users']:
    print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
        user['UserName'],
        user['UserId'],
        user['Arn'],
        user['CreateDate']
    )
    )

# the user boto3 using
print(iam.get_user())

# list all users permissions by policies
for user_detail in iam.get_account_authorization_details(Filter=['User'])['UserDetailList']:
    policyname: list[Any] = []
    policyarn = []
    # find each policy attached to the user
    for policy in user_detail['AttachedManagedPolicies']:
        policyname.append(policy['PolicyName'])
        policyarn.append(policy['PolicyArn'])
        # print user details
    print("\nUser: {0}\nUserID: {1}\nPolicyName: {2}\nPolicyARN: {3}\n".format(
            user_detail['UserName'],
            user_detail['UserId'],
            policyname,
            policyarn
        )
    )
