"""a main class for the project"""
import os
from sqlalchemy importfrom os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base