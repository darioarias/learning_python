import random
from math import floor

def simulate(upper: int = 10_000):
  heads = 0
  tails = 0

  HEAD = 1
  TAIL = 0
  for i in range(upper):
    coin = random.randint(0, 1)
    if coin == HEAD:
      heads += 1
    
    if coin == TAIL: 
      tails += 1
  
  return {"heads": heads, "tails": tails}

result = {"heads": 0, "tails": 0};

total_runs = 1;
check_ins = 1;
MAX = 10
while(result['heads'] != floor(MAX / 2)):
  result = simulate(MAX)

  total_runs += 1;
  if total_runs % 100 == 0:
    print(result)
    print(f'ran {check_ins * MAX:,} times and counting')
    check_ins += 1;

print(f'{result}, took {total_runs: ,} runs, {total_runs * MAX:,} instructions, to complete')
# print(f"Heads: {heads}, Tails: {tails}")
# print(simulate())