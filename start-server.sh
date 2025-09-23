#!/bin/bash

# Simple server startup script for devcontainers/codespaces
echo "🚀 Starting EduTools server..."

# If build doesn't exist, download it first
if [ ! -d "./edutools-build" ]; then
    echo "📥 Build not found, downloading first..."
    ./deploy-edutools.sh download
fi

# Start the server
./deploy-edutools.sh start