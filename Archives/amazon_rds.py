import boto3
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

def create_snapshot_rds(cluster_name="micrologx-restaurant-infra-production-rdsdbcluster-dzeoaag5shsa", snapshot_prefix="prod-"):
    client = boto3.client('rds')
    return client.create_db_cluster_snapshot(
        DBClusterIdentifier=cluster_name,
        DBClusterSnapshotIdentifier=(snapshot_prefix + timestamp)
    )

if __name__ == "__main__":
    create_snapshot_rds()