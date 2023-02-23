#! /bin/bash

aws rds create-db-cluster-snapshot --db-cluster-identifier micrologx-restaurant-infra-production-rdsdbcluster-dzeoaag5shsa --db-cluster-snapshot-identifier prod-$(date +'%Y%m%d-%H%M%S') --tags Key=test,Value=true
