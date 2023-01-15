import boto3


print('boto3: {}'.format(boto3.__version__) )
client = boto3.client('ce')
# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

response = client.get_cost_and_usage_with_resources(
    TimePeriod={
        'Start': 'string',
        'End': 'string'
    },
    Granularity='DAILY' | 'MONTHLY' | 'HOURLY',
    Filter={
        'Or': [
            {'... recursive ...'},
        ],
        'And': [
            {'... recursive ...'},
        ],
        'Not': {'... recursive ...'},
        'Dimensions': {
            'Key': 'AZ' | 'INSTANCE_TYPE' | 'LINKED_ACCOUNT' | 'LINKED_ACCOUNT_NAME' | 'OPERATION' | 'PURCHASE_TYPE' | 'REGION' | 'SERVICE' | 'SERVICE_CODE' | 'USAGE_TYPE' | 'USAGE_TYPE_GROUP' | 'RECORD_TYPE' | 'OPERATING_SYSTEM' | 'TENANCY' | 'SCOPE' | 'PLATFORM' | 'SUBSCRIPTION_ID' | 'LEGAL_ENTITY_NAME' | 'DEPLOYMENT_OPTION' | 'DATABASE_ENGINE' | 'CACHE_ENGINE' | 'INSTANCE_TYPE_FAMILY' | 'BILLING_ENTITY' | 'RESERVATION_ID' | 'RESOURCE_ID' | 'RIGHTSIZING_TYPE' | 'SAVINGS_PLANS_TYPE' | 'SAVINGS_PLAN_ARN' | 'PAYMENT_OPTION' | 'AGREEMENT_END_DATE_TIME_AFTER' | 'AGREEMENT_END_DATE_TIME_BEFORE' | 'INVOICING_ENTITY' | 'ANOMALY_TOTAL_IMPACT_ABSOLUTE' | 'ANOMALY_TOTAL_IMPACT_PERCENTAGE',
            'Values': [
                'string',
            ],
            'MatchOptions': [
                'EQUALS' | 'ABSENT' | 'STARTS_WITH' | 'ENDS_WITH' | 'CONTAINS' | 'CASE_SENSITIVE' | 'CASE_INSENSITIVE' | 'GREATER_THAN_OR_EQUAL',
            ]
        },
        'Tags': {
            'Key': 'string',
            'Values': [
                'string',
            ],
            'MatchOptions': [
                'EQUALS' | 'ABSENT' | 'STARTS_WITH' | 'ENDS_WITH' | 'CONTAINS' | 'CASE_SENSITIVE' | 'CASE_INSENSITIVE' | 'GREATER_THAN_OR_EQUAL',
            ]
        },
        'CostCategories': {
            'Key': 'string',
            'Values': [
                'string',
            ],
            'MatchOptions': [
                'EQUALS' | 'ABSENT' | 'STARTS_WITH' | 'ENDS_WITH' | 'CONTAINS' | 'CASE_SENSITIVE' | 'CASE_INSENSITIVE' | 'GREATER_THAN_OR_EQUAL',
            ]
        }
    },
    Metrics=[
        'string',
    ],
    GroupBy=[
        {
            'Type': 'DIMENSION' | 'TAG' | 'COST_CATEGORY',
            'Key': 'string'
        },
    ],
    NextPageToken='string'
)

print(response)

print("sof")
