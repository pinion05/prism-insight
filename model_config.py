"""
Central model configuration for all agents.

Edit the values in this file to change the LLMs used across the project from a single place.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ModelConfig:
    # OpenAI models
    trading_scenario: str = "gpt-5"
    sell_decision: str = "gpt-5"
    report_generation: str = "gpt-4.1"
    investment_strategy: str = "gpt-4.1"
    summary: str = "gpt-4.1"
    telegram_summary: str = "gpt-4.1"
    translation: str = "gpt-5-nano"

    # Other providers
    transcription: str = "whisper-1"
    anthropic_report: str = "claude-sonnet-4-5-20250929"


MODEL_CONFIG = ModelConfig()

__all__ = ["MODEL_CONFIG", "ModelConfig"]
