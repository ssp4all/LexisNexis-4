import re
sentence  = []

def compar(state, idi):
    with open('combine.json', 'r') as f:
        data = json.load(f)
        lst = data["final"]
        for each_state in lst:
            if list(each_state.keys())[0] == state:
                d = {}
                v = []
                #d[list(lstn[ind].keys())[0]]
                all_id = list(each_state.values())[0]
                for eachid in all_id:
                    if eachid[0] == idi:
                        sp = eachid[1]
                        return sp
    
    return ""



print(compar("AK", "18:1957"))
