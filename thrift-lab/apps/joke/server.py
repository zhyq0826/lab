import glob
import sys
sys.path.append('gen-py')
import logging


from entries.ttypes import EntriesResult, Entries, User
from entries import Joke

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class JokeHandler:
    def __init__(self):
        pass

    def query_entries(self, page):
        try:
            user = User(userId=123, userName='abc', text='abc')
            logging.info(user)
            return [Entries(title='abc', text='cedf', atime=1477911967.603579, user=user)]
        except Exception, e:
            logging.exception(e)

if __name__ == '__main__':
    handler = JokeHandler()
    processor = Joke.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(
    #     processor, transport, tfactory, pfactory)
   
    print('Starting the server...')
    server.serve()
    print('done.')