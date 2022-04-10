# import the JSON utility package since we will be working with a JSON object
import json
import boto3

aws_session = boto3.Session()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
s3_client = boto3.client("s3")
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")
S3_BUCKET_NAME = 'sinaroundu-bucket'
facility2table = {"Carpark": "Carpark", "Park": "Park", "Preschool": "Center", "Hawker": "Hawker",
                  "RentFlat": "Rent_out_of_flats", "ResaleFlat": "Resale_flat_prices"}
keys_to_post = {
    "Carpark": ['short_term_parking', 'car_park_type', 'free_parking', 'night_parking', 'type_of_parking_system', 'lat',
                'long', 'address'],
    "Park": ["park_id", "name", "lon", "lat"],
    "Center": ['centre_name', 'district', 'lat', 'long', 'second_languages_offered', 'postal_code', 'centre_website',
               'government_subsidy', 'centre_email_address', 'weekday_full_day', 'food_offered'],
    "Hawker": ['latitude_hc', 'longitude_hc', 'name', 'no_of_food_stalls', 'q1_cleaningstartdate', 'q1_cleaningenddate',
               'q2_cleaningstartdate', 'q2_cleaningenddate', 'q3_cleaningstartdate', 'q3_cleaningenddate',
               'q4_cleaningstartdate', 'q4_cleaningenddate'],

}


def lambda_handler(event, context):
    # get table name
    FACILITY_NAME = event["facility"]
    TABLE_NAME = facility2table[FACILITY_NAME]
    # get data
    # price table
    if TABLE_NAME == "Rent_out_of_flats" or TABLE_NAME == "Resale_flat_prices":
        BUCKET_NAME = 'sinaroundu-bucket'
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=TABLE_NAME + '.json')
        body = json.load(response["Body"])
        try:
            key = list(set(body.keys()) - set(["district", 'month']))[0]
        except:
            return {"status": "200",
                    "keys": ["na"],
                    "result": ["na"]
                    }
        # print(body.keys())
        result = []
        for i in range(len(body['district'])):
            _id = body['district'][str(i)]
            if _id == int(event['district']):
                result.append({'month': body['month'][str(i)], key: float("{:.2f}".format(float(body[key][str(i)])))})
        return {"status": "200",
                "keys": list(result[0].keys()),
                "result": result
                }
    # other table
    try:
        response = dynamodb_client.query(
            TableName=TABLE_NAME,
            KeyConditionExpression='district = :district',
            ExpressionAttributeValues={
                ':district': {'N': event["district"]}
            }
        )
        # data cleaning
        keys_list = keys_to_post[TABLE_NAME]
        remove_list = set(response["Items"][0].keys()) - set(keys_list)
        for ele_dict in response["Items"]:
            for key in remove_list:
                ele_dict.pop(key, None)
        return {"status": "200",
                "keys": list(response["Items"][0].keys()),
                "result": str(response["Items"])
                }
    except:
        response["Items"] = "na"
        return {"status": "200",
                "keys": ["na"],
                "result": str(response["Items"])
                }