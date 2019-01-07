from fastai import *          # Quick accesss to most common functionality
from fastai.tabular import *  # Quick accesss to tabular functionality
stations = pd.read_csv("../data/stations.csv")

def predict_journeys(learner,dataset):
    "This can be something that is already in the framework."
    result = 0
    accuracy = 0
    for x in range(0,dataset.shape[0]):
        correct = dataset.iloc[x].journey  #remove journey
        predicted = learner.predict(dataset.iloc[x]);
        if (str(correct)==str(predicted[0])):
            result=result+1
    accuracy=result/dataset.shape[0]
    return(accuracy)

def predict_journey(learner,detectedActivity,geoHash,minuteOfday,weekday):
    data = np.array([['','detectedActivity','geoHash','minuteOfDay','weekday'],
                ["row1",detectedActivity,geoHash,minuteOfday,weekday]])            
    dr=pd.DataFrame(data=data[1:,1:],
                    index=data[1:,0],
                    columns=data[0,1:]).astype(np.int64)
    predicted = learner.predict(dr.iloc[0])
    return(predicted[0],str(round(predicted[2].max().item(),2)))

def make_shure_we_got_enough_rows(dataset,minrows=1000):
    "If the dataset has fewer rows that minrows, whole dataset copies will be added at the end until at least minrows exists"
    newset = pd.DataFrame()
    while newset.shape[0]<minrows:
        newset = pd.concat([newset,dataset])
    return(newset)

def save_results(filename,result):
    a = np.asarray(result)
    np.savetxt("saved/"+filename,a,delimiter=',',fmt="%10.2f")
    
def from_to(journey_code):
    if(len(str(journey_code))==10):
        fromStationNbr = str(journey_code)[0:5]
        try:
            fromStationNbr = stations.loc[stations['stationId']==int(fromStationNbr)]['stationName'].iloc[0]
        except:
            fromStationNbr = str(journey_code)[0:5]
        toStationNbr = str(journey_code)[5:10]
        try:
            toStationNbr = stations.loc[stations['stationId']==int(toStationNbr)]['stationName'].iloc[0]
        except:
            toStationNbr = str(journey_code)[5:10]
        return fromStationNbr+"->"+toStationNbr
    else:
        return journey_code 
    
def from_to_id(journey_code):
    if(len(str(journey_code))==10):
        return str(journey_code)[0:5]+"->"+str(journey_code)[5:10]
    else:
        return journey_code 
    
def evaluate_learning(learner,testset):
    result = []
    #result.append(["prediction","accuracy","day"])
    for row in testset.itertuples():
        row.Index
        predicted = learner.predict(row)
        result.append([predicted[0],round(predicted[2].max().item(),2),row[4],row[5]])
    return (result)