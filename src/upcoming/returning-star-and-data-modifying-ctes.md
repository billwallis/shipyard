- [BW 10 mins] `returning *` and data-modifying CTEs
    - `returning *` is available in lotsa DBs, good for many DML actions
        - Real nice for checking results before committing them
            ```sql
            /*    SQLite    */
            create table words (id int, value text);
            insert into words
            values
                (1, 'foo'),
                (2, 'bar'),
                (3, 'baz')
            returning *
            ;

            begin transaction;
                update words
                set value = upper(value)
                where value != 'foo'
                returning *
                ;
            commit;
            rollback;
            ```
        - https://www.linkedin.com/posts/bill-wallis_sqlwithbill-sql-activity-7326532233790386176-_ga0
    - Data-modifying CTEs (PostgreSQL only feature AFAIK)
        - Generally avoid, but has some nice use cases — e.g. "archiving" data
            ```sql
            /*    PostgreSQL    */
            with events_to_move as (
                delete from events
                where event_ts <= (current_date - interval '30 days')::timestamp)
                returning *
            )

            insert into events_history
                select *
                from events_to_move
            ;
            ```
        - https://www.linkedin.com/posts/bill-wallis_sqlwithbill-sql-activity-7326893794631573504-gpeM
