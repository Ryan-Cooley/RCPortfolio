#!/bin/bash

echo "🔄 Updating portfolio site..."

# Update submodules
echo "📦 Updating submodules..."
git submodule update --remote

# Add all changes
echo "➕ Adding changes..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "✅ No changes to commit"
else
    # Commit changes
    echo "💾 Committing changes..."
    git commit -m "Auto-update: $(date)"
    
    # Push to GitHub
    echo "🚀 Pushing to GitHub..."
    git push origin main
    
    echo "✅ Site updated successfully!"
    echo "⏳ Wait 2-3 minutes for GitHub Pages to rebuild"
else
    echo "✅ No changes to commit"
fi

echo "🎉 Done!" 