class Q2:
    def __init__(self, is_valid_q0=False, is_valid_q1=False):
        self.is_valid_q0 = is_valid_q0
        self.is_valid_q1 = is_valid_q1
        self.is_valid = self.analyze_q2()

    def analyze_q2(self):
        return self.is_valid_q0 and self.is_valid_q1

    @property
    def is_valid_q0(self):
        return self._is_valid_q0

    @is_valid_q0.setter
    def is_valid_q0(self, value):
        self._is_valid_q0 = value

    @property
    def is_valid_q1(self):
        return self._is_valid_q1

    @is_valid_q1.setter
    def is_valid_q1(self, value):
        self._is_valid_q1 = value

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value
