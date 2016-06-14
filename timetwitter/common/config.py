__author__ = 'shoyeb'
import yaml
import os
from gevent import lock
from os import  path

class ConfigManager(object):
    config_obj = None
    _lock = lock.RLock()


    @classmethod
    def load(cls):
        default = os.path.join(path.dirname(path.dirname(path.abspath(__file__))),os.path.pardir,'conf/config.yaml')
        dataMap = yaml.load(open(default))
        return dataMap



    @classmethod
    def get_instance(cls):
        if not cls.config_obj:
            with cls._lock:
                if not cls.config_obj:
                    cls.config_obj = cls.load()
        return cls.config_obj


if __name__ == '__main__':
    config = ConfigManager.get_instance()
    print config