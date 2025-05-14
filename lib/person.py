#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name= "John Doe"):
        self.name = name
    def __init__(self, job= "Admin"):
        self.job = job
    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name,str) and (1 <= len(name) <= 25):
            print(f"Setting name to { name }.")
            self._name = name
        else:
            print("Name must be a string between 1 and 25.")
    name = property(get_name, set_name)

    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
