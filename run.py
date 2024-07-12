from app.celery_app import celery

if __name__ == "__main__":
    argv = [
        'worker',
        '--loglevel=info',
        '--concurrency=4',  # Adjust the concurrency as needed
        '-B'  # This flag starts the beat scheduler within the same process
    ]
    celery.worker_main(argv)
