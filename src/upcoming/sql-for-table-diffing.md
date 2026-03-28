- [BW 5 mins] One of my favourite SQL queries
    - Set-based SQL for diffing tables:
        ```sql
            (select * from old except select * from new)
        union all
            (select * from new except select * from old)
        order by all
        ```
