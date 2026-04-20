# GitHub Pages Setup Instructions for beam-code-practice

## Issue
The wiki is not working because GitHub Pages needs to be enabled and configured for the repository.

## Solution: Enable GitHub Pages

### Step 1: Enable GitHub Pages
1. Go to your repository on GitHub: https://github.com/nellaivijay/beam-code-practice
2. Click on "Settings" tab
3. Click on "Pages" in the left sidebar
4. Under "Source", select "Deploy from a branch"
5. Select "main" branch and "/docs" folder
6. Click "Save"

### Step 2: Verify GitHub Actions Workflow
1. Go to the "Actions" tab in your repository
2. Check if the "Deploy to GitHub Pages" workflow has run
3. If it hasn't run automatically, click on "Deploy to GitHub Pages" and click "Run workflow"
4. Wait for the workflow to complete

### Step 3: Access the Wiki
Once GitHub Pages is deployed, the wiki will be accessible at:
- Main site: https://nellaivijay.github.io/beam-code-practice/
- Wiki Home: https://nellaivijay.github.io/beam-code-practice/wiki/Home.html

## Alternative: Add Wiki Link to README
If GitHub Pages is not an option, you can add a direct link to the wiki content in the main README:

Add this section to your README.md:
```markdown
## 📖 Wiki
Comprehensive documentation is available in the [Wiki](docs/wiki/Home.html)

- [Wiki Home](docs/wiki/Home.html)
- [Lab 0: Sample Data Setup](docs/wiki/Lab-0-Sample-Data-Setup.html)
- [Lab 1: Environment Setup](docs/wiki/Lab-1-Environment-Setup.html)
```

## Current Wiki Structure
The wiki content is now properly organized:
```
docs/
├── index.html              # Main documentation page
└── wiki/
    ├── Home.html           # Wiki home page
    ├── Lab-0-Sample-Data-Setup.html
    └── Lab-1-Environment-Setup.html
```

## Troubleshooting
If GitHub Pages still doesn't work:
1. Check that the repository is public (GitHub Pages works best with public repos)
2. Verify the GitHub Actions workflow is enabled
3. Check the Actions tab for any workflow errors
4. Ensure the docs folder contains the index.html file