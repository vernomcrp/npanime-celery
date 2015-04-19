
from celery import Celery

import urllib2

HEADERS={
    'User-Agent': 'Mozilla/5.0'
}

app = Celery('tasks', backend='amqp://', broker='amqp://')


@app.task
def down(fname, url, folder_name):
    real_url = url[1]
    d = {
        'Accept':'image/png,image/*;q=0.8,*/*;q=0.5',
        'Accept-Encoding':'gzip, deflate',
    }
    if url[0] != '': d['Referer'] = url[0]
    HEADERS.update(d)
    try:
        img = urllib2.urlopen(urllib2.Request(real_url, None, HEADERS))
    except Exception as e:
        print 'Cannot proces url %s' % real_url
        return False
    fullname = '%s-%s' % (fname, real_url.split('/')[-1])
    with open('./%s/%s' % (folder_name, fullname), 'wb') as f:
        while True:
            t = img.read(16*1024)
            if not t:break
            f.write(t)
    print 'Writed %s' % fullname
    return True