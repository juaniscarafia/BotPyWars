# Example responses:
#
# Move forwards:
#   return {'ACTION': 'MOVE', 'WHERE': 1}
#
# Move backwards:
#   return {'ACTION': 'MOVE', 'WHERE': -1}
#
# Shooting projectile:
#   return {'ACTION': 'SHOOT', 'VEL': 100, 'ANGLE': 35}
#   # 'VEL' should be a value x, 0 < x < 150
#   # 'ANGLE' should be an x, 10 <= x < 90
#
#
# Do nothing:
#   return None
#
# For full API description and usage please visit the Rules section
import random

class Bot(object):

    def evaluate_turn(self, feedback, life):
        '''
        :param feedback: (dict) the result of the previous turn,
            ie: for the move action 'SUCCESS' is returned when the enemy
            received a hit, or 'FAILED' when missed the shot.
        {'RESULT': 'SUCCESS' | 'FAILED', Result of the action
         'POSITION': (x, y) | None, In case of move success, or at start
         'MISSING': 'HOT' | 'WARM' | 'COLD' | None, Depending how close the last
         impact was, if applicable }
        :param life: Current life level, An integer between between 0-100.
        :return: see the comments above
        '''

        result = {}

        if feedback['ACTION'] == None:
            result = {'ACTION':'SHOOT','ANGLE': 45, 'VEL': 100}
            oldResult = {'ACTION':'SHOOT','ANGLE': 45, 'VEL': 100}
            oldLife = life

        if life >= oldLife:
            if feedback['RESULT'] == 'SUCCESS':
                if oldResult['ACTION'] == 'SHOOT':
                    result = oldResult
                else:
                    result = {'ACTION':'SHOOT','ANGLE': 25, 'VEL': 100}
            else:
                if oldResult['ACTION'] == 'SHOOT':
                    result = oldResult
                    if feedback['MISSING'] == 'HOT':
                        i = random.randint(0,1)
                        if i == 0:
                            result['ANGLE'] = result['ANGLE'] - 5
                        else:
                            result['ANGLE'] = result['ANGLE'] + 5
                    elif feedback['MISSING'] == 'WARM':
                        i = random.randint (0,1)
                        if i == 0:
                            result['ANGLE'] = result['ANGLE'] - 10
                            if result['ANGLE'] > 60:
                                result['ANGLE'] = 60
                        else:
                            result['ANGLE'] = result['ANGLE'] + 10
                            if result['ANGLE'] < 10:
                                result['ANGLE'] = 10
                    elif feedback['MISSING'] == 'COLD':
                        i = random.randint (0,1)
                        if i == 0:
                            result['ANGLE'] = result['ANGLE'] - 15
                            if result['ANGLE'] > 60:
                                result['ANGLE'] = 60
                        else:
                            result['ANGLE'] = result['ANGLE'] + 15
                            if result['ANGLE'] < 10:
                                result['ANGLE'] = 10
        else:
            i = random.randint (0,1)
            if i == 0:
                result = {'ACTION':'MOVE','WERE': 1}
            else:
                result = {'ACTION':'MOVE','WERE': -1}

        oldLife = life
        oldResult = result
        return result