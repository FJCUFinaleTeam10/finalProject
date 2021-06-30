from Math.distance import distance


# main function
def Slack(S, Routes, time_buffer, t_ba):
    Slacks: int = 0
    for routePerVehicle in Routes:
        for destination in routePerVehicle.get("route"):
            Slacks += max(0, destination.get("timeDeadline") + t_ba - time_buffer - destination.get("arriveTime"))
    return Slacks
    # For every route plan Θ̂, the function calculates
    # the sum of differences between arrival time aD and deadline over
    # all orders: max{0, (tD + ¯t)−(aD + b)}.
