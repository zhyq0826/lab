import glob
import sys
sys.path.append('gen-py')


from entries import 
from entries.ttypes import EntriesResult, Entries, User
from entries.EntriesService import  EntriesService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class EntriesHandler:
    def __init__(self):
        pass

    def query_entries(self, page):
        user = User(userId=123, userName='abc', text='abc')
        as_list = [Entries(title='abc', text='cedf', atime=1477911967.603579, user=user)]
        return EntriesResult(as_list)

if __name__ == '__main__':
    handler = EntriesHandler()
    processor = EntriesService.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)