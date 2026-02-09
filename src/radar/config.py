import os
import yaml
from typing import Dict, Any

class Config:
    def __init__(self):
        self.env = self.load_env()
        self.rules = self.load_yaml("rules/rules.yaml")
        self.sources = self.load_sources("rules/sources.yaml")

    def load_env(self):
        from dotenv import load_dotenv
        load_dotenv()
        return {
            "SLACK_TOKEN": os.getenv("SLACK_TOKEN"),
            "KSTARTUP_API_KEY": os.getenv("KSTARTUP_API_KEY"),
        }

    def load_yaml(self, path: str) -> Any:
        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def load_sources(self, path: str) -> Dict[str, Any]:
        sources = self.load_yaml(path)
        return {src["id"]: src for src in sources if src.get("enabled", False)}

config = Config()