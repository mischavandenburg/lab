# Tutorial: Autoscaling with KEDA on AKS

This tutorial will guide you through setting up a simple auotscaled application based on PostgreSQL queries.

# Creating / Updating the Cluster

Use this command to create an AKS cluster with KEDA enabled:

`az aks create --resource-group myResourceGroup --name myAKSCluster --enable-keda`

Or you can enable it on an existing cluster:

`az aks update --resource-group myResourceGroup --name myAKSCluster --enable-keda`

# Setting up the Database

Install the EDB Operator to allow the creation of databases

`kubectl apply -f https://get.enterprisedb.io/cnp/postgresql-operator-1.22.0.yaml`

After creating the database, let's populate it with some data.

Start by connecting to the pod and running some commands in psql:

```

```

```sql
CREATE SCHEMA IF NOT EXISTS queue;
CREATE TABLE IF NOT EXISTS queue.messages (id SERIAL PRIMARY KEY, status VARCHAR(50));
GRANT USAGE ON SCHEMA queue TO app;
GRANT SELECT ON queue.messages TO app;
```


Now that the tables are created, we can add some data:

```sql
DO
$$
BEGIN
    FOR counter IN 1..100 LOOP
        INSERT INTO queue.messages (status) VALUES ('new');
    END LOOP;
END
$$;
```

To verify the amount of messages in the queue:

`SELECT count(*) FROM queue.messages WHERE status = 'new';`

This is the number that we'll base the scaling trigger on.


To delete all messages:
`DELETE FROM queue.messages;`

To be able to list the tables with dt, run:
SET search_path TO queue, public;

Alternatively, use:
\dt queue.*




```
