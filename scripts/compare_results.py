"""Compare experimental results with baseline"""
import json
from pathlib import Path

RESULTS_DIR = Path(__file__).parent.parent / "experiments" / "results"

def load_results(exp_id: str):
    result_file = RESULTS_DIR / f"{exp_id}_results.json"
    with open(result_file) as f:
        return json.load(f)

def compare_experiments(baseline_id: str, exp_ids: list):
    baseline = load_results(baseline_id)
    baseline_metrics = baseline["metrics"]
    
    print(f"\n{'Experiment':<30} {'Latency (ms)':<15} {'Improvement':<15}")
    print("-" * 60)
    
    for exp_id in exp_ids:
        exp = load_results(exp_id)
        exp_metrics = exp["metrics"]
        
        latency_improvement = (
            (baseline_metrics["latency_ms"] - exp_metrics["latency_ms"]) 
            / baseline_metrics["latency_ms"] * 100
        )
        
        print(f"{exp_id:<30} {exp_metrics['latency_ms']:<15.2f} {latency_improvement:<15.1f}%")

if __name__ == "__main__":
    compare_experiments("baseline", ["exp_001_attention_v1"])
