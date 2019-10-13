#!/bin/bash
ORG=""
docker pull zricethezav/gitleaks:latest

for URL in $URLS
do
echo "Beginning $URL"
docker run --name=gitleaks \
        -e GITHUB_TOKEN=${GITHUB_TOKEN} \
        zricethezav/gitleaks \
            --verbose \
            --repo=$URL \
            --disk \
            --report=results.csv \
            --github-org=${ORG} \
            --depth=1
CONTAINER_ID=$(docker ps -aq --filter="name="gitleaks"")
docker cp ${CONTAINER_ID}:/results.csv results_append.csv
docker rm gitleaks
cat results_append.json >> results.csv
rm -i -f results_append.json
    echo "done $URL"
done
echo "EVERYTHING IS COMPLETE!"

# scp -i key.pem  user@ip:gitleaks/results.json /Users/path/to/store/file.json/csv/