- [BW 5 mins] Why `1=1` in prod?
  - We all know it's good for toggling filters in development
  - Some people like it for dynamic SQL generation
  - I like it because it keeps the boolean expressions aligned!
  - I also like `0=1` for a combination of `or` expressions
  - I've seen way too many bugs in combining `and` and `or` without brackets. Using `1=1` and `0=1` keeps me defended against them. Example:
    ```sql
    from some_table
    where 1=1
        and expr_1
        and expr_2
        and (0=1
            or expr_3
            or expr_4
            or (1=1
                and expr_5
                and expr_6
            )
        )
    ```
