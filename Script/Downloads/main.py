import requests

http_url_prod = "http://*:8080/v5/stock/quote.json?symbol={}&extend=detail"
http_url_sep = "http://*:8080/v5/stock/quote.json?symbol={}&extend=detail"

REUTER_SYMBOL_MISSING = []
REUTER_QUOTE_STRUCTURE_ERROR = []
REUTER_QUOTE_TYPE_ERROR = []
REUTER_QUOTE_TICK_SIZE_ERROR = []
REUTER_QUOTE_VALUE_ERROR = []

headers = {
    'User-Agent': 'Xueqiu iPhone 11.8',
    'accept': 'application/json',
    'ept-language': 'zh-Hans-CN;q=1',
    'accept-encoding': 'br, gzip, deflate',
    'Cookie': 'u=1767539047; xq_a_token=26c5753ad9310c1d3e11d9c22ce1769b5263cec5'
}

headers_sep = {
    'User-Agent': 'Xueqiu iPhone 11.8',
    'accept': 'application/json',
    'ept-language': 'zh-Hans-CN;q=1',
    'accept-encoding': 'br, gzip, deflate',
    'Cookie': 'u=961593593472421; xq_a_token=c7371de8d5dcb647240fa15474ee79f002760c17'
}

symbol_path = "HK.csv"

OFFSET = 0.02
Record = "HK.log"


def diff(symbol_string):
    print("Parsing: " + symbol_string)
    idc = requests.get(http_url_prod.format(symbol_string), headers=headers)

    idc_quote = idc.json()['data']['quote']

    reuter = requests.get(http_url_sep.format(symbol_string), headers=headers_sep)

    reuter_quote = reuter.json()['data']['quote']

    with open(Record, "a") as file_h:
        file_h.write(str(idc_quote) + "\n")
        file_h.write(str(reuter_quote) + "\n\n")


# 路透接口返回没有quote结构
    if reuter_quote is None and idc_quote is not None:
        REUTER_SYMBOL_MISSING.append(symbol_string)
        return

    if idc_quote is None:
        return

    # 路透接口返回quote结构缺少字段
    delta = set(idc_quote.keys()) - set(reuter_quote.keys())
    if delta:
        REUTER_QUOTE_STRUCTURE_ERROR.append({symbol_string: list(delta)})

    temp_type_list = []
    temp_value_list = []
    temp_tick_size_list = []

    for key in set(idc_quote.keys()) - delta:
        idc_value = idc_quote[key]
        reuter_value = reuter_quote[key]

        if type(idc_value) is not type(reuter_value):
            temp_type_list.append(key)
            # print(key + ": type error")
            continue

        if isinstance(idc_value, int):
            if idc_value == 0 and reuter_value == 0:
                continue
            if idc_value == 0 and reuter_value != 0:
                temp_value_list.append(key)
            if idc_value != 0 and abs((reuter_value-idc_value)/idc_value) > OFFSET:
                temp_value_list.append(key)
        elif isinstance(idc_value, float):
            if idc_value == 0 and reuter_value != 0:
                temp_value_list.append(key)
            if idc_value != 0 and abs((reuter_value-idc_value)/idc_value) > OFFSET:
                temp_value_list.append(key)
            if len(str(idc_value).split(".")[1]) != len(str(reuter_value).split(".")[1]):
                temp_tick_size_list.append(key)
        elif (idc_value is True and reuter_value is False) or (idc_value is False and reuter_value is True):
            temp_value_list.append(key)
        elif isinstance(idc_value, str):
            if idc_value != reuter_value:
                temp_value_list.append(key)

    if len(temp_type_list) > 0:
        REUTER_QUOTE_TYPE_ERROR.append({symbol_string: temp_type_list})
    if len(temp_value_list) > 0:
        REUTER_QUOTE_VALUE_ERROR.append({symbol_string: temp_value_list})
    if len(temp_tick_size_list) > 0:
        REUTER_QUOTE_TICK_SIZE_ERROR.append({symbol_string: temp_tick_size_list})


if __name__ == '__main__':
    if False:
        symbol_list = []
        with open(symbol_path) as file_handler:
            for symbol in file_handler:
                symbol_list.append(symbol.rstrip().lstrip())
        for single_symbol in symbol_list:
            diff(single_symbol)

        print(REUTER_SYMBOL_MISSING)
        print(len(REUTER_SYMBOL_MISSING))
        print(REUTER_QUOTE_STRUCTURE_ERROR)
        print(len(REUTER_QUOTE_STRUCTURE_ERROR))
        print(REUTER_QUOTE_TYPE_ERROR)
        print(len(REUTER_QUOTE_TYPE_ERROR))
        print(REUTER_QUOTE_TICK_SIZE_ERROR)
        print(len(REUTER_QUOTE_TICK_SIZE_ERROR))
        print(REUTER_QUOTE_VALUE_ERROR)
        print(len(REUTER_QUOTE_VALUE_ERROR))

    temp = "00325"

    idc_data = requests.get(http_url_prod.format(temp), headers=headers)
    print(idc_data.json())

    reuter_data = requests.get(http_url_sep.format(temp), headers=headers_sep)
    print(reuter_data.json())

    diff(temp)

    print(REUTER_SYMBOL_MISSING)
    print(len(REUTER_SYMBOL_MISSING))
    print(REUTER_QUOTE_STRUCTURE_ERROR)
    print(len(REUTER_QUOTE_STRUCTURE_ERROR))
    print(REUTER_QUOTE_TYPE_ERROR)
    print(len(REUTER_QUOTE_TYPE_ERROR))
    print(REUTER_QUOTE_TICK_SIZE_ERROR)
    print(len(REUTER_QUOTE_TICK_SIZE_ERROR))
    print(REUTER_QUOTE_VALUE_ERROR)
    print(len(REUTER_QUOTE_VALUE_ERROR))
