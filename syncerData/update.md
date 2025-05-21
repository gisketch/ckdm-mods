# 📝 Changes

## ✨ **New Feature: Advanced In-Game Scoreboard System** ✨

I've rolled out a new, custom-developed scoreboard system that integrates directly into Chowkingdom.

**System Architecture:**

The goal was to create a robust and efficient scoreboard that felt native to our server.

- **Custom-Built Scoreboard Engine:** The core of this system is a Node.js application I wrote from scratch. It's not just a simple script; it's an engine designed to:
  - Continuously monitor and parse player data from the server's `leaderboard.json`.
  - Maintain its own detailed log (`scoreboard_log.json`) for precise tracking of current scores and determining eligibility for top-player medal displays.
  - Implement custom logic for ranking players across numerous categories and intelligently processing score changes. This part took a good chunk of time to conceptualize and implement effectively.
- **Pterodactyl API Integration:** To bring these stats into the game, the system communicates with the Minecraft server using the Pterodactyl panel API. This allows for:
  - Dynamic creation and real-time updates of scoreboard objectives.
  - Accurate setting of individual player scores on the sidebar.
  - Management of player display names, including the automatic awarding of a `:medal:` icon to the top 3 players in the currently active category.
- **Efficiency-Focused Design:** A key consideration was server performance. The system is built to be efficient, only sending update commands to the Minecraft server when scores or the medal status of top players actually change. This prevents unnecessary server load and keeps things running smoothly.

**In-Game Features & Usage:**

- **Dynamic Sidebar Display:** You'll see a rotating selection of different score categories displayed on the right-hand sidebar in Minecraft.
- **Real-Time Updates:** Your scores and rankings will update automatically as you play and achieve new milestones.
- **Top Player Recognition:** Medal icons will indicate the top 3 players for the scoreboard category currently being displayed.
- **Discord Bot Interaction:** You can also access scoreboard information via our Discord bot:
  - Use `!sb <category_name>` to view the current leaderboard for a specific category (e.g., `!sb global`, `!sb captures`).
  - Type `!sb help` to get a full list of all available scoreboard categories.
  - The bot uses smart matching, so partial names like `!sb starters` will correctly find `startersCaught`.

### 🟢 Added

- Scoreboard Overhaul - used for UI

### ❌ Removed

- None
