import random


def NormolizeValue(v):
    if (v > self.maxParamValue):
        v = self.maxParamValue
    if (v < self.minParamValue):
        v = self.minParamValue
    return v
# } def

class Action:
    #_paramValues = [0.5]
    #_resultEstimation = 0
    #_patternId = 0
    #_minParamValue = 0
    #_maxParamValue = 1.0

    def __init__(self):
        self._paramValues = [0.5]
        self._resultEstimation = 0
        self._patternId = 0
        self._minParamValue = 0
        self._maxParamValue = 1.0

    def SetNewParamValue(self, pv, i):
        if (pv > self._maxParamValue):
            pv = self._maxParamValue
        if (pv < self._minParamValue):
            pv = self._minParamValue
        self._paramValues[i] = pv

class Pattern:
    index = 0

class KBColumn:
    _actionList = []
    _countOfActionsGenerated = 0
    _lastActionGenerated = None
    _lastRelativeEstimation = 0
    _stepLength = 0.5

    def _init__(self):
        self._actionList = []
        self._countOfActionsGenerated = 0
        self._lastActionGenerated = None
        self._lastRelativeEstimation = 0
        self._stepLength = 0.5

    def GetBestAction(self):
        if (len(self._actionList) <= 0):
            action = Action()
            action._paramValues = [0.5]
            return action
        else:
            bestAction = None
            bestEst = -999999
            for action in self._actionList:
                if (action._resultEstimation > bestEst):
                    bestEst = action._resultEstimation
                    bestAction = action
            return bestAction
    #}GetBestAction

    def GenerateNewAction(self):
        curBestAction = self.GetBestAction()
        action = Action()
        if (self._lastRelativeEstimation >= 0 or self._countOfActionsGenerated < 2):
            deltaV = (2 * random.random() - 1.0) * self._stepLength
            newVal = curBestAction._paramValues[0] + deltaV
            action.SetNewParamValue(newVal, 0)
            self._stepLength *= 0.94
        else:
            action = curBestAction
        ########################
        self._countOfActionsGenerated += 1
        self._lastActionGenerated = action
        return action

    def ReceiveRelativeEstimation(self, est):
        if (isinstance(self._lastActionGenerated, Action) == False):
            return
        self._lastRelativeEstimation = est
        ############
        prevAction = self.GetBestAction()
        if (est >= 0):
            self._lastActionGenerated._resultEstimation = prevAction._resultEstimation + 1.0
        else:
            self._lastActionGenerated._resultEstimation = prevAction._resultEstimation - 0.5
        ############
        self._actionList.append(self._lastActionGenerated)



class AdaptiveControlSystem:
    _kb = dict({0 : KBColumn()})
    _lastActionToEstimate = "null"
    _lastActionRelativeEstimation = 0


    def GetBestAction(self, pattern):
        patternId = 0#TODO: to complete
        curColumn = self._kb[patternId]
        return curColumn.GetBestAction()

    def GenerateNewAction(self, pattern):
        patternId = 0  # TODO: to complete
        curColumn = self._kb[patternId]
        action = curColumn.GenerateNewAction()
        self._lastActionToEstimate = action
        return action
    # } def

    def ReceiveRelativeEstimation(self, est):
        if (isinstance(self._lastActionToEstimate, Action) == False):
            return
        self._lastActionRelativeEstimation = est
        ############
        self._kb[self._lastActionToEstimate._patternId].ReceiveRelativeEstimation(est)





