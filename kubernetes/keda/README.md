This is to set up a PoC with KEDA based on PostgreSQL queries.

Install EDB

kubectl apply -f \
  https://get.enterprisedb.io/cnp/postgresql-operator-1.22.0.yaml

After creating the cluster, populate the database

```sql

CREATE SCHEMA IF NOT EXISTS queue;

CREATE TABLE IF NOT EXISTS queue.messages (id SERIAL PRIMARY KEY, status VARCHAR(50));


Now that the tables are created, we can add some data:

DO
$$
BEGIN
    FOR counter IN 1..100 LOOP
        INSERT INTO queue.messages (status) VALUES ('new');
    END LOOP;
END
$$;

To verify the amount of messages in the queue:

SELECT count(*) FROM queue.messages WHERE status = 'new';


To be able to list the tables with dt, run:
SET search_path TO queue, public;

Alternatively, use:
\dt queue.*

To delete all messages:
DELETE FROM queue.messages;

```
