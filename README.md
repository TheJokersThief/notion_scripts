# Notion Scripts
Various tools and scripts I use to interact with Notion.

- [Notion Scripts](#notion-scripts)
- [Config](#config)
- [Usage](#usage)
- [Help](#help)
- [Commands](#commands)
  - [`booklist`](#booklist)

# Config
The config is in [TOML](https://toml.io/en/) and is supplied with the `-c/--config` option. If the file doesn't exist at the given path, the CLI will auto-generate one with default values and stop execution (it won't continue with your command) - this is how the example config file is generated.

For information on particular config attributes, check out the [ConfigSchema comments](notion_scripts/config.py).

# Usage
The project uses [poetry](https://python-poetry.org/) for dependency management and running. To run the CLI, you can type:

```
python run notion_scripts --config <path_to_config_file> <command_name>
```

# Help
For help, you can pass the `--help` flag at any time. 

For example, for help for the `booklist` command, you should type:

```
python run notion_scripts --config config.toml.example booklist --help
```

# Commands

## `booklist`

Updates a database with information fetched from the goodreads API. It maps the notion database column names to results from the goodreads API based on book title, then updates the database with those values.

For example, the included mapping config is:

```
pages = "num_pages"
publication_year = "publication_year"
publication_month = "publication_month"
publication_day = "publication_day"
rating = "average_rating"
name = "title"
```

| Column Name  | Goodreads API Field  |
|---|---|
| Pages | "num_pages" |
| publication_year | "publication_year" |
| publication_month | "publication_month" |
| publication_day | "publication_day" |
| Rating | "average_rating" |
| name | "title" |

**Limitations:**

* Can only insert data from the first-level of the Goodreads API response
* Can't handle select/multi-select elements as I haven't discovered a way to upsert options
