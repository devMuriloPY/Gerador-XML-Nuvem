import glob
import logging
import os
import sys
import colorlog
from datetime import date
from app.utils import exists, from_asset, get_asset_path, getAsset

class Log:

    def init(self):
        logger = logging.getLogger('')

        today = str(date.today())
        logFolder = f'logs/xml_{today}.log'

        if not exists(from_asset(__file__, logFolder)):
            with open(from_asset(__file__, logFolder), 'w') as f:
                f.write('')

        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(from_asset(__file__, logFolder))
        sh = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
        fh.setFormatter(formatter)
        sh.setFormatter(colorlog.ColoredFormatter(
            '%(log_color)s [%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S'))
        logger.addHandler(fh)
        logger.addHandler(sh)

    def delete_old_logs(self, days_to_keep=2):
        log_folder = get_asset_path()+"logs/"
        log_files = glob.glob(os.path.join(log_folder, "xml_*.log"))
        now = date.today()

        for log_file in log_files:
            file_date_str = os.path.basename(log_file)[4:-4]  # Extract date from file name
            file_date = date.fromisoformat(file_date_str)
            days_difference = (now - file_date).days

            if days_difference > days_to_keep:
                os.remove(log_file)
                logging.info(f"Deleted old log file: {log_file}")