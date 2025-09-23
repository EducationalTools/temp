#!/bin/bash
# download_latest_build_artifact.sh
# This script downloads the latest 'Build' workflow artifact from the main branch of EducationalTools/src

set -euo pipefail

REPO="EducationalTools/src"
BRANCH="main"
WORKFLOW_NAME="Build"

if [ -d "edutools" ]; then
  echo "Already exists"
else

  echo "Getting latest build..."

  # Get the latest workflow run ID for the 'Build' workflow on the main branch
  RUN_ID=$(gh run list --repo "$REPO" --branch "$BRANCH" --workflow "$WORKFLOW_NAME" --limit 1 --json databaseId -q '.[0].databaseId')

  if [ -z "$RUN_ID" ]; then
    echo "No workflow run found for $WORKFLOW_NAME on $BRANCH in $REPO"
    exit 1
  fi

  echo "Downloading artifacts for run $RUN_ID... This may take a while."
  gh run download "$RUN_ID" --repo "$REPO" --name "$WORKFLOW_NAME" --dir "./edutools"

  echo "Files downloaded to ./edutools"

fi

echo "Installing stuff"
npm i -g http-server > /dev/null

echo "Starting server"
cd edutools
# echo "You should soon get a notification down the bottom left. Press open in browser."
echo "Click here and press the enter button"
read
python -m webbrowser -t "http://127.0.0.1:8080"
npx http-server &

