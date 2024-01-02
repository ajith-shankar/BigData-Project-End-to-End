import logging
import logging.config
from pyspark.sql.functions import upper, lit, regexp_extract, col, concat_ws, when, count, isnan, when, avg, coalesce, \
    round
from pyspark.sql.window import Window

# load the logging configuration file
logging.config.fileConfig(fname='../utils/logging_to_file.conf')
# custom logger
logger = logging.getLogger(__name__)


def perform_data_clean(df1, df2):
    ### clean city DataFrame
    # 1 select only required columns
    # 2 Convert city, state and country fields to upper case
    try:
        logger.info(f"perform_data_clean() is started for df_city dataframe...")
        df_city_sel = df1.select(upper(df1.city).alias("city"),
                                 df1.state_id,
                                 upper(df1.state_name).alias("state_name"),
                                 upper(df1.county_name).alias("county_name"),
                                 df1.population,
                                 df1.zips)

        ### clean fact DataFrame
        # 1 select only required columns
        # 2 Rename the columns
        logger.info(f"perform_data_clean() is started for df_fact dataframe...")
        df_fact_sel = df2.select(df2.npi.alias("presc_id"), df2.nppes_provider_last_org_name.alias("presc_lname"), \
                                 df2.nppes_provider_first_name.alias("presc_fname"),
                                 df2.nppes_provider_city.alias("presc_city"),
                                 df2.nppes_provider_state.alias("presc_state"),
                                 df2.specialty_description.alias("presc_spclt"), df2.year_exp.alias("presc_yop"),
                                 df2.drug_name, df2.total_claim_count.alias("trx_cnt"), df2.total_day_supply,
                                 df2.total_drug_cost)

        # 3 Add a county field 'USA'
        df_fact_sel = df_fact_sel.withColumn("country_name", lit("USA"))

        # 4 Clean years_of_exp field
        pattern = '\d+'
        idx = 0
        df_fact_sel = df_fact_sel.withColumn("presc_yop", regexp_extract(col("presc_yop"), pattern, idx))

        # 5 Convert the years_of_exp datatype from string to Number
        df_fact_sel = df_fact_sel.withColumn("presc_yop", col("presc_yop").cast("int"))

        # 6 Combine Frist_Name and Last_Name
        df_fact_sel = df_fact_sel.withColumn("presc_fullName", concat_ws(" ", "presc_fname", "presc_lname"))
        df_fact_sel = df_fact_sel.drop("presc_fname", "presc_lname")  # we don't need these two columns

        # 8 Delete the records where the PRESC_ID is NULL
        df_fact_sel = df_fact_sel.dropna(subset="presc_id")

        # 9 Delete the records where the DRUG_NAME is NULL
        df_fact_sel = df_fact_sel.dropna(subset="drug_name")

        # 10 Impute TRX_CNT where it is Null as avg of trx_cnt for the prescriber
        spec = Window.partitionBy("presc_id")
        df_fact_sel = df_fact_sel.withColumn("trx_cnt", coalesce("trx_cnt", round(avg("trx_cnt").over(spec))))
        df_fact_sel = df_fact_sel.withColumn("trx_cnt", col("trx_cnt").cast('integer'))

        # 7 Check and clean all the Null and NaN values
        df_fact_sel.select(
            [count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in df_fact_sel.columns])


    except Exception as exp:
        logger.error("Error in the method perform_data_clean(). " + str(exp), exc_info=True)
        raise
    else:
        logger.info("perform_data_clean() is completed.")

    return df_city_sel, df_fact_sel
