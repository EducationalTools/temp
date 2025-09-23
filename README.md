# EduTools Temporary Instance

Spin up a temporary instance of EduTools if your school blocks it.

## Quick Start

### Automatic (in Codespaces/Devcontainer)
1. Open this repository in GitHub Codespaces or a devcontainer
2. The script will automatically download and start EduTools
3. Access the application on the forwarded port (usually 3000)

### Manual Usage

```bash
# Download and start (auto-starts in dev environments)
./deploy-edutools.sh

# Just download the latest build
./deploy-edutools.sh download

# Start the server from existing build
./deploy-edutools.sh start

# Clean up downloaded files
./deploy-edutools.sh clean

# Show help
./deploy-edutools.sh help
```

## What it does

The `deploy-edutools.sh` script:
1. Fetches the latest successful Build workflow from [EducationalTools/src](https://github.com/EducationalTools/src)
2. Downloads the Build artifact (contains the compiled application)
3. Extracts the files
4. Starts the EduTools server

## Requirements

- `curl` - for downloading artifacts
- `unzip` - for extracting archives  
- `node` - for running the application
- Internet connection to GitHub

## Environment Variables

- `PORT` - Server port (default: 3000)

## Troubleshooting

If the script fails to download artifacts, it might be due to GitHub API rate limits or authentication requirements. In that case, you can:

1. Use GitHub CLI: `gh auth login`
2. Or wait a bit and try again
3. Or download manually from the [Actions page](https://github.com/EducationalTools/src/actions/workflows/build.yml)
