import logging
from radar.config import config
from radar.connectors.knowhow_feed import _parse_rss_with_feedparser
from radar.integrations.slack import send_to_slack

def run_daily(publish: bool = True):
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting daily execution...")

    # Load configuration
    sources = config.sources
    rules = config.rules

    # Collect data from enabled sources
    raw_items = []
    for source_id, source_cfg in sources.items():
        if source_cfg["connector"] == "knowhow_feed":
            raw_items.extend(_parse_rss_with_feedparser(source_cfg["api"]))

    # Apply rules to filter/tag items
    filtered_items = []
    for item in raw_items:
        for rule in rules:
            if any(keyword in item["title"] for keyword in rule["keywords"]):
                item["tags"] = rule["tags"]
                filtered_items.append(item)
                break

    # Send results to Slack
    if publish:
        for item in filtered_items:
            message = f"Title: {item['title']}\nURL: {item['url']}\nTags: {', '.join(item['tags'])}"
            send_to_slack(message)

if __name__ == "__main__":
    run_daily()