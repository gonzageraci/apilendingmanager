autofarm_blockchain = ["fantom", "bsc", "heco", "polygon", "avax"]
beefy_apy = "https://api.beefy.finance/apy/breakdown"
beefy_tvl = "https://api.beefy.finance/TVL"
grim_blockchain = ["bsc", "fantom", "avax", "polygon"]

def autofarm(bc):
  return "https://static.autofarm.network/"+bc+"/farm_data.json"

def swamp(bc):
  if bc == "bsc":
    return "https://swamp.finance/static/frontend/api-public/api-pools.json"
  
  return f"https://swamp.finance/static/frontend/api-public/api-{bc}-pools.json"

grimApy = "https://api.grim.finance/apy/breakdown"
grimTvl = "https://api.grim.finance/tvl"