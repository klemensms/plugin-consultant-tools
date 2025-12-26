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

| Skill                            | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| `consultant-tools:markdown-docs` | Enforces consistent structure and formatting for wiki/technical docs    |

### MCP Servers

| Server               | Description                        |
|----------------------|------------------------------------|
| `example-filesystem` | Filesystem access (placeholder)    |

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

| Version | Date       | Changes                                      |
|---------|------------|----------------------------------------------|
| 1.1.0   | 2025-12-26 | Added markdown-docs skill                    |
| 1.0.0   | 2025-12-26 | Initial release with plugin structure        |
