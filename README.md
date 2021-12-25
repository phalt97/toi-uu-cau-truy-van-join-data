# toi-uu-cau-truy-van-join
Hướng dẫn chạy project.
1. Cài đặt PostrgreSQL
2. Import IMDB dataset dựa theo hướng dẫn bên dưới (# join-order-benchmark)
3. Cài đặt Python 3.* và môi trường ảo nếu cần.
4. Clone repository: https://github.com/gregrahn/join-order-benchmark
5. Cài đặt các package cần thiết từ requirements.txt: pip install -r requirements.txt
Bước cuối cùng là chỉnh sửa các biến môi trường ở __init__() and reset() ở thư mục /gym/envs/database/. 


# join-order-benchmark

This package contains the Join Order Benchmark (JOB) queries from:  
"How Good Are Query Optimizers, Really?"  
by Viktor Leis, Andrey Gubichev, Atans Mirchev, Peter Boncz, Alfons Kemper, Thomas Neumann  
PVLDB Volume 9, No. 3, 2015  
[http://www.vldb.org/pvldb/vol9/p204-leis.pdf](http://www.vldb.org/pvldb/vol9/p204-leis.pdf)

### IMDB Data Set
The CSV files used in the paper, which are from May 2013, can be found
at [http://homepages.cwi.nl/~boncz/job/imdb.tgz](http://homepages.cwi.nl/~boncz/job/imdb.tgz)

The license and links to the current version IMDB data set can be
found at [http://www.imdb.com/interfaces](http://www.imdb.com/interfaces)

### Step-by-step instructions
1. download `*gz` files (unpacking not necessary)

  wget ftp://ftp.fu-berlin.de/misc/movies/database/frozendata/*gz
  
2. download and unpack `imdbpy` and the `imdbpy2sql.py` script

  wget https://bitbucket.org/alberanid/imdbpy/get/5.0.zip


3. create PostgreSQL database (e.g., name imdbload):

  createdb imdbload

4. transform `*gz` files to relational schema (takes a while)

  imdbpy2sql.py -d PATH_TO_GZ_FILES -u postgres://username:password@hostname/imdbload

