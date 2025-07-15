#!/bin/bash

echo "🚀 Deploying Portfolio to GitHub Pages"
echo "======================================"

# Check if we have changes to commit
if git diff --quiet && git diff --cached --quiet; then
    echo "✅ No changes to commit"
else
    echo "📝 Committing changes..."
    git add .
    git commit -m "Auto-deploy: $(date)"
fi

# Update submodules
echo "📦 Updating submodules..."
git submodule update --remote

# Check if submodules were updated
if git diff --quiet; then
    echo "✅ No submodule updates"
else
    echo "📝 Committing submodule updates..."
    git add .
    git commit -m "Update submodules: $(date)"
fi

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Deployment initiated!"
echo "⏳ GitHub Actions will build and deploy automatically"
echo "🌐 Check your site in 2-3 minutes" 