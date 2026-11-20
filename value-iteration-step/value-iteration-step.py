import numpy as np
def value_iteration_step(values: list, transitions: list, rewards: list, gamma: float) -> list[float]:
    """
    Returns one updated floating-point value for every state.
    """
    # Write code here
    R = np.asarray(rewards, dtype = float)
    T = np.asarray(transitions, dtype = float)
    V = np.asarray(values, dtype = float)
    finalResult = []
    for s1 in range(len(T)):
        result = []
        for a in range(len(T[s1])):
            expected = 0.0
            for s in range(len(T[s1][a])):
                expected += T[s1][a][s] * V[s]
            Q = R[s1][a] +gamma* expected
            result.append(Q)
        finalResult.append(np.max(result))
    return finalResult