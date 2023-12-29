def load_files(spark, file_dir, file_format, header, inferSchema):
    try:
        print("The load_files() is started ...")
        if file_format == 'parquet':
            df = spark.read.format(file_format).load(file_dir)

        elif file_format == 'csv':
            df = spark.read.format(file_format) \
                .options(header=header) \
                .options(inferSchema=inferSchema) \
                .load(file_dir)
    except Exception as exp:
        print("Error in the method load_files(). ")
        raise
    else:
        print(f"The input file {file_dir} is loaded to the data frame")
    return df
