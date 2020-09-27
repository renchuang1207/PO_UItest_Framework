import os
import configparser

current_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_dir,'..','config','config')
class ConfigUtils(object):
    def __init__(self,path = config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path,encoding='utf-8')

    @property
    def url(self):
        url_value = self.cfg.get('default','URL')
        return url_value

    @property
    def testdata_path(self):
        testdata_path_value = self.cfg.get('default','testdata_path')
        return testdata_path_value

    @property
    def driver_path(self):
        driver_path_value = self.cfg.get('default', 'driver_path')
        return driver_path_value

    @property
    def driver_name(self):
        driver_name_value = self.cfg.get('default', 'driver_name')
        return driver_name_value

    @property
    def timeout(self):
        driver_name_value = float(self.cfg.get('default', 'time_out'))
        return driver_name_value

    @property
    def screenshot_path(self):
        screen_shot_path_value = self.cfg.get('default', 'screen_shot_path')
        return screen_shot_path_value

    @property
    def user_name(self):
        user_name_value = self.cfg.get('default', 'user_name')
        return user_name_value

    @property
    def password(self):
        psssword_value = self.cfg.get('default', 'password')
        return psssword_value

    @property
    def case_path(self):
        case_path_value = self.cfg.get('default', 'case_path')
        return case_path_value

    @property
    def report_path(self):
        report_path_value = self.cfg.get('default', 'report_path')
        return report_path_value


local_config = ConfigUtils()

if __name__ == '__main__':
    config = ConfigUtils()
    print(local_config.testdata_path)

