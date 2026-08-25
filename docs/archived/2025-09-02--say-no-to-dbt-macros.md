- [BW 10 mins, 5 mins debate] Say 🙅 to dbt macros
    - https://www.tobikodata.com/blog/traps-and-pitfalls-of-using-sql-with-jinja
        - Side note: parameters (e.g. [in SQLite](https://www.sqlite.org/lang_expr.html#varparam)) and prepared statements (e.g. [in PostgreSQL](https://www.postgresql.org/docs/current/sql-prepare.html))
    - Super verbose in the wrong way:
        - https://medium.com/@george.apps_98339/building-an-effective-model-for-product-lifecycle-data-with-dbt-7b959c4c8836
    - Lack of testing support (community support exists, e.g. [pytest-dbt-core](https://github.com/godatadriven/pytest-dbt-core))
    - Developer experience is 🤮
    - Can be partially improved with [dbt-py](https://github.com/billwallis/dbt-py) (custom Python "macros")
    - Best option is usually to stick with normal SQL, or use SQLMesh 👀
    - Complementary reasons:
        > - Analysts find it difficult to understand what is going on, and depending on who will manage the code I lean towards ease of use rather than saving rows
        > - sql/dbt are vehicles for storing business logic primarily, and when that is abstracted away then it becomes harder to quickly read & understand in general
        > - Debugging jinja sucks
        > - Unit testing is difficult from my admittedly limited experience
        > - IDE support for Jinja is bad ( I could probably make it better)
        > - 'Vendor' lock in making it harder to port code around
    - The main "pro" (IMO) to using macros is to override existing dbt behaviour
