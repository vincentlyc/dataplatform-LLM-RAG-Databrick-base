from src.cost_utils import estimate_gpt54_global_short_dbu

input_tokens = 1773
output_tokens = 541

cost = estimate_gpt54_global_short_dbu(input_tokens, output_tokens)
print(cost)
