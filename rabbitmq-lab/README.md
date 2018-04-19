## install 

```
brew install rabbitmq
pip install pika
/usr/local/sbin/rabbitmq-server
```

## 命令介绍

### 启动

```
./sbin/rabbitmq-server -detached
```

### 后台启动

```
./sbin/rabbitmq-server -detached
```

### 查询服务器状态


```
./sbin/rabbitmqctl status

```

### 关闭节点

```
./sbin/rabbitmqctl stop

```

### 关闭 RabbitMQ 应用程序


```
./sbin/rabbitmqctl stop_app

```

### 启动 RabbitMQ 应用程序

```
./sbin/rabbitmqctl start_app

```

### 查看已声明的队列


```
./sbin/rabbitmqctl list_queues

```

### 查看交换器

```
./sbin/rabbitmqctl list_exchanges
```

### 查看绑定

```
./sbin/rabbitmqctl list_bindings

```


## 可靠性

默认情况下 rabbitmq 分发的任务不做持久化，consume 在收到 message 之后 rabbitmq 做了删除，这时候如果 consumer 发生故障则 message will be lost。

rabbitmq 是支持 message ack 的，也即是在 worker 执行完任务之后回发 ack 告知 rabbitmq message 被处理完毕，rabbitmq 才会安全的执行 message delete，如果 worker dies，无论是 worker 自身 dies 还是 connection lost 亦或是 tcp close 导致 message 执行失败，rabbitmq 都会重新对 message 进行 re-queue。


**记住没有 timeout 机制，所以如果出现 worker 大量 dies 的情况，会造成 message 堆积，memory 消耗完毕**

确认机制默认是打开的，如果不需要需要显式关闭。rabbitmq 的确认使用的 Channel 和消息发送是同一 Channel。

## 持久性

rabbitmq 支持消息持久化，这样即使 rabbitmq server crash 了，再次启动不会丢失消息，但是这个不是绝对的，为了保证性能，消息一般会首先写入 cache 然后再同步到磁盘，如果再这样的过程中发生 crash ，消息一样也会 lost，如果需要做强一致性保证使用 https://www.rabbitmq.com/confirms.html

durable 必须在 produce 和 consume 同时执行：This queue_declare change needs to be applied to both the producer and consumer code.


## 公平分发

默认情况下 rabbitmq 分发消息完全是根据进入消息的顺序发送给不同的 consume，它并没有关心已经分发的消息是多少。

This happens because RabbitMQ just dispatches a message when the message enters the queue. It doesn't look at the number of unacknowledged messages for a consumer. It just blindly dispatches every n-th message to the n-th consumer.

如果一个 worker 处理的比较快，得到的消息就多，反之则少，这样会导致一个 worker 特别忙，另一个特别闲。


In order to defeat that we can use the **basic.qos** method with the prefetch_count=1 setting. This tells RabbitMQ not to give more than one message to a worker at a time. Or, in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one. Instead, it will dispatch it to the next worker that is not still busy.

```
channel.basic_qos(prefetch_count=1)

```

告诉 rabbitmq 直到 worker 进行消息确认之前都不再发送新的消息


## exchange 

sender 默认是不直接和 queue 交互，所有 message 都是通过 exchange 进行转发的，sender 甚至不知道 queue 的存在。

exchange 有 4 中类型， direct, topic, headers and fanout。

### fanout

The fanout exchange is very simple. As you can probably guess from the name, it just broadcasts all the messages it receives to all the queues it knows. And that's exactly what we need for our logge。


直接广播 message 到它能接触到的任何 queue

### direct

direct change 可以直接路由 change 指定的 key 和 binding key 相同的 queue

### topic

topic 的 routing key 是按照一定规则进行路由的

- * (star) can substitute for exactly one word.
- # (hash) can substitute for zero or more words.


```
x--> *.*.rabbit Q2
x--> lazy.# Q2
x--> *.orange.* Q1

```

A message with a routing key set to "quick.orange.rabbit" will be delivered to both queues. Message "lazy.orange.elephant" also will go to both of them. On the other hand "quick.orange.fox" will only go to the first queue, and "lazy.brown.fox" only to the second. "lazy.pink.rabbit" will be delivered to the second queue only once, even though it matches two bindings. "quick.brown.fox" doesn't match any binding so it will be discarded.

What happens if we break our contract and send a message with one or four words, like "orange" or "quick.orange.male.rabbit"? Well, these messages won't match any bindings and will be lost



### binding

exchange 是如何知道 queue 的？就是通过 binding 实现，exchange 在 declare 时会指定 routing key，这个 routing key 可以按照规则和 binding 上的 routing key 进行匹配来来路由



