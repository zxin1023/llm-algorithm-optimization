# LLM Algorithm Optimization Project Guide

## 项目目标
优化LLM推理性能，通过实验驱动的方式逐步改进

## 核心文件（优先理解）
- src/algorithms/attention.py - 注意力机制优化
- src/algorithms/decoding.py - 解码策略优化
- experiments/configs/ - 实验配置管理

## 性能基准
- Baseline: latency=100ms, throughput=10 req/s
- Target: latency=50ms, throughput=20 req/s

## 实验规范
1. 每个实验创建新的yaml配置文件
2. 运行后自动生成json结果文件
3. 在runs.log中记录实验日志
4. 使用scripts/compare_results.py对比结果