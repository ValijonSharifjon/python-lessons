# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:32:49 2022

@author: Asus
"""
from firststep import Shaxs
  
class Talaba(Shaxs):
    num_talaba=0
    
    def __init__(self,firstname,lastname,id,sex,nationality,grade,faculty):
        super().__init__(firstname,lastname,id,sex,nationality)
        self.grade=grade
        self.faculty=faculty
        Talaba.num_talaba+=1
        
    def add_grade(self,new):
        self.grade=new
        
    def get_info(self):
        return f'{self.firstname} {self.lastname}  {self.grade} {self.faculty}'
    @classmethod
    def get_num_talaba(cls):
        return cls.num_talaba
    
talaba1=Talaba('Valijon','Sharifjonov','AC221','male','Uzb',2,'Enginering')
print(talaba1.get_num_talaba())    
        