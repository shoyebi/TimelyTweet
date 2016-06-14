__author__ = 'shoyeb'

import oauth2,json

def oauth_req(url, config, http_method="GET", post_body='', http_headers=None):
    twitter_tokens = config.get('twitter_tokens',{})
    CONSUMER_KEY = str(twitter_tokens.get('consumer_key','Lccmq0NMhkg194XA0UWN82lS0'))
    CONSUMER_SECRET = str(twitter_tokens.get('consumer_secret','aq6CM6b7f5iS9jqgSvSmrRr7JqvZJE4AKj6ml7Q5WlVlFxAnqJ'))
    ACCESS_TOKEN = str(twitter_tokens.get('access_token','localhost'))
    ACCESS_TOKEN_SECRET = str(twitter_tokens.get('access_token_secret','8181'))

    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers )
    return content

def get_followers(config,user_id=None,user_name=None,count=10):
    if user_name:
        url = 'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=%s&count=%s'%(user_name,str(count))
    elif user_id:
        url = 'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&user_id=%s&count=%s'%(user_id,str(count))
    else:
        return None
    followers_json = oauth_req(url,config)
    jsonloads = json.loads(followers_json)
    return jsonloads.get("ids",[])

def get_status_updates(config, user_id=None, user_name=None):
    if user_id:
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=%s'%user_id
    elif user_name:
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=%s'%user_name
    else:
        return None
    return oauth_req(url,config)



#Test config
if __name__ == '__main__':
    from config import ConfigManager
    config = ConfigManager.get_instance()
    print get_followers(config,user_name='shoyeb_ibuse')
    #print get_status_updates(config, user_id='102305534')