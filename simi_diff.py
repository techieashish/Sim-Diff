import json


def sim_diff(orig, new):
    diff = {}
    if type(orig) != type(new):
        return True
    else:
        if type(orig) is dict and type(new) is dict:
            diff_test = False
            for key in orig:
                result = sim_diff(orig[key], new[key])
                if result is False:
                    diff_test = True

                    diff[key] = result

            for key in new:
                if key not in orig:
                    diff[key] = ("KeyNotFound", new[key])
                    diff_test = True

            if diff_test:
                return diff
            else:
                return False
        else:
            if str(orig) == str(new):
                return False
            else:
                return str(orig), str(new)
    return diff

if __name__ == '__main__':
    source = None
    desti = None
    with open("source.json", "r") as sour:
        source = json.load(sour)

    with open("dest.json", "r") as dest:
        desti = json.load(dest)
    print(sim_diff(source, desti))
