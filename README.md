# EduTools Temporary Instance

Spin up a temporary instance of EduTools if your school blocks it.

## Quick Start

### Automatic (in Codespaces/Devcontainer)
1. Open this repository in GitHub Codespaces or a devcontainer
2. The build will be automatically downloaded during container creation
3. Run `./start-server.sh` to start the EduTools server
4. Access the application on the forwarded port (usually 3000)

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

### Artifact Download Issues
If the script fails to download artifacts, it might be due to:

1. **GitHub API rate limits or authentication requirements**
   - Use GitHub CLI: `gh auth login`
   - Or wait a bit and try again
   - Or download manually from the [Actions page](https://github.com/EducationalTools/src/actions/workflows/build.yml)

2. **Network restrictions**
   - Some environments block GitHub API access
   - The script will create a mock instance for demonstration in this case

### In Development Environments
- The script automatically detects if running in Codespaces or devcontainers
- Use `./start-server.sh` for easy server startup
- Check that port 3000 is forwarded properly

### Manual Download
If automatic download fails, you can manually:
1. Go to [EducationalTools/src Actions](https://github.com/EducationalTools/src/actions/workflows/build.yml)
2. Click on the latest successful run
3. Download the "Build" artifact
4. Extract it to `./edutools-build/`
5. Run `./deploy-edutools.sh start`
