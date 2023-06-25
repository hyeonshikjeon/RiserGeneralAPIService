from celery import Celery

celery_app = Celery('project',
                    broker="amqp://general:general123@localhost:5672/general_host",
                    backend='rpc://',
                    include=['project.app'])
