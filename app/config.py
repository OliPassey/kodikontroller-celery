import os

class CeleryConfig:
    broker_url = os.getenv('BROKER_URL', 'amqp://rabbitmq:5672/kodikontroller')
    result_backend = os.getenv('RESULT_BACKEND', 'rpc://')
    mongodb_settings = {
        'db': os.getenv('MONGO_DB', 'kodikontroller'),
        'host': os.getenv('MONGO_HOST', 'mongodb'),
        'port': int(os.getenv('MONGO_PORT', 27017))
    }
    imports = ('app.tasks', )
    broker_connection_retry_on_startup = os.getenv('BROKER_CONNECTION_RETRY_ON_STARTUP', 'True') == 'True'
    kk_base_url = os.getenv('KK_BASE_URL', 'http://kodikontroller/')
    HOST_STATUS_SCHEDULE_MINUTES = os.getenv('HOST_STATUS_SCHEDULE_MINUTES', '*/5')
