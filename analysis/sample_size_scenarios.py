"""Simple planning scenarios for the DSP-Lab main study.

This script is for transparent planning, not for post-hoc justification of the
observed sample size. It reports conventional two-group sample-size estimates
for standardized mean differences and an ANCOVA planning sensitivity that
assumes the pre-test explains a chosen fraction of post-test variance.

Usage:
    python analysis/sample_size_scenarios.py
    python analysis/sample_size_scenarios.py --alpha 0.05 --power 0.80 --r2 0.25 --attrition 0.15
"""

from __future__ import annotations

import argparse
import math

from statsmodels.stats.power import TTestIndPower


def ceil_even_total(per_group: float) -> int:
    return 2 * math.ceil(per_group)


def recruit_total(analyzable_total: int, attrition: float) -> int:
    if not 0 <= attrition < 1:
        raise ValueError("attrition must be in [0, 1)")
    return math.ceil(analyzable_total / (1 - attrition))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--power", type=float, default=0.80)
    parser.add_argument(
        "--r2",
        type=float,
        default=0.25,
        help="Planning assumption for variance in post-test explained by pre-test.",
    )
    parser.add_argument("--attrition", type=float, default=0.15)
    args = parser.parse_args()

    if not 0 <= args.r2 < 1:
        raise ValueError("r2 must be in [0, 1)")

    analysis = TTestIndPower()
    effects = [0.40, 0.50, 0.60]

    print("DSP-Lab main-study sample-size planning scenarios")
    print(f"alpha={args.alpha:.2f}, power={args.power:.2f}, assumed pre/post R^2={args.r2:.2f}, attrition={args.attrition:.0%}")
    print()
    print("Effect  Unadjusted total  Recruit total  ANCOVA-planning total  Recruit total")
    print("------  ----------------  -------------  ---------------------  -------------")

    for d in effects:
        n_per_group = analysis.solve_power(
            effect_size=d,
            alpha=args.alpha,
            power=args.power,
            ratio=1.0,
            alternative="two-sided",
        )
        total = ceil_even_total(n_per_group)
        total_recruit = recruit_total(total, args.attrition)

        # Planning sensitivity only: if baseline explains R^2 of outcome variance,
        # residual SD is multiplied by sqrt(1-R^2), so the standardized treatment
        # effect relative to residual SD is d/sqrt(1-R^2).
        d_adjusted = d / math.sqrt(1 - args.r2)
        n_per_group_adj = analysis.solve_power(
            effect_size=d_adjusted,
            alpha=args.alpha,
            power=args.power,
            ratio=1.0,
            alternative="two-sided",
        )
        total_adj = ceil_even_total(n_per_group_adj)
        total_adj_recruit = recruit_total(total_adj, args.attrition)

        print(
            f"{d:>4.2f}   {total:>16d}  {total_recruit:>13d}  "
            f"{total_adj:>21d}  {total_adj_recruit:>13d}"
        )

    print()
    print("Notes:")
    print("- The unadjusted column is the conventional two-independent-groups benchmark.")
    print("- The ANCOVA column is only a planning sensitivity; its gain depends on the actual pre/post relationship.")
    print("- Do not choose the assumed R^2 after inspecting main-study outcomes.")
    print("- If assignment is by intact class, clustering can require a larger sample than these student-level calculations.")


if __name__ == "__main__":
    main()
