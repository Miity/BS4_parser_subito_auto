import time

from app.config import logger
from app import main

import asyncio


if __name__=='__main__':
    start_time = time.time()
    i=0
    try:
        while True:
            new_ads = main()
            print('======== CHECK FOR NEW ADS =========')
            
            if len(new_ads) > 0 and i>0:
                from bot.loader import dp
                from bot.utils.notify_admins import send_info
                for car in new_ads:
                    asyncio.run(send_info(dp,car))
                    time.sleep(2)
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