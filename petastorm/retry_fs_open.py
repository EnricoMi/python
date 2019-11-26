from petastorm import make_reader
from pyarrow.hdfs import HadoopFileSystem


# define how to decorate the open method
def decorate_open(decorated_open):
    def open(self, path, mode='rb', buffer_size=None, replication=None, default_block_size=None):
        print('opening {}'.format(path))
        return decorated_open(self, path, mode=mode, buffer_size=buffer_size, replication=replication, default_block_size=default_block_size)
    return open

# decorate open
HadoopFileSystem.open = decorate_open(HadoopFileSystem.open)

file = 'hdfs://ip-10-1-1-36.example.com/user/spark/petastorm_dataset.parquet'
with make_reader(file, hdfs_driver='libhdfs', pyarrow_serialize=True) as train_reader:
    pass

