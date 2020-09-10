from sys import argv
from df_insights_def import *
from outlook_usage_stats import *

def calculateOutlookUsageInsights(inpDate):
	"""calculate outlook usage insights for the given date"""
	try:
           insightsDefs=getInsightsDef()
           totalUsageTime = 0;

           for indx, idDef in insightsDefs.iterrows():
               if (idDef.InsightName == "OutlookUsageTime"):
                   outlookUsageData = getDataFromDate(inpDate)
                   for i in outlookUsageData:
                      totalUsageTime += int(i[3])
                   #print("\nSample insights calculated from the IE\n")
                   #print (idDef.DisplayTextTemplate.format(totalUsageTime))
                   return (idDef.DisplayTextTemplate.format(totalUsageTime))
	except Exception as e:
		#print(e)
		return(e)

if __name__ == '__main__':
    print(calculateOutlookUsageInsights(argv[1]))

