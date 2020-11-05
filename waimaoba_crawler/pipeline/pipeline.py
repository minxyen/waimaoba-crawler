from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        passing_data = None
        for step in self.steps:
            try:
                passing_data = step.process(passing_data, inputs)
            except StepException as e:
                print('Exception Happened', e)
                break
