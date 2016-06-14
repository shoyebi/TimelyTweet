__author__ = 'shoyeb'

import json,datetime
from datetime import datetime
from server_handler import ServerHandler
from timetwitter.common import utils
from timetwitter.common.log import Logger

logging = Logger.getLogger()

class TweetTimeHandler(ServerHandler):
    hmap_time=None
    hmap_day=None

    def __init__(self, app):
        super(TweetTimeHandler, self).__init__(app)
        self.hmap_time={}
        self.hmap_day={}


    def get_best_time_and_day(self, user_id=None, user_name=None):
        followers_ids = utils.get_followers(self.config, user_id,user_name)
        logging.debug("follower_ids : %s"%str( followers_ids))
        for id in followers_ids:
            status_updates = utils.get_status_updates(self.config, user_id=id)
            self.extract_time_into_dict(status_updates)
        logging.debug("hmap_time : %s"% str(self.hmap_time))
        logging.debug("hmap_day : %s"% str(self.hmap_day))
        return self.get_max_time_hmap()

    def get_max_time_hmap(self):
        max_time=0
        max_day=0
        mav_value=0
        for key,value in self.hmap_time.iteritems():
            if value>mav_value:
                max_time=key
                mav_value = value
        mav_value=0
        for key,value in self.hmap_day.iteritems():
            if value>mav_value:
                max_day=key
                mav_value = value
        logging.debug("max_time : %s"% str(max_time))
        max_day = str(max_day)
        logging.debug("max_day : %s(%s)"% (utils.DAY_MAP.get(max_day),max_day))
        max_time = str(max_time)+' hrs'
        return max_time, utils.DAY_MAP.get(max_day)

    def extract_time_into_dict(self, status_updates):
        if(not status_updates):
            return
        try:
            aj = json.loads(status_updates)
        except Exception as e:
            logging.error("caught exception "+str(e))
        for i in aj:
            try:
                if(i.get('created_at') is None):
                    continue
            except AttributeError as aerr:
                logging.error('AttributeError : ' + str(i))
                continue
            created_at = str(i.get('created_at'))
            created_at = created_at[:19] + created_at[25:]
            date_object = datetime.strptime(created_at,'%a %b %d %H:%M:%S %Y')
            val = self.hmap_time.get(str(date_object.hour), None)
            if val is None:
                self.hmap_time.update({str(date_object.hour): 1})
            else:
                val = val + 1
                self.hmap_time.update({str(date_object.hour): val})

            val = self.hmap_day.get(str(date_object.weekday()), None)
            if val is None:
                self.hmap_day.update({str(date_object.weekday()): 1})
            else:
                val = val + 1
                self.hmap_day.update({str(date_object.weekday()): val})

