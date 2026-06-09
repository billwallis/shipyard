- [BW 5 mins] Rolled back transactions still increment sequences 🤯
    - https://youtu.be/cyZ2fWVdxwE

```sql
/*    DuckDB    */
create sequence foo__pk start with 1;
create table foo(id int default nextval('foo__pk'));
insert into foo default values returning *;  -- inserts 1

start transaction;
insert into foo default values returning *;  -- inserts 2, rolled back
rollback;

start transaction;
insert into foo default values returning *;  -- inserts 3
commit;

from foo;  -- only has 1 and 3!
```
