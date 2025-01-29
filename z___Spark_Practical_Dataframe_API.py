# Databricks notebook source
# MAGIC %md
# MAGIC # **3.Read Data in spark**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Frame reader API

# COMMAND ----------

spark


# COMMAND ----------

flight_df=spark.read.format("csv")\
  .option("header","false")\
    .option("inferschema","false")\
      .option("mode","FAILFAST")\
        .load("/FileStore/tables/flight_data.csv")

flight_df.show(5)

# COMMAND ----------

flight_df_header=spark.read.format("csv")\
  .option("header","true")\
    .option("inferschema","false")\
      .option("mode","FAILFAST")\
        .load("/FileStore/tables/flight_data.csv")

flight_df_header.show(5)

# COMMAND ----------

flight_df_header.printSchema()

# COMMAND ----------

flight_df_header_schemma=spark.read.format("csv")\
  .option("header","true")\
    .option("inferschema","true")\
      .option("mode","FAILFAST")\
        .load("/FileStore/tables/flight_data.csv")

flight_df_header_schemma.show(5)

# COMMAND ----------

flight_df_header_schemma.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC # **4.Schema in Spark**

# COMMAND ----------

flight_df=spark.read.format("csv")\
  .option("header","false")\
    .option("inferschema","false")\
      .schema(my_schema)\
        .option("mode","FAILFAST")\
          .load("/FileStore/tables/flight_data.csv")

flight_df.show(5)

# COMMAND ----------

from pyspark.sql.types import StructType,StructField,StringType,IntegerType
my_schema=StructType(
    [
        StructField('DEST_COUNTRY_NAME',StringType(),True),
        StructField('ORIGIN_COUNTRY_NAME',StringType(),True),
        StructField('COUNT',IntegerType(),True)
    ]
    )

# COMMAND ----------


flight_df=spark.read.format("csv")\
  .option("header","false")\
    .option("inferschema","false")\
      .schema(my_schema)\
        .option("mode","FAILFAST")\ # failing due to FAILFAST MODE AS NULL IS COMING IN RECORD 
          .load("/FileStore/tables/flight_data.csv")

flight_df.show(5)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /FileStore/tables/

# COMMAND ----------


flight_df=spark.read.format("csv")\
                    .option("header","true")\
                    .option("skipRows",1)\
                    .option("inferschema","false")\
                    .schema(my_schema)\
                    .option("mode","PERMISSIVE")\
                    .load("/FileStore/tables/flight_data.csv")
                    #As the csv file had the header included in it but we kept header as false so the first row had header columns as record, so we need to skip 1 row

flight_df.show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC # **5.Handling Corrupted Records in spark**

# COMMAND ----------

employee_df=spark.read.format("csv")\
  .option("header","true")\
    .option("inferschema","true")\
      .option("mode","PERMISSIVE")\
        .load("/FileStore/tables/employee_file.csv")

# id,name,age,salary,address,nominee
# 1,Manish,26,75000,bihar,nominee1
# 2,Nikita,23,100000,uttarpradesh,nominee2
# 3,Pritam,22,150000,Bangalore,India,#####nominee3
# 4,Prantosh,17,200000,Kolkata,India,####nominee4
# 5,Vikash,31,300000,,nominee5

employee_df.show()

# COMMAND ----------

employee_df=spark.read.format("csv")\
  .option("header","true")\
    .option("inferschema","true")\
      .option("mode","DROPMALFORMED")\
        .load("/FileStore/tables/employee_file.csv")

# id,name,age,salary,address,nominee
# 1,Manish,26,75000,bihar,nominee1
# 2,Nikita,23,100000,uttarpradesh,nominee2
# 3,Pritam,22,150000,Bangalore,India,#####nominee3
# 4,Prantosh,17,200000,Kolkata,India,####nominee4
# 5,Vikash,31,300000,,nominee5

employee_df.show()

# COMMAND ----------

employee_df=spark.read.format("csv")\
  .option("header","true")\
    .option("inferschema","true")\
      .option("mode","FAILFAST")\
        .load("/FileStore/tables/employee_file.csv")

# id,name,age,salary,address,nominee
# 1,Manish,26,75000,bihar,nominee1
# 2,Nikita,23,100000,uttarpradesh,nominee2
# 3,Pritam,22,150000,Bangalore,India,#####nominee3
# 4,Prantosh,17,200000,Kolkata,India,####nominee4
# 5,Vikash,31,300000,,nominee5

employee_df.show()

# COMMAND ----------

employee_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Print Corrupted Records

# COMMAND ----------

# PRINT CORRUPTED RECORDS

from pyspark.sql.types import StructField,StructType,StringType,IntegerType

emp_schema=StructType(
    [
        StructField('id',IntegerType(),True),
        StructField("name",StringType(),True),
        StructField("age",IntegerType(),True),
        StructField("salary",IntegerType(),True),
        StructField("address",StringType(),True),
        StructField("nominee",StringType(),True),
        StructField("_corrupt_record",StringType(),True)
    ]
)


