class SensorStabilizer:
    def __init__(self, threshold:float=0.01, window_size:int=5, is_stable_number:int=3):
        """
        Initializes the SensorStabilizer with given parameters.
        :param threshold: Maximum allowed deviation from the mean to consider stable.
        :param window_size: Number of recent values to consider.
        :param is_stable_number: Number of consecutive stable readings required.
        """
        self.threshold:float = threshold
        self.window_size:int = window_size
        self.is_stable_number:int = is_stable_number
        self._is_stable_counter = 0
        self._value_list = []
    
    def value_is_stable(self, value:float) -> bool:
        """
        Checks if the sensor value is stable based on recent readings.
        :param value: New sensor value to check.
        :return: True if stable, otherwise False.
        """
        self.__add(value)
        
        if len(self._value_list) < self.window_size:
            return False
        
        value_mean = sum(self._value_list) / len(self._value_list)
        change = abs(value - value_mean)
        
        if change <= self.threshold:
            self._is_stable_counter += 1
        else:
            self._is_stable_counter = 0
        
        return self._is_stable_counter >= self.is_stable_number
    
    def __add(self, value):
        """
        Adds a new value to the list while maintaining the window size.
        :param value: New sensor value.
        """
        if len(self._value_list) >= self.window_size:
            self._value_list.pop(0)
        self._value_list.append(value)
    
    def clear(self):
        """
        Resets the stabilizer by clearing the values and counter.
        """
        self._is_stable_counter = 0
        self._value_list.clear()
