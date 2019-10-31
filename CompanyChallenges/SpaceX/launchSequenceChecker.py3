# https://app.codesignal.com/company-challenges/spacex/EcQD8xYZotKM77FKM
def launchSequenceChecker(systemNames, stepNumbers):

        uniqueSystems = dict()

        for i in range(len(systemNames)):
                
                if systemNames[i] not in uniqueSystems:
                        uniqueSystems[systemNames[i]] = [ stepNumbers[i] ]     
                elif stepNumbers[i] > uniqueSystems[systemNames[i]][-1]:
                        uniqueSystems[systemNames[i]].append(stepNumbers[i])
                else:
                        return False
        
        return True   