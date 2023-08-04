from celery import Celery

app = Celery('project',
             broker='amqp://riser_user:riser_pw@riserrabbitmq:5672',
             backend='rpc://'
             )

app.conf.update(
    result_expires=3600
)

if __name__ == '__main__':
    app.start()
