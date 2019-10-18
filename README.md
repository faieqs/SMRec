This project contains the data and the code for the paper called "A Context-aware Recommendation-based System for Service Composition in Smart Environments"

invocations.csv file contains the data which was generated based on a simulation of the case study presented in the paper called 'SMARTROAD' and is structured as follows:

- Users_ID : Represents the ID of the user and respects the same numbering as the WSDREAM dataset.

- Service_Model : Represents the name of the Service Model as depicted in the paper. The data contains 7 Service_Models (TrafficCongestion, RiskyVehicleSpeed, RiskyDriverHealth, RiskyDriverExperience, RiskyRoad, BadWeather, RiskyVehicleState). Only three of these service models were depicted in the paper.

- Task_Name : Represents the name of the Task as depicted in the paper. The data contains 20 tasks (TJAW_I, ISA_E, RSS_E, IVS_I, ERP_I, ISA_I, NAAS_E, ERP_E, IVS_V, NAAS_I, ERS, RSS_V, AEVW, RWW, RSS_I, WWS, GSS_V, GSSS, GSS_I, TSS_V). Each task name is divided to two parts by the underscore character. The left part is the acronym of the task and the right part represents the level at which the task is executed by the service.

- Service_ID : Represents the ID of the service and respects the same numbering as the WSDREAM dataset. Each service was associated with a task and hench has a Task_Name.

- ResponseTime : Is a QoS measure that represents the lapse of time from the invocation request by the user to the service reply in seconds and is extracted from the WSDREAM dataset.

- Throughput : Is a QoS measure that represents the amount of data transiting between the user and the service in Kbps and is extracted from the WSDREAM dataset.
