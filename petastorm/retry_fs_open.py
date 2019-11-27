from petastorm import make_reader
from pyarrow.hdfs import HadoopFileSystem
import random
import tenacity


# define how to decorate the open method
def decorate_open(decorated_open):
    @tenacity.retry
    def open(self, path, mode='rb', buffer_size=None, replication=None, default_block_size=None):
        print('opening {}'.format(path))
        if random.random() < 0.5:
            raise Exception()
        return decorated_open(self, path, mode=mode, buffer_size=buffer_size, replication=replication, default_block_size=default_block_size)
    return open


# define how to decorate the open method
def retry_open(decorated_open, retry):
    def open(self, path, mode='rb', buffer_size=None, replication=None, default_block_size=None):
        print('opening {}'.format(path))
        return retry.call(decorated_open, self, path, mode=mode, buffer_size=buffer_size, replication=replication, default_block_size=default_block_size)
    return open


# decorate open
retry = tenacity.Retrying()
HadoopFileSystem.open = retry_open(HadoopFileSystem.open, retry)

file = 'hdfs://ip-10-1-1-36.example.com/user/spark/petastorm_dataset.parquet'
with make_reader(file, hdfs_driver='libhdfs', pyarrow_serialize=True) as train_reader:
    pass
