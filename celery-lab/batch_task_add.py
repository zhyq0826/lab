from celery import group, chain
from proj.celery import app


def main():
    for i in range(100000):
        app.send_task(
            'proj.add',
            args=(1, 2),
        )


if __name__ == '__main__':
    # redis 90s
    # rabbitmq 89s
    main()
