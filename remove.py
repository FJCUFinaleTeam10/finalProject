def Remove(Theta_x, P_x):
    out_index = []
    for i in range(len(Theta_x)):
        for k in P_x:
            if Theta_x[i].label == k.label:
                out_index.append(i)

    out_index.reverse()
    print(out_index)

    for i in out_index:
        Theta_x.pop(i)

    return Theta_x

# This function removes the postponed orders
# and the according restaurant visits from
# the planned routes
