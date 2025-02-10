from src.logic.parametersCalc import ParametersCalculate

def test_tds_calc(voltage:float):
    parametersC = ParametersCalculate()
    return parametersC.calculateTds(32,voltage)

if __name__ == '__main__':
    inputs = [0.305]
    outputs = [706.5]
    test_passed = 0
    for i in range(len(inputs)):
        result = test_tds_calc(inputs[i]) * 1e6
        print("******************************")
        print(f"TEST #{i+1}")
        print(f"EXPECTED: Between {outputs[i]*0.95} to {outputs[i]*1.05}")
        print(f"OUTPUT: {result}")
        if outputs[i]*0.95 <= result <= outputs[i]*1.05:
            test_passed += 1
            print(f"TEST PASSED")
        else:
            print(f"TEST FAILED")
    print("******************************")
    print(f"RESULT: {test_passed}/{len(inputs)} PASSED")
            