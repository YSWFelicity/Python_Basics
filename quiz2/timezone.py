# Function to convert EST to PST
def est_to_pst(time_est):
    time_split =time_est.split(":",1)
    hour=time_split[0] 
    if hour=="00":
        hour="21"
    elif hour=="01":
        hour="22"
    elif hour=="02":
        hour="23"
    else:
        hour = int(hour)-3
    if len(str(hour))==1:
        hour = "0"+str(hour)
    time_pst = str(hour)+":"+str(time_split[1])
    return(time_pst)