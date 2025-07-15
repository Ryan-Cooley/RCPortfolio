#!/bin/bash

echo "🌐 Starting Development Server"
echo "=============================="

# Check if we're in a Codespace
if [ -n "$CODESPACES" ]; then
    echo "🚀 Detected GitHub Codespace - using live-server"
    live-server --port=3000 --host=0.0.0.0 --no-browser
else
    echo "💻 Local environment - using Python HTTP server"
    python -m http.server 8000
fi 