# Steam Daily Deal Bot

An automated bot that scans Steam deals with discounts of 90% or more and posts them to Discord every day. The project uses Python, the CheapShark API, and GitHub Actions for scheduled runs.

## Features

- Scans Steam deals on a daily GitHub Actions schedule.
- Filters games with `savings >= 90`.
- Sorts deals by discount percentage in descending order.
- Splits Discord messages into multiple parts, up to 10 deals per message.
- Supports local execution with `.env` and GitHub deployment with Secrets.

## Project Structure

```text
.
|-- .github/
|   `-- workflows/
|       `-- daily_check.yml
|-- src/
|   |-- main.py
|   |-- notifier.py
|   `-- steam_api.py
|-- .gitignore
|-- .editorconfig
|-- requirements.txt
|-- README.md
`-- README.vi.md
```

## Requirements

- Python 3.11
- A Discord webhook URL

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the repository root:

```env
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_here
```

Run the bot locally:

```bash
python src/main.py
```

## GitHub Actions Setup

Create a repository secret named `DISCORD_WEBHOOK_URL`:

1. Go to `Settings` -> `Secrets and variables` -> `Actions`.
2. Click `New repository secret`.
3. Set the name to `DISCORD_WEBHOOK_URL`.
4. Paste your Discord webhook URL as the value.

The workflow is defined in [.github/workflows/daily_check.yml](.github/workflows/daily_check.yml) and currently runs on this cron schedule:

```yaml
0 1 * * *
```

That corresponds to 08:00 AM Vietnam time when the offset is UTC+7.

## Discord Output

On each run, the bot will:

- Call CheapShark to fetch Steam deals.
- Filter deals with discounts of 90% or higher.
- Sort them by `% savings` descending.
- Send them to Discord in chunks of up to 10 embeds.

Each embed contains:

- Game title
- Steam Store link
- Original price
- Sale price
- Discount percentage
- Game header image

## No-Deal Behavior

If no deals meet the 90% threshold, the bot only writes a log message and does not send anything to Discord.

## Environment Variables

- `DISCORD_WEBHOOK_URL`: primary webhook URL.
- `DISCORD_WEBHOOK`: fallback variable still accepted by `src/notifier.py`.

## Dependencies

- `requests`
- `python-dotenv`
- `pytz`

## Encoding Note

The repository should be saved in UTF-8. If your terminal displays broken characters, verify:

- your editor is saving files as `UTF-8`
- your PowerShell or terminal session is reading the correct encoding

The repository includes [.editorconfig](.editorconfig) to reduce encoding-related issues in future edits.

## Language Versions

- English: [README.md](README.md)
- Vietnamese: [README.vi.md](README.vi.md)
