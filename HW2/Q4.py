############
# QUESTION 4
############

def interpolate(xy, x_hat):
    # Assume x_hat values are within x values range
    if len(xy) <= 1:
        raise ValueError('please enter at least two valid measurements')
    times_list = sorted([measure_tup[0] for measure_tup in xy])
    if all([req_x in times_list for req_x in x_hat]):
        return [(req_x, xy[times_list.index(req_x)][1]) for req_x in x_hat]
    req_x_zone_dic = {}
    for req_x in x_hat:
        for meas_index in range(len(xy) - 1):
            if times_list[meas_index] <= req_x <= times_list[meas_index + 1]:
                req_x_zone_dic[req_x] = meas_index
                break
    zone_lin_dic = {}
    lin = lambda tup1, tup2: lambda x: (tup2[1] - tup1[1]) / (tup2[0] - tup1[0]) * (x - tup1[0]) + tup1[1]
    for zone in sorted(list(set(req_x_zone_dic.values()))):
        zone_lin_dic[zone] = lin(xy[zone], xy[zone + 1])
    return [(req_x, zone_lin_dic[req_x_zone_dic[req_x]](req_x)) for req_x in x_hat]
