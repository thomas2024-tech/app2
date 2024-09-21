import redis

def publish_version(channel, appname, version_number):
    # Connect to the local Redis instance
    r = redis.Redis(host='localhost', port=6379, db=0)
    
    # Combine app name and version number into one message
    message = f"{appname} version {version_number}"
    
    # Publish the message to the Redis channel
    r.publish(channel, message)
    
    print(f'Published version {version_number} of app {appname} to channel {channel}')

if __name__ == "__main__":
    publish_version('version_channel', 'app2', '1.2')