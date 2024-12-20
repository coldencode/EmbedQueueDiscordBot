# EmbedQueueDiscordBot

EmbedQueueDiscordBot is a lightweight Discord bot that manages a queue system using rich embed messages. Users can join the queue by providing their Discord Tag and are prompted to input their username. This bot is ideal for managing queues in games, events, or community activities.

## Features
- **Simple Queue System**: Adds users to a queue using their Discord Tag.
- **Embed Messages**: Displays the queue in a visually appealing embed format.
- **Username Prompt**: Prompts users to provide their username when joining the queue.
- **Dynamic Queue Management**: Supports adding, removing, and viewing queue participants in real-time.

![Example](https://i.imgur.com/g9DXiAe.png)
## Getting Started

### Prerequisites
- A Discord account.
- A server where you have permission to add bots.
- [Discord Developer Portal](https://discord.com/developers/applications) access to create a bot.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/coldencode/EmbedQueueDiscordBot.git
   cd EmbedQueueDiscordBot
   ```

2. **Install Dependencies**:
   ```bash
   py -3 -m pip install -U discord.py
   ```

3. **Set Up Bot Token**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and generate a bot token.
   - Create a `.env` file in the project root and add the following:
     ```env
     DISCORD_TOKEN=your-bot-token
     ```

4. **Run the Bot**:
   ```bash
   node index.js
   ```

### Adding the Bot to Your Server
- Use the OAuth2 URL generator in the Discord Developer Portal to invite the bot to your server. Ensure the bot has the `Manage Messages` and `Embed Links` permissions.

### Admin Commands
- **`!clearqueue`**: Clears all users from the queue.


## Support
If you encounter any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/coldencode/EmbedQueueDiscordBot).

---
Thank you for using EmbedQueueDiscordBot! Happy queuing!

