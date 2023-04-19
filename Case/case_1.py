import json, requests, random

UNISWAP_API = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"
QUERY = """
    {
    tokens{
        symbol   
    }
}"""

response = requests.post(UNISWAP_API, json={"query" : QUERY}) # Sending request to this url then, use above query
uni_tokens = json.loads(response.text)["data"]["tokens"] # token_pools is the list of every token pair in the pools

tokens = []
data = []

for token in uni_tokens:
    tokens.append(token['symbol'])

def get_pool():
    rd_elements = random.sample(tokens, 5)
    data.append({
        "id" : 0,
        "src_token" : rd_elements[0],
        "src_price" : 10,
        "dest_token" : rd_elements[1],
        "dest_price" : 1, 
        "ratio" : -1
        })

    data.append({
        "id" : 1,
        "src_token" : rd_elements[1],
        "src_price" : 5000,
        "dest_token" : rd_elements[2],
        "dest_price" : 5, 
        "ratio" : -3
        })

    data.append({
        "id" : 2,
        "src_token" : rd_elements[2],
        "src_price" : 0.1,
        "dest_token" : rd_elements[0],
        "dest_price" : 10,
        "ratio" : 2
        })

    data.append({
        "id" : 3,
        "src_token" : rd_elements[2],
        "src_price" : 2,
        "dest_token" : rd_elements[3],
        "dest_price" : 20,
        "ratio" : 1
        })

    data.append({
        "id" : 4,
        "src_token" : rd_elements[2],
        "src_price" : 4,
        "dest_token" : rd_elements[4],
        "dest_price" : 400,
        "ratio" : 2
        })

    json_format = {
        "pools" : data
    }
    # with open("Data/case_1.json", "w") as f:
    #     json.dump(json_format, f)
    return json_format

# with open("case_1.json", "w") as f:
#     json.dump(json_format, f)