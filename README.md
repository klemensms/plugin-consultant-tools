# Consultant Tools Plugin

Shared plugin collection for Dynamics CRM consultants. Provides skills and MCP servers for use across all client projects.

## Installation

### 1. Add the marketplace

```
/plugin marketplace add klemensms/plugin-consultant-tools
```

### 2. Install the plugin

```
/plugin install consultant-tools@consultant-tools
```

## Updating

To get the latest version:

```
/plugin marketplace update consultant-tools
```

Then restart Claude Code or start a new session.

## What's Included

### Skills

| Skill                                | Description                                                                    |
|--------------------------------------|--------------------------------------------------------------------------------|
| `consultant-tools:markdown-docs`     | Enforces consistent structure and formatting for wiki/technical docs           |
| `consultant-tools:ado-user-stories`  | Create/update Azure DevOps user stories with proper HTML and AC formatting     |
| `consultant-tools:ado-wiki`          | Create/update ADO Wiki pages with consistent structure and API versioning      |
| `consultant-tools:crm-best-practices`| Standards for Dynamics 365/CRM table naming, columns, and customization        |
| `consultant-tools:secret-guard`      | Mandatory secret scanning before git commits to prevent credential exposure    |

### MCP Servers

| Server               | Description                        |
|----------------------|------------------------------------|
| `example-filesystem` | Filesystem access (placeholder)    |

### Hooks

The plugin includes auto-approval hooks for common CRM consulting workflows:

| Hook                       | What it does                                                          |
|----------------------------|-----------------------------------------------------------------------|
| `auto-approve-mcp.py`      | Auto-approves Azure DevOps, Power Platform, and Figma MCP tools       |
| `auto-approve-readonly.py` | Auto-approves safe read-only Bash commands (ls, cat, grep, etc.)      |

**MCP patterns auto-approved:**
- `mcp__.*azure-devops.*` - Azure DevOps work items, wikis, pipelines
- `mcp__powerplatform-readonly-.*` - Power Platform read-only operations
- `mcp__figma.*` - Figma design tools

**Optional (macOS only):**
Audio notification scripts are included but not active by default. See `scripts/` folder for `play-audio.py` and `audio-then-prompt.sh`. To enable, add them to your project's hooks configuration.

## Adding New Skills

1. Create a folder under `plugins/consultant-tools/skills/`
2. Add a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: your-skill-name
description: Use when [trigger condition] - brief description of what it does
---

# Your Skill Name

Instructions for Claude to follow...
```

3. Bump version in both:
   - `plugins/consultant-tools/.claude-plugin/plugin.json`
   - `.claude-plugin/marketplace.json`

4. Commit and push

## Version History

| Version | Date       | Changes                                                              |
|---------|------------|----------------------------------------------------------------------|
| 1.3.0   | 2025-12-26 | Added auto-approval hooks for MCP tools and read-only Bash commands  |
| 1.2.0   | 2025-12-26 | Added ado-user-stories, ado-wiki, crm-best-practices, secret-guard   |
| 1.1.0   | 2025-12-26 | Added markdown-docs skill                                            |
| 1.0.0   | 2025-12-26 | Initial release with plugin structure                                |
