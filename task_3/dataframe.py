from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType, StructField, StructType


spark = SparkSession.builder.appName("ProductCategory").getOrCreate()


def get_product_category_pairs(products_df, categories_df, relations_df):
    """
    Возвращает все пары «Имя продукта – Имя категории» и продукты без категорий

    Parameters:
    products_df (DataFrame): Датафрейм с продуктами (должен содержать колонки 'product_id', 'product_name')
    categories_df (DataFrame): Датафрейм с категориями (должен содержать колонки 'category_id', 'category_name')
    relations_df (DataFrame): Датафрейм со связями (должен содержать колонки 'product_id', 'category_id')

    Returns:
    DataFrame: Результирующий датафрейм с парами и продуктами без категорий
    """

    product_category_pairs = (
        relations_df.join(products_df, "product_id", "inner")
        .join(categories_df, "category_id", "inner")
        .select("product_name", "category_name")
    )

    products_without_categories = (
        products_df.join(relations_df, "product_id", "left_anti")
        .select("product_name")
        .withColumn("category_name", F.lit(None).cast(StringType()))
    )

    result_df = product_category_pairs.union(products_without_categories)

    return result_df


products_data = [(1, "Ноутбук"), (2, "Мышь"), (3, "Клавиатура"), (4, "Наушники"), (5, "Стол"), (6, "Стул")]

categories_data = [(1, "Электроника"), (2, "Компьютерная техника"), (3, "Периферия"), (4, "Мебель")]

relations_data = [
    (1, 1),  # Ноутбук -> Электроника
    (1, 2),  # Ноутбук -> Компьютерная техника
    (2, 3),  # Мышь -> Периферия
    (3, 3),  # Клавиатура -> Периферия
    (4, 1),  # Наушники -> Электроника
    (4, 3),  # Наушники -> Периферия
    # Стол и Стул не имеют категорий
]

products_schema = StructType(
    [StructField("product_id", StringType(), True), StructField("product_name", StringType(), True)]
)

categories_schema = StructType(
    [StructField("category_id", StringType(), True), StructField("category_name", StringType(), True)]
)

relations_schema = StructType(
    [StructField("product_id", StringType(), True), StructField("category_id", StringType(), True)]
)


products_df = spark.createDataFrame(products_data, products_schema)
categories_df = spark.createDataFrame(categories_data, categories_schema)
relations_df = spark.createDataFrame(relations_data, relations_schema)


print("Продукты:")
products_df.show()

print("\nКатегории:")
categories_df.show()

print("\nСвязи:")
relations_df.show()

result_df = get_product_category_pairs(products_df, categories_df, relations_df)

print("\nРезультат (пары продукт-категория и продукты без категорий):")
result_df.show()
