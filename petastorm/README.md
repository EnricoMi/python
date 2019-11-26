# Petastorm

Example code related to Petastorm

## Retry fs open

We want to add retry capabilities to Petastore opening HDFS files.
There are several places where Petastorm accesses HDFS via HadoopFileSystem.open,
so the easiest way to add retries is not to touch Petastorm itself but
HadoopFileSystem.open, which is used by Petastorm for `hdfs://` files.

Install the required packages:

```
pip install -r requirements.txt`
```

Then run `retry_fs_open.py`:

```
$ env ARROW_LIBHDFS_DIR=/usr/hdp/3.1.0.0-78/usr/lib python retry_fs_open.py
19/11/26 19:14:12 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
19/11/26 19:14:13 WARN shortcircuit.DomainSocketFactory: The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
opening /user/spark/petastorm_dataset.parquet/_common_metadata
opening /user/spark/petastorm_dataset.parquet/_common_metadata
opening /user/spark/petastorm_dataset.parquet/_common_metadata
opening /user/spark/petastorm_dataset.parquet/part-00000-9d7849a6-6c21-43fe-ba38-679256fb5c1a-c000.snappy.parquet
opening /user/spark/petastorm_dataset.parquet/part-00000-9d7849a6-6c21-43fe-ba38-679256fb5c1a-c000.snappy.parquet
```

You can see, all calls into HadoopFileSystem.open done by Petastorm will be decorated by a print-line `opening FILE`.

