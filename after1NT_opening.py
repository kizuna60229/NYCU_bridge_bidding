def after1NT_opening(num,bid,min_bid,bid_list):
    bid_mean = 'nothing to say'
    length = len(bid_list)-1
    print(length,bid_list)
    # 第一個叫品
    if bid == '1NT':
        bid_mean = 'bal, 15-17HCP'
    # 第二個叫品
    elif (num+1) <= length:
        if bid_list[num+1] == 'P':
            bid_mean = 'nothing to say'
            # 第三個叫品(無插叫)
            if (num+2) <= length:
                if bid_list[num+2] == '2C':
                    bid_mean = 'stayman : ask 4M'
                    #第四個叫品(假設pass)
                    if (num+3) <= length:
                        if bid_list[num+3] == 'P':
                            bid_mean = 'nothing to say'
                            #第五個叫品(無插叫,stayman後續)
                            if (num+4) <= length:
                                if bid_list[num+4] == '2D':
                                    bid_mean = 'no 4M'
                                #後續還沒寫
                        else:
                            bid_mean = '還沒寫或是沒約定'
                elif bid_list[num+2] == '2D':
                    bid_mean = 'transfer to 2H'
                elif bid_list[num+2] == '2H':
                    bid_mean = 'transfer to 2S'
                elif bid_list[num+2] == '2S':
                    bid_mean = 'ask minor'
                elif bid_list[num+2] == '2NT':
                    bid_mean = 'bal, inv'
                elif bid_list[num+2] == '3C':
                    bid_mean = '6C only have AQ or KQ'
                elif bid_list[num+2] == '3D':
                    bid_mean = '6D only have AQ or KQ'
                elif bid_list[num+2] == '3H':
                    bid_mean = '6+H SL'
                elif bid_list[num+2] == '3S':
                    bid_mean = '6+S SL'
                elif bid_list[num+2] == '3NT':
                    bid_mean = 'To play'
                elif bid_list[num+2] == '4C':
                    bid_mean = 'Ask A (04123)'
                elif bid_list[num+2] == '4D':
                    bid_mean = 'transfer to 4H'
                elif bid_list[num+2] == '4H':
                    bid_mean = 'transfer to 4S'
                elif bid_list[num+2] == '4S':
                    bid_mean = 'good quant'
                elif bid_list[num+2] == '4NT':
                    bid_mean = 'bad quant'
                else:
                    bid_mean = '沒約定'
        elif bid_list[num+1] == 'X':
            bid_mean = 'Meckwell Dont : 1m or 2M \n二線蓋叫以上點力'
        elif bid_list[num+1] == '2C':
            bid_mean = 'Meckwell Dont : 5+C and 4+M \n二線蓋叫以上點力'
        elif bid_list[num+1] == '2D':
            bid_mean = 'Meckwell Dont : 5+D and 4+M \n二線蓋叫以上點力'
        elif bid_list[num+1] in {'2H','2S'}:
            bid_mean = 'Nature \n二線蓋叫以上點力'
        elif bid_list[num+1] == '2NT':
            bid_mean = 'Unusual 2NT \n中性以上'
        elif bid_list[num+1] == '4NT':
            bid_mean = 'choose 5X'
        else:
            bid_mean = '建設性'
    else:
        bid_mean = '還沒寫或是沒約定'

    return bid_mean