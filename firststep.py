# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:19:43 2022

@author:Asus """
class Shaxs:
    def __init__(self,firstname,lastname,id,sex,nationality):
        self.firstname=firstname
        self.lastname=lastname
        self.__id=id
        self.sex=sex
        self.nationality=nationality
        
        
    def get_id(self):
        return self.__id
    
    def update_nat(self,new):
        self.nationality=new
        
        
    
        

        
        
    
        