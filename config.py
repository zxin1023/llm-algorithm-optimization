"""Global configuration for LLM optimization experiments"""
from pathlib import Path
from dataclasses import dataclass

PROJECT_ROOT = Path(__file__).parent
EXPERIMENTS_DIR = PROJECT_ROOT / "experiments"
RESULTS_DIR = EXPERIMENTS_DIR / "results"
CONFIGS_DIR = EXPERIMENTS_DIR / "configs"

@dataclass
class PerformanceBaseline:
    latency_ms: float = 100.0
    throughput_req_s: float = 10.0
    memory_gb: float = 16.0

BASELINE = PerformanceBaseline()
