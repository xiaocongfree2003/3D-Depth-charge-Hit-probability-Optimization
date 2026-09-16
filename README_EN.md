# 3D Depth-charge Hit-probability Optimization

This repository presents a **2024 National Second Prize mathematical modeling paper**. It preserves the original Chinese paper and reorganizes its research questions, methods, solution process, and results for easier reading on GitHub.

[Original Paper (PDF)](paper/README.md) · [Chinese README](README.md) · [Extended Chinese Guide](docs/论文导读.md)

## Overview

The study investigates probability optimization under uncertain three-dimensional positioning. It develops models for three increasingly complex scenarios: a single release without depth error, a single release with three-dimensional positioning error, and a multi-point array strategy.

The main methods are:

- three-dimensional geometric probability modeling;
- normal and one-sided truncated normal distributions;
- Monte Carlo simulation;
- particle swarm optimization;
- repeated experiments and sensitivity analysis.

## Problem Structure

| Part | Objective | Main Method |
| --- | --- | --- |
| Problem 1 | Relate planar coordinates and depth settings to a single-event hit probability | Probability integration and Monte Carlo simulation |
| Problem 2 | Optimize parameters under errors in all three spatial directions | Truncated-normal modeling and parameter search |
| Problem 3 | Optimize a multi-point array, sequence, and shared parameters | Joint probability modeling and particle swarm optimization |

## Reported Results

Under the assumptions and parameters of the competition problem, the paper reports:

- a maximum combined probability of `0.082` for Problem 1;
- an optimal depth parameter of `118 m` and a maximum probability of `0.0223` for Problem 2;
- the best overall performance from the edge-priority strategy, with a total probability of `0.7634`, for Problem 3.

Please follow the [paper restoration guide](paper/README.md) to obtain the original PDF with a verified SHA-256 checksum.

> This is an academic mathematical-modeling project based on competition assumptions. It is provided for educational and research discussion only and should not be interpreted as an operational engineering or military conclusion.
