import time
from app.config import logger
from app import main
import asyncio

from bot.loader import dp
from bot.utils.notify_admins import send_info


if __name__=='__main__':
    start_time = time.time()
    try:
        i=0
        while True:
            logger.info(f'======== LOOP NUMBER: {i} =========')
            logger.info('======== CHECK FOR NEW ADS =========')
            new_ads = main()
            logger.info(f'======== found {len(new_ads)} new ads =========')
            for car in new_ads:
                if i>0:
                    asyncio.run(send_info(dp,car))
                    time.sleep(4)
            i+=1
            time.sleep(600)

    except KeyboardInterrupt:
        logger.info('=== Script has been stopped manually! ===')
    except Exception as e:  # pylint: disable=broad-except
        logger.exception(e)
    else:
        logger.info('=== Script has been finished successfully ===')
    finally:
        logger.info('=== Operating time is %s seconds ===', (time.time() - start_time))
