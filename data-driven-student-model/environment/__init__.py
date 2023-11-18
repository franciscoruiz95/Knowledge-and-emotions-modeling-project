from environment.StudentModel import StudentModel

from gym.envs.registration import register

register(
    id="StudentModel-v1",
    entry_point='environment.StudentModel:StudentModel'
)

(StudentModel,)