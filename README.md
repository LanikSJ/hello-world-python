# Hello World Python Application

A simple Python application that displays a "Hello, World!" message.

## Description

This is a basic Python application that demonstrates the classic "Hello, World!" program. It's perfect for beginners learning Python or for testing Python installations.

## Features

- Simple "Hello, World!" output
- Clean, well-documented code
- Python 3 compatible
- Executable script

## Requirements

- Python 3.x

## Usage

### Running the Application

1. Make the script executable (optional):

   ```bash
   chmod +x hello_world_app.py
   ```

2. Run the application:

   ```bash
   python3 hello_world_app.py
   ```

   Or if you made it executable:

   ```bash
   ./hello_world_app.py
   ```

### Expected Output

When you run the application, you should see:

```bash
Hello, World!
Welcome to Python programming!
```

## File Structure

- `hello_world_app.py` - Main application file
- `README.md` - This documentation file

## Skills Update Automation

This project uses the `skills` CLI (npm package) to manage Agent Skills. The skills are tracked in `skills-lock.json`.

### Automated Updates

A GitHub Actions workflow automatically checks for skill updates weekly:

- **Schedule**: Every Sunday at 00:00 UTC
- **Action**: Runs `npm skills update` to check for updates
- **Cleanup**: Removes any local `.agents/` folder (uses global `.agents` config)
- **Output**: Creates a pull request with any changes

### Manual Usage

```bash
# Check for skill updates
npm skills update

# Install/upgrade specific skills
npm skills update <skill-name>
```

### Workflow File

The automation is configured in `.github/workflows/skills-update.yml`.

## License

This project is in the public domain.
