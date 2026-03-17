- [BW 5 mins] Shell commands in `.envrc`
    - ...and how to hide annoying dbt warnings
    - direnv ♥️ 1password
    - Example of an `.envrc` file:
        ```shell
        export SNOWFLAKE_ACCOUNT=$(op read "op://Vault/Snowflake/account")
        export SNOWFLAKE_USER=$(op read "op://Vault/Snowflake/username")
        export SNOWFLAKE_PASSWORD=$(op read "op://Vault/Snowflake/password")

        export SNOWFLAKE_ROLE=$(op read "op://Vault/Snowflake/role")
        export SNOWFLAKE_WAREHOUSE=$(op read "op://Vault/Snowflake/warehouse")
        export SNOWFLAKE_DATABASE=$(op read "op://Vault/Snowflake/database")
        export SNOWFLAKE_SCHEMA=$(op read "op://Vault/Snowflake/schema")
        ```
