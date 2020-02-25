import json
import boto3
import slack

client = boto3.client('ec2', region_name='REGION')
token = '[YOUR TOKEN]'
sc = slack.WebClient(token=token)
channel = '[CHANNEL]'
# all_volume = []

next_token = None
while True:
    if next_token:
        volumes = client.describe_volumes(NextToken = next_token)
    else:
        volumes = client.describe_volumes()
    next_token = volumes.get('nextToken', None)
    for volume in volumes['Volumes']:
        if volume['State'] != "in-use":
            state = volume['State']
            volume_id = volume['VolumeId']
            msg = "This volume `{}` is `{}` on `euw-1` region".format(volume_id, state)
            sc.chat_postMessage(channel=channel,
                                text=msg, username='AWS-EBS Alert ',
                                icon_emoji=':robot_face:')
#             all_volume.append(volume_id)
    if not next_token or len(volumes) == 0:
        break;
print(msg)