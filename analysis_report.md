# Random Number Generator Analysis (LCG)

## Algorithm Description
This project implements a Linear Congruential Generator (LCG), which is one of the
simplest and most widely used pseudo-random number generation algorithms.

## Formula
Xₙ₊₁ = (a × Xₙ + c) mod m

## Parameters
- a = 1664525
- c = 1013904223
- m = 2³²
- Seed = current system time

## Time Complexity
- O(1) per random number generation

## Space Complexity
- O(1), only one integer stored as state

## Advantages
- Fast and easy to implement
- Requires minimal memory
- Suitable for simulations and basic randomization tasks

## Disadvantages
- Not cryptographically secure
- Can show patterns if parameters are poorly chosen

## Use Cases
- Simulations
- Educational purposes
- Quantization table generation
