def estimate_gpt54_global_short_dbu(input_tokens: int, output_tokens: int) -> dict:
    input_rate_dbu_per_1m = 35.714
    output_rate_dbu_per_1m = 214.286

    input_dbu = input_tokens / 1_000_000 * input_rate_dbu_per_1m
    output_dbu = output_tokens / 1_000_000 * output_rate_dbu_per_1m
    total_dbu = input_dbu + output_dbu

    return {
        "estimated_input_dbu": input_dbu,
        "estimated_output_dbu": output_dbu,
        "estimated_total_dbu": total_dbu,
    }
