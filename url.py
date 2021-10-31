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
"""
polycat_tokenlist = "https://raw.githubusercontent.com/polycatfi/polycat-default-token-list/master/polycat-default.tokenlist.json"
polycat_apr = "https://api.pangolin.exchange/pangolin/apr/"
"""
penguinApr = "https://api.pangolin.exchange/pangolin/apr/"

yieldyakFarms = "https://staging-api-dot-formal-shell-329203.uc.r.appspot.com/farms"
yieldyakApy = "https://staging-api-dot-formal-shell-329203.uc.r.appspot.com/apys"

coinmarket = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"