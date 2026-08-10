def score(results):
    points_per_check = 10 / len(results)
    return round(sum(points_per_check for _, passed, _ in results if passed), 1)


def render(results):
    lines = ["Open Source Readiness Check", "-" * 30]
    for name, passed, fix in results:
        mark = "PASS" if passed else "FAIL"
        lines.append(f"[{mark}] {name}")
        if not passed:
            lines.append(f"     -> {fix}")
    lines.append("-" * 30)
    lines.append(f"Score: {score(results)}/10")
    return "\n".join(lines)
