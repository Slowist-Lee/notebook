# 进阶-数据库相关

配置环境：
[MySQL下载及配置](https://blog.csdn.net/qq_42126822/article/details/123168928?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172048888716800188585126%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=172048888716800188585126&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-123168928-null-null.142^v100^pc_search_result_base8&utm_term=MySQL%20Installer&spm=1018.2226.3001.4187)

Tips:

基本语句：

创建新的数据库

```sql
CREATE DATABASE newdatabase;
```

成功应该有如下反应：

```text
Query OK, 1 row affected (0.00 sec)
```

连接已有的`init.sql`文件：

```sql
SOURCE /path/to/your/init.sql;
```

显示所有表

```sql
SHOW TABLES;
```

选择数据库

```sql
USE testdb;
```

查看表的结构

```sql
DESCRIBE table_name;
```

查看表中数据

```sql
SELECT * FROM table_name;
```