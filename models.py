from sqlalchemy.dialects.mysql import VARCHAR
# from sqlalchemy.dialects.mssql import VARCHAR
# from sqlalchemy.dialects.oracle import VARCHAR
# from sqlalchemy.dialects.sqlite import VARCHAR
from sqlalchemy import Column, ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Province(db.Model):
  __tablename__ = "Provinces"

  code = Column(VARCHAR(20), primary_key=True)
  name = Column(VARCHAR(255), nullable=False)
  name_en = Column(VARCHAR(255))
  full_name = Column(VARCHAR(255), nullable=False)
  full_name_en = Column(VARCHAR(255))
  code_name = Column(VARCHAR(255))
  center = Column(VARCHAR(100))

  def __init__(self, code, name, name_en, full_name, full_name_en, code_name, center):
    self.code = code
    self.name = name
    self.name_en = name_en
    self.full_name = full_name
    self.full_name_en = full_name_en
    self.code_name = code_name
    self.center = center

class District(db.Model):
  __tablename__ = "Districts"

  code = Column(VARCHAR(20), primary_key=True)
  name = Column(VARCHAR(255), nullable=False)
  name_en = Column(VARCHAR(255))
  full_name = Column(VARCHAR(255), nullable=False)
  full_name_en = Column(VARCHAR(255))
  code_name = Column(VARCHAR(255))
  province_code = Column(VARCHAR(20), ForeignKey(Province.code))
  center = Column(VARCHAR(100))

  def __init__(self, code, name, name_en, full_name, full_name_en, code_name, province_code, center):
    self.code = code
    self.name = name
    self.name_en = name_en
    self.full_name = full_name
    self.full_name_en = full_name_en
    self.code_name = code_name
    self.province_code = province_code
    self.center = center

class Ward(db.Model):
  __tablename__ = "Wards"

  code = Column(VARCHAR(20), primary_key=True)
  name = Column(VARCHAR(255), nullable=False)
  name_en = Column(VARCHAR(255))
  full_name = Column(VARCHAR(255), nullable=False)
  full_name_en = Column(VARCHAR(255))
  code_name = Column(VARCHAR(255))
  district_code = Column(VARCHAR(20), ForeignKey(District.code))
  center = Column(VARCHAR(100))

  def __init__(self, code, name, name_en, full_name, full_name_en, code_name, district_code, center):
    self.code = code
    self.name = name
    self.name_en = name_en
    self.full_name = full_name
    self.full_name_en = full_name_en
    self.code_name = code_name
    self.district_code = district_code
    self.center = center
