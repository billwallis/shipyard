- [BW 10 mins] Which of these has a subtle bug? *A lesson on CTE materialisation*
    - DuckDB SQL:
        ```sql
        /* Filter with LIMIT */
        with foo as (
            select id, random() as val
            from generate_series(1, 100) as gs(id)
        )

        from foo
        order by val desc
        limit 1
        ;

        /* Filter with QUALIFY */
        with foo as (
            select id, random() as val
            from generate_series(1, 100) as gs(id)
        )

        from foo
        qualify val = max(val) over (order by val desc)
        ;

        /* Filter with MAX */
        with foo as (
            select id, random() as val
            from generate_series(1, 100) as gs(id)
        )

        from foo
        where val = (select max(val) from foo)
        ;
        ```
    - Spoiler: https://github.com/duckdb/duckdb/issues/15557
