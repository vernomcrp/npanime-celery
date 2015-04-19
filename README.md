# npanime-celery
User should have installed rabbit-mq, celery

## How to use
Start rabbit-mq, start worker by
>>> celery -A tasks worker --loglevel=info
Then start script
>>> python npanime.py <target link> <target folder>
