- [BW 5 mins] gitmojis!
    - https://gitmoji.dev/
    - PyCharm plugin (GitToolBox)
- [BW 3 mins]: BigQuery's [WITH expression](https://cloud.google.com/bigquery/docs/reference/standard-sql/operators#with_expression)
    - Sample:
        ```sql
        with example as (select 1 as a, 2 as b)

        select
            a,
            b,
            with (
                x as 9,
                y as a + b,
                x / y
            ) as c
        from example
        ```