# COMMAND ----------

# PRINT CORRUPTED RECORDS
employee_df=spark.read.format("csv")\
  .option("header","true")\
    .option("inferschema","true")\
      .option("mode","Permissive")\
        .schema(emp_schema)\
        .load("/FileStore/tables/employee_file.csv")

# id,name,age,salary,address,nominee
# 1,Manish,26,75000,bihar,nominee1
# 2,Nikita,23,100000,uttarpradesh,nominee2
# 3,Pritam,22,150000,Bangalore,India,#####nominee3
# 4,Prantosh,17,200000,Kolkata,India,####nominee4
# 5,Vikash,31,300000,,nominee5

employee_df.show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Storing Bad Records

# COMMAND ----------

employee_df=spark.read.format("csv")\
  .option("header","true")\
    .option("inferschema","true")\
      .schema(emp_schema)\
        .option("badRecordsPath","/FileStore/tables/bad_records")\
        .load("/FileStore/tables/employee_file.csv")
employee_df.show(truncate=False)      

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /FileStore/tables/bad_records/20250119T134229/bad_records/

# COMMAND ----------

bad_data_df=spark.read.format("json")\
    .load("/FileStore/tables/bad_records/20250119T134229/bad_records/")
bad_data_df.show(truncate=False)       

# COMMAND ----------

# MAGIC %md
# MAGIC # **6.How to read json files in pyspark**

# COMMAND ----------

# MAGIC %md
# MAGIC - File uploaded to /FileStore/tables/multiline_incorrect.json
# MAGIC - File uploaded to /FileStore/tables/multiline_correct.json
# MAGIC - File uploaded to /FileStore/tables/line_delimited_json_extrafield.json
# MAGIC - File uploaded to /FileStore/tables/corrupted_json.json
# MAGIC - File uploaded to /FileStore/tables/line_delimited_json.json

# COMMAND ----------

spark.read.format("json")\
  .option("inferschema","true")\
    .option("mode","PERMISSIVE")\
      .load("/FileStore/tables/line_delimited_json.json").show()

# COMMAND ----------

spark.read.format("json")\
    .option("inferschema","true")\
        .option("mode","PERMISSIVE")\
            .load("dbfs:/FileStore/tables/line_delimited_json_extrafield.json").show()

# {"name":"Manish","age":20,"salary":20000},
# {"name":"Nikita","age":25,"salary":21000},
# {"name":"Pritam","age":16,"salary":22000},
# {"name":"Prantosh","age":35,"salary":25000},
# {"name":"Vikash","age":67,"salary":40000,"gender":"M"}    
# gender column with only 1 actual value and other are nulls
#        

# COMMAND ----------

# line delimited(single line---for each record of table all Key(column):Value(data) pairs in 1 line) json works faster than multiline json(each resords having multiple KV pairs in separate lines)...

#single line--- {"name":"Manish","age":20,"salary":20000}
# multiline---{
#   "name": "Manish",
#   "age": 20,
#   "salary": 20000
# }

# COMMAND ----------

spark.read.format("json")\
    .option("inferschema","true")\
        .option("multiline","true")\
          .option("mode","PERMISSIVE")\
            .load("/FileStore/tables/multiline_correct.json").show()

            # multiline correct is List of Dictionaries
# [
# {
#   "name": "Manish",
#   "age": 20,
#   "salary": 20000
# },
# {
#   "name": "Nikita",
#   "age": 25,
#   "salary": 21000
# }
# ]            

# COMMAND ----------

spark.read.format("json")\
    .option("inferschema","true")\
        .option("multiline","true")\
          .option("mode","PERMISSIVE")\
            .load("/FileStore/tables/multiline_incorrect.json").show()

            # multiline_incorrect is json without a list of dictionaries so only 1 record was parsed

# {
#   "name": "Manish",
#   "age": 20,
#   "salary": 20000
# },
# {
#   "name": "Nikita",
#   "age": 25,
#   "salary": 21000
# }            

# COMMAND ----------

spark.read.format("json")\
    .option("inferschema","true")\
          .option("mode","PERMISSIVE")\
            .load("/FileStore/tables/corrupted_json.json").show(truncate=False)

# {"name":"Prantosh","age":35,"salary":25000},
# {"name":"Vikash","age":67,"salary":40000        curly bracket missing   

# COMMAND ----------

# MAGIC %md
# MAGIC # **7.What is Apache Parquet file**

# COMMAND ----------

#  Spark API format file path
#  dbfs:/FileStore/tables/part_r_00000_1a9822ba_b8fb_4d8e_844a_ea30d0801b9e_gz.parquet
#  ==/FileStore/tables/part_r_00000_1a9822ba_b8fb_4d8e_844a_ea30d0801b9e_gz.parquet

# COMMAND ----------

