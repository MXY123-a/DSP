# Control Review 03 — Discrete Convolution

**Target time:** 20–30 minutes

## Learning objective

Explain discrete convolution as shifted overlap followed by multiplication and summation, and determine basic properties such as output length.

## Concept review

For two discrete sequences `x[n]` and `h[n]`, linear convolution is

`y[n] = Σ x[k] h[n-k]`.

For each output index `n`:

1. one sequence is shifted relative to the other;
2. overlapping samples are multiplied;
3. the products are summed.

If `x[n]` has length `L` and `h[n]` has length `M`, the linear-convolution output has length

`L + M - 1`.

## Worked example

Let

`x = [1, 2, 1]`

and

`h = [1, 1]`.

The convolution has length `3 + 2 - 1 = 4`.

The output samples are:

- `y[0] = 1×1 = 1`
- `y[1] = 2×1 + 1×1 = 3`
- `y[2] = 1×1 + 2×1 = 3`
- `y[3] = 1×1 = 1`

So

`y = [1, 3, 3, 1]`.

## Practice

1. Two sequences have lengths 5 and 4. What is the length of their linear convolution?
2. For `x = [2, 1]` and `h = [1, 3]`, calculate the full convolution.
3. In words, what does `h[n-k]` contribute to the convolution process?
4. Why does the output normally become longer than either individual input sequence?

## Compare and explain

Consider

`x = [1, 0, 1]`.

Compare convolution with:

- Filter A: `hA = [1]`
- Filter B: `hB = [0.5, 0.5]`

Without using software, calculate both outputs. Then explain why Filter B can be interpreted as a simple local averaging or smoothing operation.

## Short summary

In 2–3 sentences, explain what happens at one output sample of a discrete convolution and why the phrase **multiply and sum over the overlap** is useful.
