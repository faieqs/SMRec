import pandas as pd
import pyfpgrowth as fpg
from tabulate import tabulate

def get_service_models(user_id, invocations):
    userInvocations = invocations.groupby('Users_ID').get_group(user_id)
    user_service_models = []
    for index, user in userInvocations.iterrows():
        sm = str(user.Service_Model)
        if (sm not in user_service_models) and (sm != 'nan'):
            user_service_models.append(user.Service_Model)
    return user_service_models

# read the data
event_log = pd.read_csv('invocations.csv', sep=',')

# declare threshold variable p
p = 50

# declare output variable
r = []

# create an atomic events filter
is_atomic = event_log['Service_Model'].isna()

#extract the atomic event
atomic_events = event_log[is_atomic]

# group the events by the task name
grouped_atomic_events = atomic_events.groupby('Task_Name')

# group the events by service model
grouped_events_by_service_model = event_log.groupby('Service_Model')

# get distinct service models
distinct_service_models = event_log.Service_Model.unique().tolist()
distinct_service_models = [x for x in distinct_service_models if str(x) != 'nan']

# get the list of atomic events
unique_atomic_events = atomic_events.Task_Name.unique().tolist()

for uat in unique_atomic_events:
    users_gae=[]
    # get the list of users who invoked the atomic task uat
    for index, gae in grouped_atomic_events.get_group(uat).iterrows():
        users_gae.append(gae.Users_ID)

    service_models = []
    
    # get the service models invoked by each user who also invoked the atomic event
    for u in users_gae:
        service_models.append(get_service_models(u, event_log))
    
    # for each service model, count all the users and the number of users who invoked the service model
    # then check the patterns surpassing the threshold in the service models from the previous step
    # and then add it to the list if it doesn't exist already
    for distinct_service_model in distinct_service_models:
        gae_service_models = grouped_events_by_service_model.get_group(distinct_service_model)
        frequent_service_models = fpg.find_frequent_patterns(service_models, gae_service_models.Users_ID.nunique() * p/100)
        if frequent_service_models:
            most_frequent_sm = frequent_service_models.popitem()[0][0]
            if most_frequent_sm and ([most_frequent_sm, uat] not in r) :
                r.append([most_frequent_sm, uat])
print('This is the result')
print(tabulate(r, headers=['Service_Model', 'Atomic_Task'], tablefmt='orgtbl'))
                        
        
