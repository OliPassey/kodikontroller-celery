# kodikontroller-celery
Schedule runner component of Kodi Kontroller (requires Kodi Kontroller, MongoDB & RabbitMQ)  

## Docker
Pull from docker olipassey/kodikontroller-celery

Set the following docker environment variables;

- BROKER_URL - eg. amqp://rabbitmq:5672/kodikontroller
- MONGO_HOST - eg. IP or Hostname of your MongoDB
- MONGO_PORT - eg. Only required if you run a non-standard Mongo Port
- KK_BASE_URL - eg. Site URL of your Kodi Kontroller instance https://kodi.domain.com/
- HOST_STATUS_SCHEDULE_MINUTES - eg. */1 if you want the host check to run every 1 minute, default is 5

## RabbitMQ
You should create a new user and vhost in your RabbitMQ instance and add those details as required to the above config.  

## Functionality
- [x] Call /admin/host_status every X minutes
- [ ] Check schedule for playlist items to be triggered
