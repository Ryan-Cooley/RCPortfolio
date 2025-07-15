#!/bin/bash

echo "🆕 Add New Project to Portfolio"
echo "==============================="

# Get project details
read -p "Enter project name (e.g., my-awesome-project): " PROJECT_NAME
read -p "Enter GitHub repository URL: " REPO_URL
read -p "Enter project category (e.g., Python, Web, ML): " CATEGORY

# Convert project name to folder name
FOLDER_NAME=$(echo $PROJECT_NAME | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

echo ""
echo "📋 Project Details:"
echo "  Name: $PROJECT_NAME"
echo "  Folder: $FOLDER_NAME"
echo "  Category: $CATEGORY"
echo "  URL: $REPO_URL"
echo ""

read -p "Continue? (y/n): " CONFIRM

if [ "$CONFIRM" != "y" ]; then
    echo "❌ Cancelled"
    exit 1
fi

# Add as submodule
echo "📦 Adding as submodule..."
git submodule add $REPO_URL $FOLDER_NAME

# Commit the addition
echo "📝 Committing submodule addition..."
git add .gitmodules $FOLDER_NAME
git commit -m "Add $PROJECT_NAME as submodule"

echo "✅ Project added successfully!"
echo ""
echo "📝 Next steps:"
echo "  1. Update index.html to include the new project"
echo "  2. Add project images to img/ folder"
echo "  3. Run ./scripts/deploy.sh to deploy" 