#reading a parquet file by loading directly
spark.read.parquet("/FileStore/tables/part_r_00000_1a9822ba_b8fb_4d8e_844a_ea30d0801b9e_gz.parquet").show()
#no need of other options for reading parquet file as the the metadata of parquet file is so enriched that there no requirement at all.
#parquet format is structured file format Binary file format(not human readable) and columnar-hybrid(mix of column and rows) based file format

#Hybrid-if 100M records are there then it the data is arranged such that for evry 1lakh records the data will stored  column wise which is called a row group and then a break and then again from 100001 to 200000 record will be arranged in columnar format

# COMMAND ----------

# MAGIC %md
# MAGIC encoding:RUN LENGTH ENCODING(RLE) 01233313
# MAGIC
# MAGIC encoding:BIT PACKED 0,1,2,(3,3),1,3---requires 2 bytes instead of 8 bytes
# MAGIC
# MAGIC Predicate Pushdown- discards rowgroups where data is not in between min and max values
# MAGIC
# MAGIC Projection Pruning-searching only columns that are required
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # **8.How to write Dataframe to disk in spark**

# COMMAND ----------

df_emp=spark.read.format("csv")\
  .option("header","true")\
    .option("inferschema","true")\
      .option("mode","PERMISSIVE")\
        .load("/FileStore/tables/employee.csv")
df_emp.show()        


# COMMAND ----------

df_emp.write.format("csv")\
        .option("header","true")\
        .mode("overwrite")\
        .option("path","/FileStore/tables/csv_write")\
        .save()
#.option("mode","overwrite") is used for reading purposes for writing use .mode("overwrite")

# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables/csv_write"))

# COMMAND ----------

df_emp.repartition(3).write.format("csv")\
        .option("header","true")\
        .mode("overwrite")\
        .option("path","/FileStore/tables/csv_write_1")\
        .save()
# 1 file divided into 3 files

# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables/csv_write_1"))

# COMMAND ----------

spark.read.csv("/FileStore/tables/csv_write_1/part-00001-tid-7427873579321568306-a3be03bf-d631-4f08-97d1-22818a52d2e8-176512-1-c000.csv").show()

# COMMAND ----------

# MAGIC %md
# MAGIC # **Partitioning and Bucketing**

# COMMAND ----------

df_emp.show()

# COMMAND ----------

df_emp.write.format("csv")\
  .option("header","true")\
    .mode("overwrite")\
      .option("path","/FileStore/tables/partition_by_address/")\
        .partitionBy("address")\
          .save()



# COMMAND ----------

dbutils.fs.ls("/FileStore/tables/partition_by_address") # 4 partitions created basesd on country address

# COMMAND ----------

df_emp.write.format("csv")\
  .option("header","true")\
    .mode("overwrite")\
      .option("path","/FileStore/tables/partition_by_id/")\
        .partitionBy("id")\
          .save()


# COMMAND ----------

dbutils.fs.ls("/FileStore/tables/partition_by_id") # optimized partitioning failed as the column on which we partitioned the data doesn't has cardinality(evenly distributed big group of data for each key in the field id unlike address)
#eg set_id={1,2,3,...,15}-->cardinality 15 _____>bucketBy preferred
#eg set_address={INDIA,JAPAN,USA,RUSSIA}--->CARDINALITY 4 ----partitionBy preferred

# COMMAND ----------

#If we want data to be partioned by male and female data in a country then we can partition by address then gender

df_emp.write.format("csv")\
    .option("header","true")\
        .mode("overwrite")\
            .option("path","/FileStore/tables/partition_by_address_gender")\
                .partitionBy("address","gender")\
                    .save()

# COMMAND ----------

dbutils.fs.ls("/FileStore/tables/partition_by_address_gender/address=INDIA/")

# COMMAND ----------

dbutils.fs.ls("/FileStore/tables/partition_by_address_gender/address=INDIA//gender=f/")

# COMMAND ----------

df_emp.write.format("csv")\
    .option("header","true")\
        .mode("overwrite")\
            .option("path","/FileStore/tables/bucket_by_id/")\ #shdjdj
                .bucketBy(3,'id')\
                    .saveAsTable("bucket_by_id_table")
#need to to do saveAsTable for bucketBy        

# COMMAND ----------

dbutils.fs.ls("/FileStore/tables/bucket_by_id/")

# COMMAND ----------

# MAGIC %md
# MAGIC # **10.How to create data frame in spark**

# COMMAND ----------

 data=[('name'      ,   'varchar'),    
 ('continent' ,   'varchar'),    
 ('area'      ,   'int'    ),    
 ('population',   'int'    ),    
 ('gdp'       ,   'bigint' )  ]

# COMMAND ----------

my_schema=['column','datatype']

# COMMAND ----------

spark

# COMMAND ----------

spark.createDataFrame(data=data,schema=my_schema).show()

# COMMAND ----------

