import logging
from datetime import datetime

logfileName = 'testlog_' + datetime.now().strftime('%y%m%d_%H%M%s') + '.log'

logging.basicConfig(
    filename = logfileName,
    level = logging.INFO,
    format = "%(asctime)s %(levelname)s %(message)s",
    encoding = 'utf-8',
    force = True   # 현재 로그 설정 강제화
)


logging.info('[스케줄]로그 시작')

# ... 여러 작업 수행 
logging.warning('경고!!')

logging.info('[스케줄]로그 완료!')