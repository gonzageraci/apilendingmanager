from flask.json import jsonify
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
import json
import url

def getAutofarm(bc):
    pools = {}
    r = requests.get(url.autofarm(bc)).json()
    for id in r["pools"]:
        if r["pools"][id]["wantIsLP"] == True:
            if r["pools"][id]["APY_total"] == None or r["pools"][id]["APY_total"] == "None" or r["pools"][id]["APY_total"] == 0 or r["pools"][id]["APY_total"] == "0" :
                continue
            else:
                #print (r["pools"][i]["wantName"]+" | "+str(r["pools"][i]["APY_total"]) + " | " + "Autofarm " + str(r["pools"][i]["farmName"]) +" | "+ str(bc))
                poolName = r["pools"][id]["wantName"]
                poolApy = r["pools"][id]["APY_total"]
                poolFarm = r["pools"][id]["farmName"]
                poolYield = "Autofarm"
                poolBC = str(bc)
                pools[str(id)] =  {"symbol":str(poolName), "apy":str(poolApy), "farm":str(poolFarm), "yield_optimizer":str(poolYield), "blockchain":poolBC}
    return pools

def getAutofarmFull():
    fullPools = {}
    for bc in url.autofarm_blockchain:
        pools={}
        r = requests.get(url.autofarm(bc)).json()
        for id in r["pools"]:
            if r["pools"][id]["wantIsLP"] == True:
                if r["pools"][id]["APY_total"] == None or r["pools"][id]["APY_total"] == "None" or r["pools"][id]["APY_total"] == 0 or r["pools"][id]["APY_total"] == "0" :
                    continue
                else:
                    #print (r["pools"][i]["wantName"]+" | "+str(r["pools"][i]["APY_total"]) + " | " + "Autofarm " + str(r["pools"][i]["farmName"]) +" | "+ str(bc))
                    poolName = r["pools"][id]["wantName"]
                    poolApy = r["pools"][id]["APY_total"]
                    poolFarm = r["pools"][id]["farmName"]
                    poolYield = "Autofarm"
                    poolBC = str(bc)
                    pools[str(id)] =  {"symbol":str(poolName), "apy":str(poolApy), "farm":str(poolFarm), "yield_optimizer":str(poolYield), "blockchain":poolBC}
        fullPools[str(bc)] = pools
    return fullPools

def getBeefy(bc):
    blockchains = {"56":"bsc",
                   "128":"heco",
                   "137":"polygon",
                   "250":"fantom",
                   "42161":"arbitrum",
                   "43114":"avax",
                   "1666600000":"harmony"}
    
    pools = {}

    for chain in blockchains:
        if bc == blockchains[chain]:
            bc = chain
    
    r = requests.get(url.beefy_tvl).json()
    r2 = requests.get(url.beefy_apy).json()
    id = 0
    for pool in r[bc]:
        try:
            tvl = r[bc][pool]
            apy = r2[pool]
            pools[str(id)] = {"symbol":str(pool), "tvl":tvl, "apy":apy}
            id = id + 1
        except KeyError:
            continue
    return pools
    

def getBeefyFull():
    blockchains = {"56":"bsc",
                   "128":"heco",
                   "137":"polygon",
                   "250":"fantom",
                   "42161":"arbitrum",
                   "43114":"avax",
                   "1666600000":"harmony"}
    pools = {}
    for bc in blockchains:
        pools[str(blockchains[bc])] = getBeefy(blockchains[bc])
    
    return pools

def getSwamp(bc):
  r = requests.get(url.swamp(bc)).json()
  pools = {}
  for id in r["pools"]:
    name = r["pools"][id]["currency"]
    apy = r["pools"][id]["apy"]
    tvl = r["pools"][id]["tvl"]
    farm = r["pools"][id]["platformDisplay"]
    status = r["pools"][id]["status"]
    deposit = r["pools"][id]["isDepositPaused"]
    if status == "deprecated" or deposit == True:
      continue
    else:
      pools[id] = {"name":name, "apy":apy, "tvl":tvl, "farm":farm}
  return pools

def getSwampFull():
    pools = {}
    for bc in url.grim_blockchain:
        pools[bc] = getSwamp(bc)
    return pools

def getGrim():
    pools = {}
    r1 = requests.get(url.grimTvl).json()
    r2 = requests.get(url.grimApy).json()
    id = 0
    for name in r2:
        try:
            tvl = r1["250"][name]
            apy = r2[name]["totalApy"]
            pools[id] = {"name":name, "tvl": tvl, "apy":apy}
            id = id + 1
        except:
            continue    
    return pools
"""
def penguin():
    r1 = requests.get(url.penguinTokens).json()
    
    for token in r1["tokens"]:
        address = token["address"]
        apr = requests.get(url.penguinApr+address).json()
        print(str(address) + "uwu" + str(apr))
"""
#penguin()

def getCoinMarketCap():
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'a39a503a-0a40-4f20-9760-43682032cc0c',
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url.coinmarket, params=parameters)
        data = json.loads(response.text)
        return(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return(e)    

def getYieldyak():
    r1 = requests.get(url.yieldyakFarms).json()
    r2 = requests.get(url.yieldyakApy).json()
    pools = []
    for i in r1:
        try:
            symbol = i["name"]
            address = i["address"]
            #tvl = i["totalSupply"]
            apy = r2[address]["apy"]
            apr = r2[address]["apr"]
            pool = {"symbol":symbol, "apy":apy, "apr":apr, "address":address}
        except:
            continue
        pools.append(pool)
    return pools

getYieldyak()