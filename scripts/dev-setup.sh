#!/bin/bash

echo "🚀 Portfolio Development Setup"
echo "=============================="

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Update submodules
echo "📦 Updating submodules..."
git submodule update --init --recursive

# Install global tools if not present
if ! command_exists live-server; then
    echo "📥 Installing live-server..."
    npm install -g live-server
fi

if ! command_exists prettier; then
    echo "📥 Installing prettier..."
    npm install -g prettier
fi

# Setup pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
if [ ! -f .git/hooks/pre-commit ]; then
    cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
echo "🔍 Running pre-commit checks..."
# Format HTML/CSS/JS files
find . -name "*.html" -o -name "*.css" -o -name "*.js" | xargs prettier --write
echo "✅ Pre-commit checks completed"
EOF
    chmod +x .git/hooks/pre-commit
fi

echo "✅ Development environment ready!"
echo ""
echo "📋 Available commands:"
echo "  ./scripts/dev-server.sh    - Start development server"
echo "  ./scripts/deploy.sh        - Deploy to GitHub Pages"
echo "  ./scripts/new-project.sh   - Add new project as submodule"
echo "  ./scripts/update-all.sh    - Update all submodules and deploy" 