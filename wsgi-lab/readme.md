
wsgi 是 python [pep333](https://www.python.org/dev/peps/pep-0333/) 的一个网关协议 web server gateway interface，提供应用程序和web服务器进行通信的协议规范。

gunicorn 是实现了 wsgi 的一个 web 服务器，他提供多种工作模式，同步、gevent 异步、tornado等不同的工作模式，类似于 nginx master-work 的进程管理方式来保证服务的稳定和性能。

通过 gunicorn 把 nginx 请求交给 flask 来做，在这里 flask 的角色就变成了一个单独处理请求的 web framework，gunicorn 启动的时候回按照 wsgi 的规范将 flask app 导入到 gunicorn 的进程中，按照给定的工作模式进行请求分发的处理。



## start app
start app 

`gunicorn app:app --log-level=debug

`

